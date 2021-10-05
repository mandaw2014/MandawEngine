import sdl2.ext

class Color(sdl2.ext.Color):
    def __init__(self, r, g, b, a = 255):
        super().__init__(
            r, g, b, a
        )