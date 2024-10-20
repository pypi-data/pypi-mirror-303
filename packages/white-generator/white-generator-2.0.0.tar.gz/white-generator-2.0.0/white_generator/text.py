from PIL import ImageDraw
from PIL import ImageFont

from . import types

def fit_text_rectangle(
    image_parameters: types.ImageParameters,
    text_parameters: types.TextParameters,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
) -> types.Rectangle:
    text_left = _crop(text_parameters.rectangle.left, 0, image_parameters.width)
    text_top = _crop(text_parameters.rectangle.top, 0, image_parameters.height)
    text_right = _crop(
        _add_modulus_to_negative(
            text_parameters.rectangle.right,
            image_parameters.width,
        ),
        text_left,
        image_parameters.width,
    )
    text_bottom = _crop(
        _add_modulus_to_negative(
            text_parameters.rectangle.bottom,
            image_parameters.height,
        ),
        text_top,
        image_parameters.height,
    )
    font_descent = _get_font_descent(font)
    if image_parameters.height - text_bottom < font_descent:
        text_bottom = image_parameters.height - font_descent
    return types.Rectangle(text_left, text_top, text_right, text_bottom)

def fit_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    text_parameters: types.TextParameters,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
) -> str:
    if text.strip() == '':
        return text

    lines = text.split('\n')
    if len(lines) > 1:
        return '\n'.join(
            fit_text(draw, line, text_parameters, font)
            for line in lines
        )

    words = [word.strip() for word in text.split(' ') if word.strip() != '']
    fitted_text = words[0]
    rectangle_width = \
        text_parameters.rectangle.right - text_parameters.rectangle.left
    for word in words[1:]:
        extended_fitted_text = fitted_text + ' ' + word
        (text_box_left, _, text_box_right, _) \
            = draw.multiline_textbbox((0, 0), extended_fitted_text, font=font)
        text_width = text_box_right - text_box_left
        if text_width <= rectangle_width:
            fitted_text = extended_fitted_text
        else:
            fitted_text += '\n' + word

    return fitted_text

def get_text_position(
    draw: ImageDraw.ImageDraw,
    text: str,
    text_parameters: types.TextParameters,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
) -> tuple[int, int]:
    (text_box_left, text_box_top, text_box_right, text_box_bottom) \
        = draw.multiline_textbbox((0, 0), text, font=font)
    text_width = text_box_right - text_box_left
    text_left = _get_text_position_on_axis(
        text_parameters.rectangle.left,
        text_parameters.rectangle.right,
        text_width,
        text_parameters.horizontal_align,
    )
    text_height = text_box_bottom - text_box_top
    text_top = _get_text_position_on_axis(
        text_parameters.rectangle.top,
        text_parameters.rectangle.bottom,
        text_height,
        text_parameters.vertical_align,
    )
    return (text_left, text_top)

def get_watermark_position(
    draw: ImageDraw.ImageDraw,
    text: str,
    image_parameters: types.ImageParameters,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
) -> tuple[int, int]:
    (text_box_left, text_box_top, text_box_right, text_box_bottom) \
        = draw.multiline_textbbox((0, 0), text, font=font)
    text_width = text_box_right - text_box_left
    text_left = image_parameters.width - text_width
    text_height = text_box_bottom - text_box_top
    text_top = image_parameters.height - text_height - _get_font_descent(font)
    return (text_left, text_top)

def _add_modulus_to_negative(value: int, modulus: int) -> int:
    return value if value > 0 else value + modulus

def _crop(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(value, maximum))

def _get_text_position_on_axis(
    axis_start: int,
    axis_end: int,
    text_size: int,
    align: types.HorizontalAlign | types.VerticalAlign,
) -> int:
    axis_size = axis_end - axis_start
    if align in [types.HorizontalAlign.LEFT, types.VerticalAlign.TOP]:
        position = 0
    elif align in [types.HorizontalAlign.CENTER, types.VerticalAlign.CENTER]:
        position = (axis_size - text_size) // 2
    elif align in [types.HorizontalAlign.RIGHT, types.VerticalAlign.BOTTOM]:
        position = axis_size - text_size
    else:
        raise Exception('text alignment is incorrect')

    return position + axis_start

def _get_font_descent(
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
) -> int:
    if not isinstance(font, ImageFont.FreeTypeFont):
        return 0

    (_, font_descent) = font.getmetrics()
    return font_descent
