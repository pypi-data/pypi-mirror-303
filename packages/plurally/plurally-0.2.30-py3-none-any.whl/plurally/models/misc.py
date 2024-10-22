import itertools
from typing import Dict, List

from pydantic import BaseModel, field_validator


class Table(BaseModel):
    data: List[Dict[str, str]]

    @field_validator("data", mode="before")
    def check_data(cls, value):
        # make sure everything is a string
        columns = set()
        value, other = itertools.tee(value)
        for row in value:
            for key, val in row.items():
                if not isinstance(val, str):
                    row[key] = str(val)
            columns.add(tuple(row))

        if len(columns) > 1:
            raise ValueError(f"All rows must have the same columns, got {columns}")

        return other

    def columns(self):
        return list(self.data[0]) if self.data else []

    def is_empty(self):
        return not bool(self.data)

    class Config:
        json_schema_extra = {
            "type-friendly": "Table",
            "hidden-for-example": True,
        }
