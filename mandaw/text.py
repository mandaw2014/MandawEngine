import mandaw.main


class Text:
    def __init__(self, text, window: mandaw.main.Mandaw, font, color, x=0, y=0):
        self.text = font.render(text, True, color)
        self.window = window
        self.x = x
        self.y = y
        self.color = color
        self.font = font

    def draw(self):
        self.window.window.blit(self.text, (self.x, self.y))

    def change_text(self, text):
        self.text = self.font.render(text, True, self.color)

