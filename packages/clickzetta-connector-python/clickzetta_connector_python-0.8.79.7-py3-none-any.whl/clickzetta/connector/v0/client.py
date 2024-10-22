"""Client for interacting with the ClickZetta API."""

from __future__ import absolute_import, division

import json
import logging
import os
import random
import re
import shutil
import threading
import time
import typing
import uuid
import warnings
from datetime import datetime, timedelta
from functools import partial
from typing import (
    IO,
    Any,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
)
from urllib.parse import unquote, urlparse

import requests
import requests.exceptions
from requests.adapters import HTTPAdapter
from sqlalchemy.engine.url import make_url
from urllib3 import Retry

from clickzetta.connector.v0._bulkload import import_bulkload_api
from clickzetta.connector.v0._volume import resolve_local_path
from clickzetta.connector.v0.enums import *
from clickzetta.connector.v0.exception import ClickzettaJobNotExistsException
from clickzetta.connector.v0.query_result import QueryData, QueryDataType, QueryResult
from clickzetta.connector.v0.table import Table
from clickzetta.connector.v0.utils import (
    BaseExecuteContext,
    execute_with_retrying,
    normalize_file_path,
    split_sql,
)

logger = logging.getLogger(__name__)
TIMEOUT_HEADER = "X-Server-Timeout"
TimeoutType = Union[float, None]
ResumableTimeoutType = Union[None, float, Tuple[float, float]]

if typing.TYPE_CHECKING:
    PathType = Union[str, bytes, os.PathLike[str], os.PathLike[bytes]]

_DEFAULT_CHUNKSIZE = 10 * 1024 * 1024  # 10 MB
_MAX_MULTIPART_SIZE = 5 * 1024 * 1024
_DEFAULT_NUM_RETRIES = 6
_GENERIC_CONTENT_TYPE = "*/*"

_MIN_GET_QUERY_RESULTS_TIMEOUT = 120
HTTP_PROTOCOL_DEFAULT_PORT = "80"
HTTPS_PROTOCOL_DEFAULT_PORT = "443"
HTTP_PROTOCOL_PREFIX = "http://"
HTTPS_PROTOCOL_PREFIX = "https://"

DEFAULT_TIMEOUT = None
DEFAULT_MAXIMUM_TIMEOUT = 60
HYBRID_SQL_TIMEOUT = 120

HEADERS = {"Content-Type": "application/json"}

_globals = globals()
_globals["token_https_session"] = None
_globals["token_https_session_inited"] = False
DEFAULT_INSTANCE_ID = 100
DEFAULT_EXPIRED_FACTOR = 0.8
DEFAULT_TOKEN_EXPIRE_TIME_MS = 2 * 60 * 60 * 1000
user_token_dict = {}
user_token_time_dict = {}
JOB_ALREADY_EXIST = "CZLH-60007"
JOB_NOT_EXIST = "CZLH-60005"
JOB_STATUS_UNKNOWN = "CZLH-60022"
JOB_NOT_SUBMITTED = "CZLH-60023"
JOB_TIME_OUT_KILLED = "CZLH-60010"
JOB_NEED_RE_EXECUTE = "CZLH-57015"


class Client(object):
    def __init__(
        self,
        username: str = None,
        password: str = None,
        instance: str = None,
        workspace: str = None,
        vcluster: str = None,
        cz_url: str = None,
        service: str = None,
        schema: str = "public",
        magic_token: str = None,
        protocol: str = None,
        hints: Dict = None,
        **extra,
    ):
        self.schema = None
        self.magic_token = None
        self.protocol: Optional[str] = protocol
        self.hints = hints
        self.lock = None
        self._token = None
        self.token_expire_time_ms = 0 if self.magic_token is not None else DEFAULT_TOKEN_EXPIRE_TIME_MS
        self._pure_arrow_decoding = True
        self.timezone_hint: Optional[str] = None
        if cz_url is not None:
            self._parse_url(cz_url)
            self.instance_id = 0
        else:
            if service is None:
                raise ValueError("ClickZetta connection url `service` is required.")
            else:
                if self.protocol is None:
                    self.protocol = "https"
                if self.protocol == "https":
                    self.service = (
                        HTTPS_PROTOCOL_PREFIX + service
                        if not service.startswith(HTTPS_PROTOCOL_PREFIX)
                        else service
                    )
                elif self.protocol == "http":
                    self.service = (
                        HTTP_PROTOCOL_PREFIX + service
                        if not service.startswith(HTTP_PROTOCOL_PREFIX)
                        else service
                    )
                else:
                    raise ValueError(
                        "protocol must be http or https. Other protocols are not supported yet."
                    )
            self._token = None
            self.workspace = workspace
            self.instance = instance
            self.vcluster = vcluster
            self.session = None
            self.instance_id = 0
            self.username = username
            self.schema = schema
            self.password = password
            self.magic_token = magic_token
            if "token_expire_time_ms" in extra:
                self.token_expire_time_ms = int(extra["token_expire_time_ms"])
        self.validate()
        if self.magic_token is None:
            self.lock = threading.Lock()
        self._token: str = self.token

    def _parse_url(self, url: str):
        url = make_url(url)
        query = dict(url.query)
        port = url.port

        self.instance = url.host.split(".")[0]
        length = len(self.instance) + 1

        if "protocol" in query:
            self.protocol = query.pop("protocol")
            if self.protocol == "http":
                if not port:
                    self.service = (
                        HTTP_PROTOCOL_PREFIX
                        + url.host[length:]
                        + ":"
                        + HTTP_PROTOCOL_DEFAULT_PORT
                    )
                else:
                    self.service = (
                        HTTP_PROTOCOL_PREFIX + url.host[length:] + ":" + str(port)
                    )
            else:
                raise ValueError(
                    "protocol parameter must be http. Other protocols are not supported yet."
                )
        else:
            self.protocol = "https"
            if not port:
                self.service = (
                    HTTPS_PROTOCOL_PREFIX
                    + url.host[length:]
                    + ":"
                    + HTTPS_PROTOCOL_DEFAULT_PORT
                )
            else:
                self.service = (
                    HTTPS_PROTOCOL_PREFIX + url.host[length:] + ":" + str(port)
                )

        self.workspace = url.database
        self.username = url.username
        self.password = url.password

        if (
            "virtualcluster" in query
            or "virtualCluster" in query
            or "vcluster" in query
        ):
            if "virtualcluster" in query:
                self.vcluster = query.pop("virtualcluster")
            elif "virtualCluster" in query:
                self.vcluster = query.pop("virtualCluster")
            else:
                self.vcluster = query.pop("vcluster")
        else:
            raise ValueError(
                "url must have `virtualcluster` or `virtualCluster` or `vcluster` parameter."
            )
        if "schema" in query:
            self.schema = query.pop("schema")
        if "magic_token" in query:
            self.magic_token = query.pop("magic_token")
        if "token_expire_time_ms" in query:
            self.token_expire_time_ms = int(query.pop("token_expire_time_ms"))

    def log_in_cz(self, username: str, password: str, instance: str) -> str:
      with self.lock:
        path = "/clickzetta-portal/user/loginSingle"
        login_params = LoginParams(username, password, instance)
        api_repr = login_params.to_api_repr()
        data = json.dumps(api_repr)
        try:
            if not _globals["token_https_session_inited"] or not _globals["token_https_session"]:
                session = requests.Session()
                retries = Retry(
                    total=3,
                    backoff_factor=1,
                    allowed_methods=frozenset(["GET", "POST"]),
                )
                session.mount(self.protocol + "://",
                              HTTPAdapter(pool_connections=20, pool_maxsize=100, max_retries=retries))
                _globals["token_https_session"] = session
                _globals["token_https_session_inited"] = True
            api_response = _globals["token_https_session"].post(self.service + path, data=data, headers=HEADERS,
                                                                timeout=10)
            if api_response.status_code != 200:
                raise requests.exceptions.RequestException(
                    "user:"
                    + login_params.username
                    + " login to clickzetta failed, error:"
                    + api_response.text
                )
            result = api_response.text
            try:
                result_dict = json.loads(result)
            except Exception:
                logging.error(f"login error:{result}")
                raise Exception(f"login error:{result}")
            if result_dict["code"] != 0:
                raise requests.exceptions.RequestException(
                    "user:"
                    + login_params.username
                    + " login to clickzetta failed, error:"
                    + result_dict["message"]
                )
            if result_dict["data"]["token"] is None:
                raise requests.exceptions.RequestException(
                    "user:"
                    + login_params.username
                    + " login to clickzetta  failed, error: token is None"
                )
            else:
                token = result_dict["data"]["token"]
                return token
        except requests.exceptions.RequestException:
            raise

    def create_bulkload_stream(self, schema_name: str, table_name: str, options):
        return import_bulkload_api().create_bulkload_stream_metadata(
            self, schema_name, table_name, options
        )

    def commit_bulkload_stream(
        self,
        instance_id: int,
        workspace: str,
        schema_name: str,
        table_name: str,
        stream_id: str,
        execute_workspace: str,
        execute_vc: str,
        commit_mode,
    ):
        return import_bulkload_api().commit_bulkload_stream(
            self,
            instance_id,
            workspace,
            schema_name,
            table_name,
            stream_id,
            execute_workspace,
            execute_vc,
            commit_mode,
        )

    def get_bulkload_stream(self, schema_name: str, table_name: str, stream_id: str):
        return import_bulkload_api().get_bulkload_stream_metadata(
            self, schema_name, table_name, stream_id
        )

    def open_bulkload_stream_writer(
        self,
        instance_id: int,
        workspace: str,
        schema_name: str,
        table_name: str,
        stream_id: str,
        partition_id: int,
    ):
        return import_bulkload_api().open_bulkload_stream_writer(
            self,
            instance_id,
            workspace,
            schema_name,
            table_name,
            stream_id,
            partition_id,
        )

    def finish_bulkload_stream_writer(
        self,
        instance_id: int,
        workspace: str,
        schema_name: str,
        table_name: str,
        stream_id: str,
        partition_id: int,
        written_files: list,
        written_lengths: list,
    ):
        return import_bulkload_api().finish_bulkload_stream_writer(
            self,
            instance_id,
            workspace,
            schema_name,
            table_name,
            stream_id,
            partition_id,
            written_files,
            written_lengths,
        )

    def pre_process_sql(self, sql):
        queries = split_sql(sql)
        if len(queries) > 0:
            for query in queries[:-1]:
                self.process_use_cmd(query)
        return queries[-1] + "\n;"

    def process_use_cmd(self, sql: str):
        sql = re.sub(r"\s+", " ", sql)
        if sql.lower().startswith("use vcluster "):
            self.vcluster = sql.lower().replace("use vcluster ", "").strip()
        elif sql.lower().startswith("use schema "):
            self.schema = sql.lower().replace("use schema ", "").strip()
        elif sql.lower().startswith("use "):
            self.schema = sql.lower().replace("use ", "").strip()

    def submit_sql_job(
        self,
        token: str,
        sql: str,
        job_id: JobID,
        parameters=None,
        schema=None,
        asynchronous: bool = False,
    ) -> QueryResult:
        sql = self.pre_process_sql(sql)
        if "test plain returns" in sql or "test unicode returns" in sql:
            return QueryResult({}, self._pure_arrow_decoding, timezone_hint=self.timezone_hint)
        table = Table(self.workspace, "", self.instance, self.vcluster)
        vc = table.vcluster
        job_type = JobType.SQL_JOB
        logging.info("clickzetta connector submitting job,  id:" + job_id.id)
        job_name = "SQL_JOB"
        user_id = 0
        reqeust_mode = JobRequestMode.HYBRID
        job_config = {}
        polling_timeout = 0
        sdk_job_priority = 15
        sql_job_set_prop = {
            "cz.sql.adhoc.result.type": "embedded",
            "cz.sql.adhoc.default.format": "arrow",
            "cz.sql.job.result.file.presigned.url.enabled": "true",
            "cz.sql.job.result.file.presigned.url.ttl": "3600",
        }
        max_retries = 10
        job_timeout_ms = 0
        hints = self.hints if self.hints is not None else {}
        if parameters is not None and len(parameters) != 0:
            if "hints" in parameters.keys():
                hints = parameters["hints"]
            for key in parameters.keys():
                if "%(" + key + ")s" in sql:
                    sql = sql.replace("%(" + key + ")s", str(parameters[key]))
        if len(hints) > 0:
            for key in hints:
                if not asynchronous and key == "sdk.job.polling.timeout":
                    polling_timeout = int(hints[key])
                elif key == "sdk.job.priority":
                    sdk_job_priority = int(hints[key])
                elif key == "sdk.query.timeout.ms":
                    job_timeout_ms = int(hints[key])
                elif key == "sdk.query.max.retries":
                    max_retries = max_retries if int(hints[key]) <= 0 else int(hints[key])
                elif key == "cz.sql.timezone":
                    self.timezone_hint = hints[key]
                else:
                    sql_job_set_prop[key] = hints[key]
        """
        The `polling_timeout` cannot exceed the threshold DEFAULT_MAXIMUM_TIMEOUT, otherwise it will be reset to the 
        default, which can avoid gateway and server timeout exceptions. If it exceeds the threshold, we will 
        switch to asynchronous result retrieval, and use `job_timeout_ms` to control the asynchronous timeout.  
        """
        if not asynchronous and (0 > polling_timeout or polling_timeout > DEFAULT_MAXIMUM_TIMEOUT):
            polling_timeout = DEFAULT_MAXIMUM_TIMEOUT
        sql_config = SQLJobConfig(0, "0", "0", sql_job_set_prop)
        schema_name = ""
        if self.schema is not None:
            schema_name = self.schema
        if schema is not None:
            schema_name = schema
        sql_job = SQLJob(sql_config, table.workspace, schema_name, [sql])
        user_agent = ""
        job_desc = JobDesc(
            vc,
            job_type,
            job_id,
            job_name,
            user_id,
            reqeust_mode,
            polling_timeout,
            job_config,
            sql_job,
            job_timeout_ms,
            user_agent,
            sdk_job_priority,
        )
        job_request = JobRequest(job_desc)
        data = json.dumps(job_request.to_api_repr())
        HEADERS["instanceName"] = table.instance
        HEADERS["X-ClickZetta-Token"] = token
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug("BEGIN TO SEND REQUEST:{0} TO CZ SERVER, TIME:{1}".format(sql, str(datetime.now())))
        return execute_with_retrying(
            partial(Client._handle_submit_sql, sql=sql, job_id=job_id.id, client=self, data=data),
            partial(Client._check_result_dict, sql=sql, client=self, job_id=job_id, job_timeout_ms=job_timeout_ms,
                    asynchronous=asynchronous),
            max_tries=max_retries
        )

    @staticmethod
    def sts_token_error(result_set: Dict):
        if "data" not in result_set and "location" in result_set:
            location = result_set["location"]
            if "fileSystem" in location and location["fileSystem"] == FileSystemType.GCS:
                return "sts_token" not in location or location["sts_token"] == ""
            else:
                return ("sts_ak_id" not in location or location["sts_ak_id"] == "") or (
                        "sts_ak_secret" not in location or location["sts_ak_secret"] == "")
        return False

    @staticmethod
    def _handle_submit_sql(sql, job_id: str, client, data, tried) -> dict:
        try:
            resp = client.session.post(client.service + "/lh/submitJob", data=data, headers=HEADERS)
            if resp is None:
                return {}
            resp.encoding = "utf-8"
            result = resp.text
        except Exception as e:
            logging.warning(
                f"Submit job throw Exception, {job_id} tried {tried}, got exception: {e}, "
                f"{e.msg}" if hasattr(e, "msg") else ""
            )
            raise e
        try:
            result_dict = json.loads(result)
        except Exception:
            logging.error(f"Job result parse failed, {job_id} tried {tried}, exception: {result}")
            raise Exception(f"Job result parse failed, {job_id} tried {tried}, exception: {result}")
        if not resp.ok:
            raise requests.exceptions.RequestException(
                f"submit sql job failed:{str(resp.status_code)} {resp.text}. sql:{sql}"
            )
        return result_dict

    @staticmethod
    def _check_result_dict(sql: str, client, job_id: JobID, job_timeout_ms, asynchronous, context: BaseExecuteContext,
                           tried, exception=None, **kwargs) -> bool:
        if exception is not None:
            msg = str(exception)
            if "NumberFormatException" in msg or "JSONDecodeError" in msg or "Illegal authorization" in msg:
                raise exception
            elif client.should_resubmit(job_id.id, tried):
                return False
            else:
                raise exception
        result = context.result
        if not result or "status" not in result:
            if client.should_resubmit(job_id.id, tried):
                return False
            else:
                raise Exception(
                    "Execute sql job:{0} failed, http response job status is not exist.{1}"
                    .format(str(job_id.id), (str(result) or ""))
                )
        elif Client.sts_token_error(result):
            raise Exception("Sts token is not generated")
        elif "errorCode" in result["status"] and result["status"]["errorCode"] != '':
            if (
                    result["status"]["errorCode"] == JOB_STATUS_UNKNOWN or
                    result["status"]["errorCode"] == JOB_NOT_SUBMITTED
            ):
                if client.should_resubmit(job_id.id, tried):
                    return False
                else:
                    raise Exception(
                        f"Job status is unknown, job_id:{job_id.id}, tried {tried} times"
                    )
            elif result["status"]["errorCode"] == JOB_ALREADY_EXIST:
                # Return True and will get the result in the next step
                pass
            elif result["status"]["errorCode"] == JOB_TIME_OUT_KILLED:
                raise Exception(
                    "submit sql job:{0} timeout after {1} ms. killed by lakehouse"
                    .format(str(job_id.id), str(job_timeout_ms))
                )
            # When the error code is CZLH-57015, jobid needs to be generated to resubmit the job
            elif result["status"]["errorCode"] == JOB_NEED_RE_EXECUTE:
                if client.should_resubmit(job_id.id, tried):
                    return False
                else:
                    raise Exception(
                        f"Job need re-execute, job_id:{job_id.id}, origin sql:{sql}, error:"
                        f"{result['status']['errorCode']}"
                    )
            else:
                error_msg = result["status"]["errorMessage"] if "errorMessage" in result["status"] else ""
                success_msg = result["status"]["message"] if "message" in result["status"] else ""
                state = result["status"]["state"]
                msg = state + " " + (error_msg if error_msg != "" else success_msg)
                raise Exception(
                    f"submit sql job:{job_id.id} failed, origin sql:{sql}, error:{result['status']['errorCode']} {msg}"
                )
        try:
            context.result = client.retry_get_result(
                result, job_id, job_timeout_ms, asynchronous, sql
            )
        except ClickzettaJobNotExistsException as e:
            if client.should_resubmit(job_id.id, 1):
                return False
            else:
                raise e
        return True

    def process_volume_sql(
            self, token: str, sql: str, query_result: QueryResult
    ) -> QueryResult:
        upper_sql = sql.strip().upper()
        outcome = query_result.data.read()
        if len(outcome) != 1:
            raise Exception(f"get volume sql failed, with result: {outcome}")
        outcome_obj = json.loads(outcome[0][0])
        if outcome_obj["status"] == "FAILED":
            raise Exception(
                f"{outcome_obj['request']['command']} volume failed: {outcome_obj['error']}"
            )
        if upper_sql.startswith("GET"):
            query_result = self.gen_volume_result(outcome_obj)
            if outcome_obj["status"] == "CONTINUE" and outcome_obj["nextMarker"] != "":
                sql = "set cz.sql.volume.file.transfer.next.marker=nextMarker;" + sql
                job_id = JobID(
                    self._format_job_id(), self.workspace, DEFAULT_INSTANCE_ID
                )
                next_result = self.submit_sql_job(token=token, sql=sql, job_id=job_id)
                query_result.data = self._merge_get_query_result(query_result.data.data, next_result.data.data,
                                                            query_result.schema)
            return query_result
        elif upper_sql.startswith("PUT"):
            if outcome_obj["status"] == "CONTINUE":
                sql = self._gen_new_put_sql(outcome_obj)
                job_id = JobID(
                    self._format_job_id(), self.workspace, DEFAULT_INSTANCE_ID
                )
                return self.submit_sql_job(token=token, sql=sql, job_id=job_id)
            else:
                return self.gen_volume_result(outcome_obj)

    def gen_volume_result(self, outcome: Any):
        result_list = []
        if outcome["request"]["command"].upper() == "GET":
            volume_files = self.get_volume_files(outcome)
            for i in range(len(volume_files)):
                response = requests.get(
                    outcome["ticket"]["presignedUrls"][i], stream=True
                )
                local_path = os.path.join(
                    normalize_file_path(outcome["request"]["localPaths"][0]), volume_files[i]
                )
                if not os.path.exists(os.path.dirname(local_path)):
                    os.makedirs(os.path.dirname(local_path))
                with open(local_path, "wb") as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                logging.info(
                    f"get volume success, volume_path:{volume_files[i]}, local_path:{local_path}"
                )
                res = [volume_files[i], local_path, os.path.getsize(local_path)]
                result_list.append(res)
        elif outcome["request"]["command"].upper() == "PUT":
            if outcome["status"] == "SUCCESS":
                for i in range(len(outcome["ticket"]["presignedUrls"])):
                    local_path = normalize_file_path(outcome["request"]["localPaths"][i])
                    if not os.path.exists(local_path):
                        raise Exception(
                            f"put volume failed, local_path:{local_path} not exists"
                        )
                    with open(local_path, "rb") as f:
                        requests.put(
                            outcome["ticket"]["presignedUrls"][i],
                            data=f.read(),
                            headers={},
                        )
                    logging.info(f"put volume success, local_path:{local_path}")
                    volume_file = ""
                    if "file" in outcome["request"]:
                        volume_file = outcome["request"]["file"]
                    else:
                        if "subdirectory" in outcome["request"]:
                            path = outcome["request"]["subdirectory"]
                            path = path if path[-1] == "/" else path + "/"
                            volume_file = path + os.path.basename(local_path)
                        else:
                            volume_file = os.path.basename(local_path)
                    res = [local_path, volume_file, os.path.getsize(local_path)]
                    result_list.append(res)
        query_result = QueryResult({}, self._pure_arrow_decoding, timezone_hint=self.timezone_hint)
        query_result.data = QueryData(
            data=result_list,
            data_type=QueryDataType.Memory,
            schema=query_result.schema,
            pure_arrow_decoding=self._pure_arrow_decoding,
        )
        return query_result

    def get_volume_files(self, outcome: Any):
        volume_files = []
        if "file" in outcome["request"]:
            volume_files.append(
                os.path.basename(os.path.abspath(outcome["request"]["file"]))
            )
        else:
            for url in outcome["ticket"]["presignedUrls"]:
                parsed_url = urlparse(unquote(url))
                path_parts = parsed_url.path.split("/")
                volume_files.append(path_parts[-1])
        return volume_files

    def __check_not_submitted(self, job_id: str) -> bool:
        try:
            get_job_result_response = self.get_job_result(job_id)
            return get_job_result_response is None
        except Exception as e:
            logging.warning(f"get job result failed! e:{str(e)}")
            return True

    def should_resubmit(self, job_id: str, tried) -> bool:
        if self.__check_not_submitted(job_id):
            try:
                time.sleep(0.5 * tried)
                return True
            except InterruptedError:
                logger.warning(
                    f"Receive Interrupt but Job {job_id} is still running..."
                )
        return False

    def close(self):
        pass

    def cancel_job(self, job_id: JobID, headers=HEADERS):
        account = ClickZettaAccount(0)
        cancel_job_request = CancelJobRequest(
            account, job_id, "", False
        )
        path = "/lh/cancelJob"
        data = json.dumps(cancel_job_request.to_api_repr())
        try:
            self.session.post(self.service + path, data=data, headers=headers)
        except Exception as e:
            logging.error("clickzeta connector cancel job error:{}".format(e))

    def _check_job_timeout_with_cancel(
            self, job_timeout_ms, sql_job_start_time: datetime, job_id
    ):
        if job_timeout_ms > 0:
            time_range: timedelta = datetime.now() - sql_job_start_time
            if time_range.seconds > job_timeout_ms / 1000:
                self.cancel_job(job_id)
                return True
        return False

    def get_job_profile(self, job_id: str):
        result_dict = self._get_job(job_id, JobRequestType.PROFILE)
        return result_dict

    def get_job_result(self, job_id: str) -> dict:
        result_dict = self._get_job(job_id, JobRequestType.RESULT)
        return result_dict

    def get_job_progress(self, job_id: str):
        result_dict = self._get_job(job_id, JobRequestType.PROGRESS)
        return result_dict

    def get_job_summary(self, job_id: str):
        result_dict = self._get_job(job_id, JobRequestType.SUMMARY)
        return result_dict

    def get_job_plan(self, job_id: str):
        result_dict = self._get_job(job_id, JobRequestType.PLAN)
        return result_dict

    def _get_job(self, job_id: str, type: str):
        HEADERS["instanceName"] = self.instance
        HEADERS["X-ClickZetta-Token"] = self.token
        id = JobID(job_id, self.workspace, DEFAULT_INSTANCE_ID)
        account = ClickZettaAccount(0)
        get_job_request = GetJobRequest(account, id, 0, "")
        path = "/lh/getJob"
        try:
            api_request = APIGetJobRequest(get_job_request, "", type)
            data = json.dumps(api_request.to_api_repr())
            api_response = self.session.post(
                self.service + path, data=data, headers=HEADERS
            )
            result = api_response.text
            result_dict = json.loads(result)
            if int(result_dict["code"]) != 200:
                raise requests.exceptions.RequestException(
                    f"Get job:{id.id} {type} failed:{result_dict}"
                )
            return result_dict
        except AttributeError as e:
            raise requests.exceptions.RequestException(
                f"Get job:{id.id} {type} failed:{e}, Only supports：result/progress/summary/plan/profile."
            )
        except Exception as e:
            raise Exception(f"Get job:{id.id} {type} failed:{e}")

    @staticmethod
    def verify_result_dict_finished(result_dict, sql=None):
        if result_dict and "status" in result_dict:
            if "state" in result_dict["status"]:
                error_msg = result_dict["status"]["errorMessage"] if "errorMessage" in result_dict["status"] else ""
                success_msg = result_dict["status"]["message"] if "message" in result_dict["status"] else ""
                state = result_dict["status"]["state"]
                msg = state + " " + (error_msg if error_msg != "" else success_msg)
                if "errorCode" in result_dict["status"] and len(result_dict["status"]["errorCode"]) > 0:
                    error_code = result_dict["status"]["errorCode"]
                    # Return False and will retry to get the result
                    if error_code == JOB_ALREADY_EXIST:
                        return False
                    msg = f"Execute sql job failed, sql:{sql}, error: {msg or error_code}"
                    logger.error(msg)
                    if error_code == JOB_NOT_EXIST:
                        # It will raise exception and resubmit job in the next step
                        raise ClickzettaJobNotExistsException(
                            msg, error_code=error_code
                        )
                    else:
                        raise Exception(msg)
                if state == "SUCCEED":
                    return True
                elif state == "FAILED":
                    if msg.__contains__(JOB_ALREADY_EXIST):
                        return False
                    else:
                        raise Exception(
                            f"Execute sql job failed, sql:{sql}, error: {msg}"
                        )
                elif state == "CANCELLED" or state == "CANCELLING":
                    raise Exception(
                        f"Job is cancelled/cancelling. {msg}"
                    )
                elif state == "QUEUEING" or state == "SETUP" or state == "RUNNING" or state == "RESUMING_CLUSTER":
                    if "resultSet" in result_dict:
                        if "data" in result_dict["resultSet"]:
                            if "data" in result_dict["resultSet"]["data"]:
                                return True
                        elif "location" in result_dict["resultSet"]:
                            return True
                else:
                    raise Exception(
                        f"Execute sql job failed, sql:{sql}, error: {msg}"
                    )
        return False

    def retry_get_result(self, result_dict, job_id: JobID, job_timeout_ms=0, asynchronous=False, sql=None) -> QueryResult:
        if not result_dict or "status" not in result_dict or "state" not in result_dict["status"]:
            raise Exception(
                "Execute sql job:{0} failed, http response job status is not exist.".format(str(job_id.id))
            )
        # The first round of result verification, if the job is finished, return the result directly
        already_finished = Client.verify_result_dict_finished(result_dict, sql)
        if already_finished and asynchronous:
            return QueryResult(result_dict, self._pure_arrow_decoding, timezone_hint=self.timezone_hint)
        elif asynchronous:
            return QueryResult({}, self._pure_arrow_decoding, timezone_hint=self.timezone_hint)

        begin_time = datetime.now()
        sleep_time_ms = 50

        def _get_result_with_timeout(*args, **kwargs):
            if not self._check_job_timeout_with_cancel(job_timeout_ms, begin_time, job_id):
                return self.get_job_result(job_id.id)
            else:
                error_msg = (f"clickzetta sql job:{str(job_id.id)} timeout after {str(job_timeout_ms / 1000)} "
                             f"seconds. killed by sdk.")
                logging.error(error_msg)
                raise Exception(error_msg)

        def _handle_result_check(sql, context, tried, exception=None, **kwargs):
            if exception:
                logging.warning("_handle_result_check warn: " + str(exception))
                raise exception
            result = context.result
            if not Client.verify_result_dict_finished(result, sql):
                # Retry after `sleep_time_ms` seconds
                nonlocal sleep_time_ms
                second = sleep_time_ms / 1000.0
                time.sleep(second)
                # Randomly generate a waiting time from 5s to 30s, and avoid the latency caused by long waiting
                # time by shuffling the time series.
                if sleep_time_ms * 1.5 <= 30000:
                    sleep_time_ms = sleep_time_ms * 1.5
                else:
                    sleep_time_ms = random.randint(5000, 30000)
                    if logger.isEnabledFor(logging.DEBUG):
                        logging.debug(
                            "Get async sql job:{0} result pending, retry after {1} seconds, tried:{2}, time cost:{3}, next"
                            " sleep time:{4}".format(str(job_id.id), str(second), str(tried),
                                                     str(begin_time - datetime.now()),
                                                     str(sleep_time_ms))
                        )
                return False
            else:
                return True

        if not already_finished:
            # max_tries=-1 means retrying until the job is finished
            result_dict = execute_with_retrying(
                _get_result_with_timeout,
                partial(_handle_result_check, sql),
                lambda result, exception: self.cancel_job(job_id),
                max_tries=-1
            )
        return self._process_hint_job(sql, self.token,
                                      QueryResult(result_dict, self._pure_arrow_decoding,
                                                  timezone_hint=self.timezone_hint))

    def _process_hint_job(self, sql, token, query_result: QueryResult):
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(
                "GET RESPONSE FROM CZ SERVER FOR REQUEST:{0} TIME:{1}".format(sql, str(datetime.now()))
            )
        if sql.lstrip().upper().startswith(
                "PUT "
        ) or sql.lstrip().upper().startswith("GET "):
            check_volume_result = self.process_volume_sql(token, sql, query_result)
            return check_volume_result
        return query_result

    def _format_job_id(self):
        unique_id = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        format_unique_id = unique_id.replace("-", "").replace(":", "").replace(
            ".", ""
        ).replace(" ", "") + str(random.randint(10000, 99999))
        return format_unique_id

    def generate_job_id(self):
        return self._format_job_id()

    def get_table_names(self, schema: str):
        job_id = JobID(self._format_job_id(), self.workspace, DEFAULT_INSTANCE_ID)
        query_result = self.submit_sql_job(
            token=self.token, sql="show tables;", schema=schema, job_id=job_id
        )
        query_data = query_result.data.read()
        table_names = []
        for entry in query_data:
            table_names.append(entry[1])

        return table_names

    def get_schemas(self):
        job_id = JobID(self._format_job_id(), self.workspace, DEFAULT_INSTANCE_ID)
        query_result = self.submit_sql_job(
            token=self.token, sql="show schemas;", job_id=job_id
        )
        query_data = query_result.data.read()
        schema_names = []
        for entry in query_data:
            schema_names.append(entry[0])

        return schema_names

    def get_columns(self, table_name: str, schema: str):
        job_id = JobID(self._format_job_id(), self.workspace, DEFAULT_INSTANCE_ID)
        if "." in table_name:
            schema = table_name.split(".")[0]
            table_name = table_name.split(".")[1]
        query_result = self.submit_sql_job(
            token=self.token,
            sql="select * from " + schema + "." + table_name + " limit 1;",
            job_id=job_id,
        )
        schema = query_result.schema

        return schema

    def has_table(self, full_table_name: str):
        job_id = JobID(self._format_job_id(), self.workspace, DEFAULT_INSTANCE_ID)
        try:
            query_result = self.submit_sql_job(
                token=self.token,
                sql="show create table " + full_table_name + ";",
                job_id=job_id,
            )
        except Exception as e:
            return False
        if query_result.state != "FAILED":
            return True
        else:
            return False

    def _merge_get_query_result(self, res1: List, res2: List, schema=None):
        new_data = res1 + res2
        data = QueryData(
            data=new_data,
            data_type=QueryDataType.Memory,
            schema=schema,
            pure_arrow_decoding=self._pure_arrow_decoding,
        )
        return data

    def _gen_new_put_sql(self, outcome_obj):
        prefix = ""
        option_part = ""
        for option in outcome_obj["request"]["options"]:
            if option["name"].upper() == "SOURCE_PREFIX":
                prefix = option["value"]
            option_part += " " + option["name"] + " = " + option["value"]
        requested_paths = outcome_obj["request"]["localPaths"]
        resolved_paths = []
        for p in requested_paths:
            resolved_paths += resolve_local_path(p)
        if len(resolved_paths) == 0:
            raise Exception("No local file to put into volume")
        sql = "PUT "
        sql += ", ".join(f"'{p}'" for p in resolved_paths)
        sql += " TO " + outcome_obj["request"]["volumeIdentifier"]
        if "subdirectory" in outcome_obj["request"]:
            sql += " SUBDIRECTORY '" + outcome_obj["request"]["subdirectory"] + "'"
        elif "file" in outcome_obj["request"]:
            sql += " FILE '" + outcome_obj["request"]["file"] + "'"
        sql += option_part
        sql += ";"
        return sql

    @property
    def unique_key(self):
        return self.username + "?" + self.instance

    @property
    def token(self) -> str:
        if self.magic_token is not None:
            return self.magic_token
        if _globals["user_token_dict"].__contains__(self.unique_key):
            if not self._token or self.will_soon_expire():
                now = int(round(time.time() * 1000))
                new_token = self.log_in_cz(self.username, self.password, self.instance)
                _globals["user_token_dict"][self.unique_key] = new_token
                _globals["user_token_time_dict"][self.unique_key] = now
                self.token = new_token
            else:
                self.token = _globals["user_token_dict"][self.unique_key]
        else:
            now = int(round(time.time() * 1000))
            new_token = self.log_in_cz(self.username, self.password, self.instance)
            _globals["user_token_dict"][self.unique_key] = new_token
            _globals["user_token_time_dict"][self.unique_key] = now
            self.token = new_token
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def refresh_token(self):
        return self.token

    def will_soon_expire(self) -> bool:
        if self.token_expire_time_ms == 0:
            return False
        expire_time = self.token_expire_time_ms * DEFAULT_EXPIRED_FACTOR
        now = int(round(time.time() * 1000))
        return now - _globals["user_token_time_dict"][self.unique_key] > expire_time

    def validate(self):
        if not self.service:
            raise ValueError("service must be specified")
        if not self.instance:
            raise ValueError("instance must be specified")
        if not self.workspace:
            raise ValueError("workspace must be specified")
        if not self.vcluster:
            raise ValueError("vcluster must be specified")
        if not ((self.username and self.password) or self.magic_token):
            raise ValueError("username and password or token must be specified")
        if not self.schema:
            self.schema = "public"


def _add_server_timeout_header(headers: Optional[Dict[str, str]], kwargs):
    timeout = kwargs.get("timeout")
    if timeout is not None:
        if headers is None:
            headers = {}
        headers[TIMEOUT_HEADER] = str(timeout)

    if headers:
        kwargs["headers"] = headers

    return kwargs
