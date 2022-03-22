from typing import Union

import pyxel

from .box import Box
from .typefaces import Typeface


class Panel(Box):
    color_background: int
    color_inner_border: int
    color_outer_border: int
    border_width: int
    vert_side_height: int
    hort_side_width: int
    typeface: Typeface
    lines: list[str] = []
    padding: int
    line_gap: int

    def __init__(self, x: int, y: int, width: int, height: int, typeface: Typeface):
        super().__init__(x, y, width, height)
        self.color_background = 0
        self.color_inner_border = 7
        self.color_outer_border = 13
        self.border_width = 4
        self.padding = 12
        self.line_gap = 9
        self.vert_side_height = self.height - (self.border_width * 2)
        self.hort_side_width = self.width - (self.border_width * 2)
        self.typeface = typeface

    def set_text(self, lines: Union[str, list[str]]):
        if isinstance(lines, str):
            self.lines = [lines]
        else:
            self.lines = lines

    def draw(self):
        self._draw_border()
        self._draw_text()

    def _draw_border(self):
        # draw the gray box, white outline, and black interior
        pyxel.rect(self.x, self.y, self.width, self.height, self.color_outer_border)
        pyxel.rect(
            self.x + self.border_width,
            self.y + self.border_width,
            self.width - (self.border_width * 2),
            self.height - (self.border_width * 2),
            self.color_background,
        )
        pyxel.rectb(
            self.x + 1,
            self.y + 1,
            self.width - 2,
            self.height - 3,
            self.color_inner_border,
        )

        # round the corners of the box, clockwise from top-left
        pyxel.blt(self.x, self.y, 0, 0, 0, 4, 4)
        pyxel.blt(self.after_right - 4, self.y, 0, 0, 0, -4, 4)
        pyxel.blt(self.after_right - 5, self.after_bottom - 5, 0, 4, 0, -5, 5)
        pyxel.blt(self.x, self.after_bottom - 5, 0, 4, 0, 5, 5)

    def _draw_text(self):
        y = self.before_top + self.border_width + self.padding
        for text in self.lines:
            x = self.before_left + self.border_width + self.padding
            self.typeface.blt(text, x, y)
            y += self.typeface.line_height + self.line_gap
