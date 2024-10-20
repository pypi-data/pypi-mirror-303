import argparse
import pathlib
import dataclasses
import pathlib
import typing

from PIL import Image

from . import __version__
from . import types

DEFAULT_OUTPUT_PATH = pathlib.Path('output')

@dataclasses.dataclass
class Options:
    input_file: pathlib.Path | None = None
    output_path: pathlib.Path = DEFAULT_OUTPUT_PATH
    image: types.ImageParameters = \
        dataclasses.field(default_factory=types.ImageParameters)
    text: types.TextParameters = \
        dataclasses.field(default_factory=types.TextParameters)
    watermark: types.WatermarkParameters = \
        dataclasses.field(default_factory=types.WatermarkParameters)
    no_database: bool = False

    def __post_init__(self) -> None:
        self._initialized = True

    def __setattr__(self, name: str, value: typing.Any) -> None:
        if not hasattr(self, '_initialized') or hasattr(self, name):
            super().__setattr__(name, value)
            return

        _set_attr_with_prefix("image_", self.image, name, value)
        _set_attr_with_prefix("text_font_", self.text.font, name, value)
        _set_attr_with_prefix("text_rectangle_", self.text.rectangle, name, value)
        _set_attr_with_prefix("text_", self.text, name, value)
        _set_attr_with_prefix("watermark_", self.watermark, name, value)

class HelpFormatter(
    argparse.RawTextHelpFormatter,
    argparse.ArgumentDefaultsHelpFormatter,
):
    pass

def parse_options() -> Options:
    parser = argparse.ArgumentParser(
        prog=__package__.replace('_', '-'),
        formatter_class=HelpFormatter,
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        help='show the version message and exit',
        version='White Generator, v{:s}\n'.format(__version__) \
            + 'Copyright (C) 2017, 2024 thewizardplusplus',
    )
    parser.add_argument(
        '-i',
        '--input-file',
        type=pathlib.Path,
        required=True,
        help='the path to the file with notes',
    )
    parser.add_argument(
        '-o',
        '--output-path',
        type=pathlib.Path,
        default=DEFAULT_OUTPUT_PATH,
        help='the path for generated images',
    )
    parser.add_argument(
        '-l',
        '--text-rectangle-left',
        type=int,
        default=types.DEFAULT_RECTANGLE_LEFT,
        help='the left text position',
    )
    parser.add_argument(
        '-t',
        '--text-rectangle-top',
        type=int,
        default=types.DEFAULT_RECTANGLE_TOP,
        help='the top text position',
    )
    parser.add_argument(
        '-R',
        '--text-rectangle-right',
        type=int,
        default=types.DEFAULT_RECTANGLE_RIGHT,
        help='the horizontal text limit ' \
            + '(if the value is negative, the image width is added to it)',
    )
    parser.add_argument(
        '-B',
        '--text-rectangle-bottom',
        type=int,
        default=types.DEFAULT_RECTANGLE_BOTTOM,
        help='the vertical text limit ' \
            + '(if the value is negative, the image height is added to it)',
    )
    parser.add_argument(
        '-a',
        '--text-horizontal-align',
        type=_parse_horizontal_align,
        choices=tuple(types.HorizontalAlign),
        default=types.DEFAULT_TEXT_HORIZONTAL_ALIGN,
        help='the text horizontal alignment',
    )
    parser.add_argument(
        '-A',
        '--text-vertical-align',
        type=_parse_vertical_align,
        choices=tuple(types.VerticalAlign),
        default=types.DEFAULT_TEXT_VERTICAL_ALIGN,
        help='the text vertical alignment',
    )
    parser.add_argument(
        '-W',
        '--image-width',
        type=int,
        default=types.DEFAULT_IMAGE_WIDTH,
        help='the image width',
    )
    parser.add_argument(
        '-H',
        '--image-height',
        type=int,
        default=types.DEFAULT_IMAGE_HEIGHT,
        help='the image height',
    )
    parser.add_argument(
        '-b',
        '--image-background-color',
        type=types.Color.parse,
        default=types.DEFAULT_IMAGE_BACKGROUND_COLOR,
        help='the image background color',
    )
    parser.add_argument(
        '-I',
        '--image-background-image',
        type=pathlib.Path,
        help='the path to the background image',
    )
    parser.add_argument(
        '-F',
        '--image-resizing-filter',
        type=_parse_image_resampling,
        choices=tuple(Image.Resampling),
        default=types.DEFAULT_IMAGE_RESIZING_FILTER,
        help='the resizing filter for the background image',
    )
    parser.add_argument(
        '-f',
        '--text-font-file',
        type=pathlib.Path,
        help="the path to the font file (if none, the Pillow library's default font is used)",
    )
    parser.add_argument(
        '-s',
        '--text-font-size',
        type=int,
        default=types.DEFAULT_FONT_SIZE,
        help='the font size',
    )
    parser.add_argument(
        '-c',
        '--text-font-color',
        type=types.Color.parse,
        default=types.DEFAULT_FONT_COLOR,
        help='the font color',
    )
    parser.add_argument(
        '-w',
        '--watermark-text',
        help='the watermark text',
    )
    parser.add_argument(
        '-S',
        '--watermark-size',
        type=int,
        default=types.DEFAULT_WATERMARK_SIZE,
        help='the watermark font size',
    )
    parser.add_argument(
        '-C',
        '--watermark-color',
        type=types.Color.parse,
        default=types.DEFAULT_WATERMARK_COLOR,
        help='the watermark font color',
    )
    parser.add_argument(
        "--no-database",
        action="store_true",
        help="don't filter notes by database",
    )
    parser.add_argument(
        "--no-resizing",
        action="store_true",
        dest="image_no_resizing",
        help="don't resize the background image",
    )

    return parser.parse_args(namespace=Options())

def _parse_horizontal_align(text: str) -> types.HorizontalAlign:
    try:
        return types.HorizontalAlign[text.upper()]
    except KeyError as exception:
        raise argparse.ArgumentTypeError(f"unknown horizontal align: {exception}") from exception

def _parse_vertical_align(text: str) -> types.VerticalAlign:
    try:
        return types.VerticalAlign[text.upper()]
    except KeyError as exception:
        raise argparse.ArgumentTypeError(f"unknown vertical align: {exception}") from exception

def _parse_image_resampling(text: str) -> Image.Resampling:
    try:
        return Image.Resampling[text.upper()]
    except KeyError as exception:
        raise argparse.ArgumentTypeError(f"unknown image resampling: {exception}") from exception

def _set_attr_with_prefix(prefix: str, obj: object, name: str, value: typing.Any) -> None:
    if name.startswith(prefix):
        setattr(obj, name.removeprefix(prefix), value)
