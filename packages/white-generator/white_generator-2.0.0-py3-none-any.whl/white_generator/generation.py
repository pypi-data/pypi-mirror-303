import pathlib
import dataclasses

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from . import text
from . import types

def generate_image(
    note: str,
    image_parameters: types.ImageParameters,
    text_parameters: types.TextParameters,
    watermark_parameters: types.WatermarkParameters,
) -> Image.Image:
    updated_image_parameters = image_parameters
    if image_parameters.background_image is None:
        image = Image.new(
            'RGB',
            image_parameters.size,
            tuple(image_parameters.background_color),
        )
    else:
        image = Image.open(image_parameters.background_image)

        if not image_parameters.no_resizing \
            and image.size != image_parameters.size:
            image = image.resize(
                image_parameters.size,
                image_parameters.resizing_filter,
            )
        else:
            (image_width, image_height) = image.size
            updated_image_parameters = dataclasses.replace(
                image_parameters,
                width=image_width,
                height=image_height,
            )

    text_font = load_font(text_parameters.font.file, text_parameters.font.size)
    updated_text_parameters = dataclasses.replace(
        text_parameters,
        rectangle=text.fit_text_rectangle(
            updated_image_parameters,
            text_parameters,
            text_font,
        ),
    )

    draw = ImageDraw.Draw(image)
    fitted_note = text.fit_text(draw, note, updated_text_parameters, text_font)
    draw.multiline_text(
        text.get_text_position(draw, fitted_note, updated_text_parameters, text_font),
        fitted_note,
        align=updated_text_parameters.horizontal_align,
        font=text_font,
        fill=tuple(updated_text_parameters.font.color),
    )

    if watermark_parameters.text is not None:
        watermark_font = load_font(
            updated_text_parameters.font.file,
            watermark_parameters.size,
        )
        draw.multiline_text(
            text.get_watermark_position(
                draw,
                watermark_parameters.text,
                updated_image_parameters,
                watermark_font,
            ),
            watermark_parameters.text,
            font=watermark_font,
            fill=tuple(watermark_parameters.color),
        )

    return image

def load_font(
    font_file: pathlib.Path | None,
    font_size: int,
) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    if font_file is None:
        return ImageFont.load_default(font_size)

    return ImageFont.truetype(font_file, font_size)
