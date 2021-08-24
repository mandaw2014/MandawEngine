from mandaw import *

class MainMenu:
    def __init__(self, window):
        self.title = Sprite(window, "./assets/title.png", 0, 0, size = (300, 100))
        
        self.title.x = window.width / 2 - 150
        self.title.y = 50

        self.instructions = Text(window, "Press Space To Play", font_size = 40, color = "white")
        
        self.instructions.x = 270
        self.instructions.y = window.height / 2 - 20

        self.enabled = True