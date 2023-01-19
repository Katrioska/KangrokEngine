import pygame.font

class Widget:
    def __init__(self, position):
        self.pos = position

    def process(self):
        pass

    def render(self, window):
        pass

class Text(Widget):
    def __init__(self, text, pos, size = 12, font = "Consolas", color = pygame.Color("white")):
        super().__init__(pos)
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont(font, self.size)
        self.color = color

    def update(self, text):
        self.text = text

    def render(self, window):
        for i, l in enumerate(self.text.splitlines()):
            window.blit(self.font.render(l, False, self.color), (self.pos[0], self.pos[1] + self.size * i))

class Button(Widget):
    def __init__(self, pos, size=(300, 100), command=None):
        super().__init__(pos)

        self.pressed = False

        self.toggle = False

        self.idle = pygame.Color("white")
        self.active = pygame.Color("green")
        self.blocked = pygame.Color("gray")
        self.selected = pygame.Color("yellow")

        self.rect = pygame.Rect(self.pos[0], self.pos[1], size[0], size[1])

        self.status = self.idle

        self.function = command

    def process(self, cursor):
        if cursor.rect.colliderect(self.rect):
            if not self.pressed:
                self.status = self.selected

                if cursor.left_click:
                    self.pressed = True
                    self.status = self.active
                    if self.function != None:
                        self.function()

            elif cursor.left_click:
                self.pressed = False
                self.status = self.selected
        else:
            if not self.pressed:
                self.status = self.idle



    def render(self, window):
        pygame.draw.rect(window, self.status, self.rect)