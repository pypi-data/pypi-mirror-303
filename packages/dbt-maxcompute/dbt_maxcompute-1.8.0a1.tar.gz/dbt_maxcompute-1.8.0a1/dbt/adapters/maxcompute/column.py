from dataclasses import dataclass
from typing import TypeVar, Any

from dbt.adapters.base.column import Column
from odps.models.table import TableSchema
from odps.types import Decimal, Varchar

_PARENT_DATA_TYPE_KEY = "__parent_data_type"

Self = TypeVar("Self", bound="MaxComputeColumn")


@dataclass
class MaxComputeColumn(Column):
    table_column: TableSchema.TableColumn = None
    comment: str = None

    TYPE_LABELS = {
        "TEXT": "STRING",
    }

    @property
    def quoted(self):
        return "`{}`".format(self.column)

    def literal(self, value):
        return "cast({} as {})".format(value, self.dtype)

    @property
    def data_type(self) -> str:
        return self.dtype

    @classmethod
    def numeric_type(cls, dtype: str, precision: Any, scale: Any) -> str:
        # MaxCompute makes life much harder if precision + scale are specified
        # even if they're fed in here, just return the data type by itself
        return dtype

    def is_string(self) -> bool:
        return self.dtype.lower() == "string"

    def can_expand_to(self: Self, other_column: Self) -> bool:  # type: ignore
        """returns True if both columns are strings"""
        return self.is_string() and other_column.is_string()

    def __repr__(self) -> str:
        return "<MaxComputeColumn {} ({})>".format(self.name, self.data_type)

    @classmethod
    def from_odps_column(cls, column: TableSchema.TableColumn):
        char_size = None
        numeric_precision = None
        numeric_scale = None

        if isinstance(column.type, Decimal):
            numeric_precision = column.type.precision
            numeric_scale = column.type.scale
        elif isinstance(column.type, Varchar):
            char_size = column.type.size_limit

        return cls(
            column=column.name,
            dtype=column.type.name,
            char_size=char_size,
            numeric_precision=numeric_precision,
            numeric_scale=numeric_scale,
            table_column=column,
            comment=column.comment,
        )
