import base64
import enum
import io
import logging
import string
from typing import List, Optional, Tuple

import pyarrow as pa

from clickzetta.connector.v0._dbapi import MESSAGE_FIELD, proto_to_field
from clickzetta.connector.v0.enums import FetchMode
from clickzetta.connector.v0.utils import as_timezone

logger = logging.getLogger(__name__)


def safe_to_py_list(column):
    type = str(column.type)
    # pyarrow does not support type of type month_interval and day_time_interval, see this conversion:
    # https://github.com/apache/arrow/issues/29828
    if type == 'month_interval' or type == "day_time_interval":
        raise NotImplementedError(f"Datatype not supported - {type}. You can use `cast` function to "
                                  "convert to other types and try again.")
    return column.to_pylist()


def arrow_table_to_rows(table: pa.Table, schema: List, time_zone: Optional[str] = None) -> List[Tuple]:
    cols = [safe_to_py_list(c) for c in table.columns]
    row_count = table.num_rows
    rows = []
    for i in range(row_count):
        row = []
        for j, col in enumerate(cols):
            value = col[i]
            if value and schema and schema[j]:
                field_type = schema[j].field_type
                if field_type in ['TIMESTAMP_LTZ', 'TIMESTAMP_NTZ']:
                    value = as_timezone(value, time_zone, field_type == 'TIMESTAMP_NTZ')
            row.append(value)
        rows.append(tuple(row))
    return rows

class QueryDataType(enum.Enum):
    Memory = 0
    File = 1


class QueryData(object):
    def __init__(
            self,
            data: Optional[list],
            data_type: QueryDataType,
            file_list: list = None,
            schema: Optional[List] = None,
            time_zone: Optional[str] = None,
            *,
            pure_arrow_decoding: bool = False,
    ):
        self.data = data
        self.data_type = data_type
        self.file_list = file_list
        self.schema = schema
        self.time_zone: Optional[str] = time_zone
        self.current_file_index = 0
        self.memory_read = False
        self._pure_arrow_decoding = pure_arrow_decoding

    def read(self, fetch_mode=FetchMode.FETCH_ALL, size=0):
        if self.data_type == QueryDataType.Memory:
            if self.memory_read:
                return None
            self.memory_read = True
            return self.data
        elif self.data_type == QueryDataType.File:
            assert self.file_list is not None
            try:
                final_result = []
                if fetch_mode == FetchMode.FETCH_ONE:
                    file = self.file_list[0]
                    return self.get_presigened_file_input_stream(file)
                elif fetch_mode == FetchMode.FETCH_MANY:
                    for file in self.file_list:
                        final_result.extend(self.get_presigened_file_input_stream(file))
                        if len(final_result) >= size:
                            break
                else:
                    for file in self.file_list:
                        final_result.extend(self.get_presigened_file_input_stream(file))
                return final_result
            except Exception as e:
                raise Exception(f"Error while converting from file arrow to result: {e}")

    def get_presigened_file_input_stream(self, url: str) -> List:
        from clickzetta.connector.v0.client import _globals
        response = _globals["token_https_session"].get(url, stream=True)
        response.raise_for_status()
        result = []
        stream = io.BytesIO(response.content)
        with pa.ipc.RecordBatchStreamReader(stream) as reader:
            if self._pure_arrow_decoding:
                return arrow_table_to_rows(reader.read_all(), self.schema, self.time_zone)
            for index, row in reader.read_pandas().iterrows():
                result.append(tuple(row.to_list()))
            return result


class QueryResult(object):
    def __init__(self, total_msg, pure_arrow_decoding, timezone_hint=None):
        self.data = None
        self.panda_data = None
        self.state = None
        self.timezone_hint = timezone_hint
        self.total_row_count = 0
        self.total_msg = total_msg
        self.schema = []
        self._pure_arrow_decoding = pure_arrow_decoding
        self._parse_result_data()

    def get_result_state(self) -> string:
        return self.total_msg["status"]["state"]

    def get_arrow_result(self, arrow_buffer, time_zone: Optional[str] = None):
        try:
            buffer = base64.b64decode(arrow_buffer)
            with pa.ipc.RecordBatchStreamReader(io.BytesIO(buffer)) as reader:
                table = reader.read_all()
                column_dict = {}
                for index, column_name in enumerate(table.column_names):
                    if column_name in column_dict:
                        column_dict[f"{column_name}_{index}"] = index
                    else:
                        column_dict[column_name] = index
                new_table = table.rename_columns(list(column_dict.keys()))
                if self._pure_arrow_decoding:
                    return arrow_table_to_rows(new_table, self.schema, time_zone)
                result = []
                pandas_result = new_table.to_pandas()
                self.panda_data = pandas_result
                for index, row in pandas_result.iterrows():
                    result.append(tuple(row.tolist()))
                return result

        except Exception as e:
            logger.error(f"[get_arrow_result] Error while converting from arrow to result: {e}")
            raise Exception(f"[get_arrow_result] Error while converting from arrow to result: {e}")

    def get_result_schema(self):
        fields = self.total_msg["resultSet"]["metadata"]["fields"]
        self.schema = [proto_to_field(f) for f in fields]

    def _parse_result_data(self) -> None:
        if len(self.total_msg) == 0:
            return
        self.state = self.total_msg["status"]["state"]
        if self.state != "FAILED" and self.state != "CANCELLED":
            rst = self.total_msg["resultSet"]
            meta = rst["metadata"] if "metadata" in rst else {}
            time_zone = meta["timeZone"] if "timeZone" in meta else self.timezone_hint
            if "data" not in rst:
                if "location" in rst:
                    self.get_result_schema()
                    location = self.total_msg["resultSet"]["location"]
                    presigned_urls = location["presignedUrls"]
                    url_count = len(presigned_urls)
                    logger.info(f"location count: {url_count}")
                    if url_count == 0:
                        self.total_row_count = 0
                        self.data = QueryData(
                            data=[],
                            data_type=QueryDataType.Memory,
                            schema=self.schema,
                            time_zone=time_zone,
                            pure_arrow_decoding=self._pure_arrow_decoding,
                        )
                        return
                    self.data = QueryData(
                        data=None,
                        data_type=QueryDataType.File,
                        file_list=presigned_urls,
                        schema=self.schema,
                        time_zone=time_zone,
                        pure_arrow_decoding=self._pure_arrow_decoding,
                    )
                else:
                    self.schema = [MESSAGE_FIELD]
                    self.total_row_count = 1
                    result_data = [["OPERATION SUCCEED"]]
                    self.data = QueryData(
                        data=result_data,
                        data_type=QueryDataType.Memory,
                        schema=self.schema,
                        time_zone=time_zone,
                        pure_arrow_decoding=self._pure_arrow_decoding,
                    )
            else:
                if not (len(rst["data"]["data"])):
                    self.total_row_count = 0
                    self.get_result_schema()
                    self.data = QueryData(
                        data=[],
                        data_type=QueryDataType.Memory,
                        schema=self.schema,
                        time_zone=time_zone,
                        pure_arrow_decoding=self._pure_arrow_decoding,
                    )
                    return
                result_data = rst["data"]["data"]
                self.get_result_schema()
                query_result = []
                for row in result_data:
                    partial_result = self.get_arrow_result(row, time_zone=time_zone)
                    query_result.extend(entity for entity in partial_result)
                self.data = QueryData(
                    data=query_result,
                    data_type=QueryDataType.Memory,
                    schema=self.schema,
                    time_zone=time_zone,
                    pure_arrow_decoding=self._pure_arrow_decoding,
                )

        else:
            raise Exception(
                "SQL job execute failed.Error:" + self.total_msg["status"]["message"]
            )
