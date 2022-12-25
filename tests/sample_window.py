import pygame

from KangrokEngine import App
from KangrokEngine import Scene
from KangrokEngine.Widgets import Text

class Red(Scene):
    def __init__(self, window, active_scene):
        super().__init__(window, active_scene)

        self.background_color = pygame.Color("red")
        self.keybind(pygame.K_r, lambda: self.setActiveScene(0))
        self.keybind(pygame.K_g, lambda: self.setActiveScene(1))
        self.keybind(pygame.K_b, lambda: self.setActiveScene(2))


class Green(Scene):
    def __init__(self, window, active_scene):
        super().__init__(window, active_scene)

        self.background_color = pygame.Color("green")
        self.keybind(pygame.K_r, lambda: self.setActiveScene(0))
        self.keybind(pygame.K_g, lambda: self.setActiveScene(1))
        self.keybind(pygame.K_b, lambda: self.setActiveScene(2))


class Blue(Scene):
    def __init__(self, window, active_scene):
        super().__init__(window, active_scene)

        self.background_color = pygame.Color("blue")
        self.keybind(pygame.K_r, lambda: self.setActiveScene(0))
        self.keybind(pygame.K_g, lambda: self.setActiveScene(1))
        self.keybind(pygame.K_b, lambda: self.setActiveScene(2))


MyApp = App("Sample Window", (800, 800))
MyApp.new_scene(id=0, scene=Red, default=True)
MyApp.new_scene(id=1, scene=Green)
MyApp.new_scene(id=2, scene=Blue)
MyApp.run()