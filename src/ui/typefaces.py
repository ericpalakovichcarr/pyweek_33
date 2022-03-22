from itertools import chain
from pdb import line_prefix

import pyxel

from .box import Box

ResMapping = dict[str, Box]


def create_res_mapping(
    starting_x: int,
    starting_y: int,
    line_height: int,
    supported_characters: str,
    charcters_last_on_line: str,
    width_groupings: list[tuple[str, int]],
) -> ResMapping:
    res_mapping: dict[str, ResCharacter] = {}
    x = starting_x
    y = starting_y

    if (
        "".join(chain([characters for characters, _ in width_groupings]))
        != supported_characters
    ):
        raise ValueError(
            "Characters for text mapping different from supported characters"
        )

    for characters, width in width_groupings:
        for character in characters:
            res_mapping[character] = ResCharacter(x, y, width, line_height)
            x += width
            if character in charcters_last_on_line:
                x = starting_x
                y += line_height

    return res_mapping


class ResCharacter(Box):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)


class Typeface:
    image_bank: int
    image_color_key: int
    line_height: int
    space_width: int = 5
    supported_characters: str = ""
    res_mapping: ResMapping

    def __init__(
        self,
        image_bank: int,
        image_color_key: int,
        line_height: int,
        supported_characters: str,
        res_mapping: ResMapping,
    ):
        self.image_bank = image_bank
        self.image_color_key = image_color_key
        self.line_height = line_height
        self.supported_characters = supported_characters
        self.res_mapping = res_mapping

    def blt(self, text: str, x: int, y: int):
        self._validate_text(text)
        for character in text:
            if character == " ":
                x += self.space_width
                continue
            pyxel.blt(
                x,
                y,
                self.image_bank,
                self.res_mapping[character].x,
                self.res_mapping[character].y,
                self.res_mapping[character].width,
                self.res_mapping[character].height,
                self.image_color_key,
            )
            x += self.res_mapping[character].width + 1

    def _validate_text(self, text):
        unsupported_characters_in_text = set(text.replace(" ", "")).difference(
            set(self.supported_characters)
        )
        if unsupported_characters_in_text:
            raise ValueError(
                f"{self.__class__.__name__} doesn't support {unsupported_characters_in_text}"
            )


class TypefaceFinalFantasy(Typeface):
    def __init__(self):
        line_height = 7
        supported_characters = (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        )
        super().__init__(
            image_bank=1,
            image_color_key=0,
            line_height=line_height,
            supported_characters=supported_characters,
            res_mapping=create_res_mapping(
                0,
                0,
                line_height,
                supported_characters,
                "o",
                [
                    ("A", 7),
                    ("B", 6),
                    ("CDEFGH", 7),
                    ("I", 4),
                    ("JKLMNOPQRS", 7),
                    ("T", 8),
                    ("UVWX", 7),
                    ("Y", 8),
                    ("Z", 7),
                    ("a", 6),
                    ("bc", 5),
                    ("d", 6),
                    ("efgh", 5),
                    ("i", 2),
                    ("j", 4),
                    ("k", 6),
                    ("l", 2),
                    ("m", 7),
                    ("nop", 5),
                    ("qrs", 6),
                    ("t", 5),
                    ("uv", 6),
                    ("w", 7),
                    ("xyz", 6),
                    ("0", 7),
                    ("1", 4),
                    ("23456789", 7),
                ],
            ),
        )
