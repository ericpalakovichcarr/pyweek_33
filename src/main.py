import pyxel
from ui.typefaces import TypefaceFinalFantasy
from ui.panel import Panel

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 240
SCREEN_PADDING = 8

BATTLE_TOP = 35
INFO_PANELS_TOP = 140


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        pyxel.mouse(True)

        pyxel.load("../assets/evil_rps.pyxres")

        self.typeface = TypefaceFinalFantasy()
        self.initialize_info_panels()
        pyxel.run(self.update, self.draw)

    def initialize_info_panels(self):
        # Make the height of each info panels fill all the remaining space
        # to the bottom of the screen
        info_panel_height = SCREEN_HEIGHT - SCREEN_PADDING - INFO_PANELS_TOP

        # Make the monster panel a set width
        self.panel_monsters = Panel(
            SCREEN_PADDING,
            INFO_PANELS_TOP,
            86,
            info_panel_height,
            self.typeface,
        )
        self.panel_monsters.set_text(
            [
                "SeaTROLL",
                "LOBSTER",
                "SeaSNAKE",
            ]
        )

        # Make the party panel fill all the remaining space
        # to the right edge of the screen
        gap_between_info_panels = 1
        left_and_right_margins = SCREEN_PADDING * 2
        party_panel_width = (
            SCREEN_WIDTH
            - left_and_right_margins
            - gap_between_info_panels
            - self.panel_monsters.width
        )
        self.panel_party = Panel(
            self.panel_monsters.after_right + gap_between_info_panels,
            INFO_PANELS_TOP,
            party_panel_width,
            info_panel_height,
            self.typeface,
        )
        self.panel_party.set_text(
            [
                "FIGHT",
                "MAGIC",
                "DRINK",
                "ITEM",
            ]
        )

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        self.panel_monsters.draw()
        self.panel_party.draw()
        self.typeface.blt("THE QUICK BROWN FOX JUMPED OVER", 2, 30)
        self.typeface.blt("THE LAZY DOG", 2, 40)
        self.typeface.blt("the quick brown fox jumped over", 2, 50)
        self.typeface.blt("the lazy dog", 2, 60)
        self.typeface.blt("The Quick Brown Fox Jumped Over", 2, 70)
        self.typeface.blt("The Lazy Dog", 2, 80)
        self.typeface.blt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 2, 90)
        self.typeface.blt("abcdefghijklmnopqrstuvwxyz", 2, 100)
        self.typeface.blt("0123456789", 2, 110)
        self.test_text(3, 3)

    def test_text(self, x, y):
        pyxel.text(x, y, "text(x,y,s,col)", 7)
        x += 4
        y += 8
        s = (
            f"Elapsed frame count is {pyxel.frame_count}\n"
            f"Current mouse position is ({pyxel.mouse_x},{pyxel.mouse_y})"
        )
        pyxel.text(x + 1, y, s, 1)
        pyxel.text(x, y, s, 9)


App()
