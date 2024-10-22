from pydantic import BaseModel, field_serializer, model_validator, PositiveInt
from pydantic_extra_types.color import Color
from pydantic_core import SchemaValidator

from typing import List, Literal, Union, Optional


def check_schema(model: BaseModel) -> None:
    schema_validator = SchemaValidator(schema=model.__pydantic_core_schema__)
    schema_validator.validate_python(model.__dict__)


class FHTableEntry(BaseModel):
    value: Union[str, int, float, None]
    background_color: Optional[Color] = None
    text_color: Optional[Color] = None
    col_span: Optional[PositiveInt] = None

    @field_serializer("background_color", "text_color")
    def serialize_background_color(self, color, _info):
        return color.as_hex("Long") if color is not None else None


class FHTable(BaseModel):
    title: str
    header: List[FHTableEntry] = []
    rows: List[List[FHTableEntry]] = []

    @model_validator(mode="after")
    def rows_wrong_size(self):
        header_len = self.header_len()
        row_lens = self.rows_len()
        if header_len != 0 and len(row_lens) != 0:
            for row_len in row_lens:
                if row_len != header_len:
                    raise ValueError("row lengths do not match header")
        return self

    def header_len(self):
        length = 0
        for header in self.header:
            length += header.col_span if header.col_span is not None else 1
        return length

    def rows_len(self):
        lengths = []
        for row in self.rows:
            length = 0
            for entry in row:
                length += entry.col_span if entry.col_span is not None else 1
            lengths.append(length)
        return lengths

    def add_row(self, row: List[FHTableEntry]):
        self.rows.append(row)
        check_schema(self)

    def add_header(self, header: List[FHTableEntry]):
        self.header = header
        check_schema(self)


class FHFigure(BaseModel):
    title: str
    filename: str
    width: Optional[Union[int, float, str]] = None
    height: Optional[Union[int, float, str]] = None


class FHObject(BaseModel):
    type: Literal["table", "svg_figure"]
    data: Union[FHTable, FHFigure]


class FHJSON(BaseModel):
    data: List[FHObject] = []

    def add_table(self, table):
        self.data.append(FHObject(type="table", data=table))
        check_schema(self)

    def add_svg_figure(self, figure):
        self.data.append(FHObject(type="svg_figure", data=figure))
        check_schema(self)
