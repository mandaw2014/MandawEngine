from mandaw.input import Input
from mandaw.color import Color
import sdl2, sdl2.ext, os

class Mandaw:
    def __init__(self, title = "Mandaw", width = 800, height = 600, bg_color = Color(0, 0, 0)):
        self.title = title
        self.width = width
        self.height = height
        self.bg_color = bg_color

        sdl2.ext.init()

        self.running = True

        self.window = sdl2.ext.Window(self.title, size = (self.width, self.height))
        self.window.show()

        self.window.bg_color = bg_color

        self.world = sdl2.ext.World()
        self.world.width = self.width
        self.world.height = self.height

        self.factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
        self.world.factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

        self.sprite_renderer = SoftwareRenderer(self.window, self)
        self.world.add_system(self.sprite_renderer)

        path = os.path.dirname(os.path.abspath(__file__))
        self.icon = os.path.join(path, "./assets/mandaw.png")

        self.input = Input()

        self.now = sdl2.SDL_GetTicks()
        self.last = 0
        self.dt = 0

        self.color = {
            "black":(0, 0, 0), "white":(255, 255, 255),
            "red":(255, 0, 0), "green":(0, 255, 0),
            "blue":(0, 0, 255), "yellow":(255, 255, 0),
            "cyan":(0, 255, 255), "magenta":(255, 0, 255),
            "silver":(192, 192, 192), "gray":(128, 128, 128),
            "maroon":(128, 0, 0), "olive":(128, 128, 0),
            "darkgreen":(0, 128, 0), "purple":(128, 0, 128),
            "teal":(0, 0, 128), "orange":(255, 165, 0),
            "turquoise":(64, 224, 208), "sky":(135, 206, 250),
            "pink":(255, 192, 203), "brown":(139, 69, 19)
        }
        
    def run(self):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                quit()
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                    quit()

        self.last = self.now
        self.now = sdl2.SDL_GetTicks()

        self.dt = int(((self.now - self.last) * 1000 / sdl2.SDL_GetPerformanceFrequency()))

        self.world.process()

class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window, mandaw):
        super().__init__(window)
        self.mandaw = mandaw

    def render(self, components):
        sdl2.ext.fill(self.surface, self.mandaw.bg_color)
        super().render(components)

if __name__ == "__main__":
    from mandaw import *

    mandaw = Mandaw(title = "Mandaw!", width = 800, height = 600, bg_color = Color(0, 0, 0))

    while True:
        mandaw.run()