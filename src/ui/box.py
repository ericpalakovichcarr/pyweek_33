class Box:
    x: int
    y: int
    width: int
    height: int

    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def left(self) -> int:
        return self.x

    @property
    def right(self) -> int:
        return self.x + self.width - 1

    @property
    def top(self) -> int:
        return self.y

    @property
    def bottom(self) -> int:
        return self.y + self.height - 1

    @property
    def before_left(self) -> int:
        return self.left - 1

    @property
    def after_right(self) -> int:
        return self.right + 1

    @property
    def before_top(self) -> int:
        return self.top - 1

    @property
    def after_bottom(self) -> int:
        return self.bottom + 1
