from typing import List, Optional

from PIL import Image, ImageDraw

from .draw_image_grid import draw_image_grid
from .drawing.captions_overlay import overlay_captions
from .drawing.text_utils import *


def draw_labeled_image_grid(images: List[Image.Image],
                            labels_x: List[str],
                            labels_y: List[str],
                            title: Optional[str] = None,
                            captions: Optional[List[str]] = None,
                            fontsize: int = 16,
                            cell_width: Optional[int] = None,
                            max_space_y: float = 0.75,
                            margin: int = 10,
                            title_separator_thickness: int = 0,
                            border_width: int = 0) -> Image.Image:
    if len(images) != len(labels_x) * len(labels_y):
        raise ValueError('Number of images does not match numbers of X and Y labels')

    # Load font
    font = load_font(fontsize)

    cols = len(labels_x)
    rows = len(labels_y)

    grid = draw_image_grid(
        images,
        cols=cols,
        cell_width=cell_width,
        border_width=border_width
    )

    if captions is not None:
        grid = overlay_captions(
            grid,
            captions=captions,
            font=font,
            cols=cols,
            rows=rows,
            background_color=(255, 255, 255, 128)
        )

    cell_width = grid.width // cols
    cell_height = grid.height // rows

    line_spacing = fontsize // 2

    max_label_y_width = max([s[0] for s in compute_texts_sizes(labels_y, font)]) + margin * 2 if len(labels_y) > 0 else 0
    max_padding_left = int(cell_width * max_space_y)
    padding_left = min(max_label_y_width, max_padding_left)

    labels_x = wrap_texts(labels_x, font, line_length=cell_width - margin * 2)
    labels_y = wrap_texts(labels_y, font, line_length=padding_left - margin * 2)

    sizes_x = compute_texts_sizes(labels_x, font)
    sizes_y = compute_texts_sizes(labels_y, font)

    labels_x_height = max([s[1] for s in sizes_x]) + line_spacing * 2 if len(sizes_x) > 0 else 0
    padding_top = labels_x_height

    if title is not None:
        title = wrap_text(title, font, line_length=grid.width - margin * 2)
        title_size = compute_text_size(title, font)
        title_height = title_size[1] + line_spacing * 2 + title_separator_thickness
        title_width = title_size[0]
        padding_top += title_height
    else:
        title_height = 0
        title_width = 0

    canvas_size = (grid.width + padding_left, grid.height + padding_top)
    result = Image.new('RGB', canvas_size, 'white')
    result.paste(grid, (padding_left, padding_top))

    d = ImageDraw.Draw(result)

    for col in range(cols):
        x = padding_left + cell_width * col + cell_width / 2
        y = labels_x_height / 2 + title_height

        draw_text(labels_x[col], x, y, font, d)

    for row in range(rows):
        x = max(padding_left / 2, sizes_y[row][0] / 2)
        y = padding_top + cell_height * row + cell_height / 2

        draw_text(labels_y[row], x, y, font, d)

    if title is not None:
        x = grid.width / 2 + padding_left
        y = (title_height - title_separator_thickness) / 2

        draw_text(title, x, y, font, d)

        if title_separator_thickness > 0:
            x1 = x - title_width / 2
            x2 = x + title_width / 2
            y = title_height - title_separator_thickness
            d.line((x1, y, x2, y), fill=(0, 0, 0), width=title_separator_thickness)

    return result
