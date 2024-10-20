from __future__ import annotations
import dataclasses
import pathlib
import enum
import typing
import collections.abc

from PIL import Image
from PIL import ImageColor

_ColorValues: typing.TypeAlias = collections.abc.ValuesView[int | None]

@dataclasses.dataclass
class Color:
    red: int
    green: int
    blue: int
    alpha: int | None = None

    @staticmethod
    def parse(text: str) -> Color:
        (red, green, blue, *rest_values) = ImageColor.getrgb(text)
        return Color(red, green, blue, rest_values[0] if rest_values else None)

    def __iter__(self) -> typing.Iterator[int]:
        values: _ColorValues = dataclasses.asdict(self).values()
        yield from (value for value in values if value is not None)

    def __str__(self) -> str:
        values = tuple(self)
        assert len(values) == 3 or len(values) == 4

        return f'rgb{"a" if len(values) == 4 else ""}{values}'

DEFAULT_IMAGE_WIDTH = 640
DEFAULT_IMAGE_HEIGHT = 480
DEFAULT_IMAGE_BACKGROUND_COLOR = Color.parse('rgb(255, 255, 255)')
DEFAULT_IMAGE_RESIZING_FILTER = Image.Resampling.LANCZOS

DEFAULT_FONT_SIZE = 25
DEFAULT_FONT_COLOR = Color.parse('rgb(0, 0, 0)')

DEFAULT_RECTANGLE_LEFT = 0
DEFAULT_RECTANGLE_TOP = 0
DEFAULT_RECTANGLE_RIGHT = -1
DEFAULT_RECTANGLE_BOTTOM = -1

DEFAULT_WATERMARK_SIZE = 12
DEFAULT_WATERMARK_COLOR = Color.parse('rgb(128, 128, 128)')

@dataclasses.dataclass
class ImageParameters:
    width: int = DEFAULT_IMAGE_WIDTH
    height: int = DEFAULT_IMAGE_HEIGHT
    background_color: Color = DEFAULT_IMAGE_BACKGROUND_COLOR
    background_image: pathlib.Path | None = None
    resizing_filter: Image.Resampling = DEFAULT_IMAGE_RESIZING_FILTER
    no_resizing: bool = False

    @property
    def size(self) -> tuple[int, int]:
        return (self.width, self.height)

@dataclasses.dataclass
class FontParameters:
    file: pathlib.Path | None = None
    size: int = DEFAULT_FONT_SIZE
    color: Color = DEFAULT_FONT_COLOR

@dataclasses.dataclass
class Rectangle:
    left: int = DEFAULT_RECTANGLE_LEFT
    top: int = DEFAULT_RECTANGLE_TOP
    right: int = DEFAULT_RECTANGLE_RIGHT
    bottom: int = DEFAULT_RECTANGLE_BOTTOM

# TODO: replace with `enum.StrEnum` after upgrading to Python 3.11
class HorizontalAlign(str, enum.Enum):
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'

# TODO: replace with `enum.StrEnum` after upgrading to Python 3.11
class VerticalAlign(str, enum.Enum):
    TOP = 'top'
    CENTER = 'center'
    BOTTOM = 'bottom'

DEFAULT_TEXT_HORIZONTAL_ALIGN = HorizontalAlign.CENTER
DEFAULT_TEXT_VERTICAL_ALIGN = VerticalAlign.CENTER

@dataclasses.dataclass
class TextParameters:
    font: FontParameters = dataclasses.field(default_factory=FontParameters)
    rectangle: Rectangle = dataclasses.field(default_factory=Rectangle)
    horizontal_align: HorizontalAlign = DEFAULT_TEXT_HORIZONTAL_ALIGN
    vertical_align: VerticalAlign = DEFAULT_TEXT_VERTICAL_ALIGN

@dataclasses.dataclass
class WatermarkParameters:
    text: str | None = None
    size: int = DEFAULT_WATERMARK_SIZE
    color: Color = DEFAULT_WATERMARK_COLOR
