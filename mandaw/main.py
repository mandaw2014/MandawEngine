import pygame

class Mandaw:
    def __init__(self, title = "Mandaw", width = 800, height = 600, bg_color = "black"):
        super().__init__()

        self.width = width
        self.height = height
        self.title = title
        self.bg_color = bg_color

        pygame.init()
        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.window.fill(self.bg_color)

        self.keys = pygame.key.get_pressed()

        self.UP = pygame.K_UP
        self.DOWN = pygame.K_DOWN
        self.LEFT = pygame.K_LEFT
        self.RIGHT = pygame.K_RIGHT
        
        self.W = pygame.K_w
        self.A = pygame.K_a
        self.S = pygame.K_s
        self.D = pygame.K_d

        self.SPACE = pygame.K_SPACE

    def run(self):
        pygame.display.flip()
        self.clock.tick(60)

        pygame.display.update()
        
        self.keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self.window.fill(self.bg_color)