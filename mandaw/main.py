from mandaw.input import Input
import os, sys, pygame

class Mandaw:
    def __init__(self, title = "Mandaw", width = 800, height = 600, bg_color = "black"):
        self.width = width
        self.height = height
        self.title = title
        self.bg_color = bg_color
        self.background = None

        self.running = True

        pygame.init()
        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        path = os.path.dirname(os.path.abspath(__file__))
        self.icon = os.path.join(path, "./assets/mandaw.png")
        image = pygame.image.load(self.icon)
        pygame.display.set_icon(image)
        self.window.fill(self.bg_color)

        self.last = 0
        self.t = pygame.time.get_ticks()
        self.dt = (self.t - self.last) / 1000.0
        self.last = self.t

        self.delta = 1.0 / 60.0

        self.update_dt = 0
        self.update_handlers = []
        self.draw_handlers = []

        self.input = Input()

    def _update(self, dt):
        self.update_dt += dt
        while self.update_dt > self.delta:
            for update in self.update_handlers:
                update(self.delta)
            self.update_dt -= self.delta

    def _draw(self):
        for draw in self.draw_handlers:
            draw()

    def loop(self):
        while self.running:
            pygame.display.flip()
            self.clock.tick(60)

            pygame.display.update()

            self.input.update()

            self.t = pygame.time.get_ticks()
            self.dt = (self.t - self.last) / 1000.0
            self.last = self.t

            self.window.fill(self.bg_color)
            
            self._update(self.dt)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.input.get_key_pressed(self.input.keys["F5"]):
                os.execl(sys.executable, sys.executable, *sys.argv)

            self._draw()

            if self.background != None:
                self.background.draw()

        pygame.quit()
        quit()

    def quit(self):
        self.running = False
    
    def draw(self, fn):
        self.draw_handlers.append(fn)
        return fn

    def update(self, fn):
        self.update_handlers.append(fn)
        return fn

if __name__ == "__main__":
    from mandaw import Mandaw

    mandaw = Mandaw("Mandaw!", width = 800, height = 600, bg_color = "black")

    mandaw.loop()