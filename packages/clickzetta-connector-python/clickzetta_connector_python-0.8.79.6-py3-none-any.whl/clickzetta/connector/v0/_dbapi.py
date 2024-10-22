from typing import Any, Dict, NamedTuple, Optional

from clickzetta.connector.v0._sql import (
    BaseCharType,
    DecimalType,
    SqlType,
    proto_to_sql_type,
)
from clickzetta.connector.v0.types import STRING


class ColumnDescription(NamedTuple):
    name: str
    type_code: str
    display_size: Optional[int]
    internal_size: Optional[int]
    precision: Optional[int]
    scale: Optional[int]
    null_ok: bool


class Field(NamedTuple):
    name: str
    field_type: str
    precision: Optional[int]
    scale: Optional[int]
    length: Optional[int]
    nullable: bool
    sql_type: SqlType

    def to_column_description(self) -> ColumnDescription:
        return ColumnDescription(
            self.name,
            self.field_type,
            None,
            self.length,
            self.precision,
            self.scale,
            self.nullable,
        )


MESSAGE_FIELD = Field("RESULT_MESSAGE", "STRING", None, None, None, False, STRING)


def proto_to_field(data: Dict) -> Field:
    name = data["name"]
    sql_type = proto_to_sql_type(data["type"])
    return create_field(name, sql_type)


def create_field(name: str, sql_type: SqlType) -> Field:
    return Field(
        name,
        sql_type.category,
        sql_type.precision if isinstance(sql_type, DecimalType) else None,
        sql_type.scale if isinstance(sql_type, DecimalType) else None,
        sql_type.length if isinstance(sql_type, BaseCharType) else None,
        sql_type.nullable,
        sql_type,
    )
