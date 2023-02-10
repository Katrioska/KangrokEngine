__author__ = "Katrioska"

import time

from KangrokEngine.Widgets import Widget, Button

import pygame
pygame.init()

class App:
    def __init__(self, title, size, resizable=False, fps=60):
        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.isRunning = True

        self.fps = fps
        self.actual_fps = 0

        self.scenes = {}
        self.default_scene_id = None
        self.active_scene = None

    def run(self):
        if self.default_scene_id != None:
            self.active_scene = self.default_scene_id

        while self.isRunning:
            dt = self.clock.tick(self.fps)/1000
            self.actual_fps = round(self.clock.get_fps(), 1)
            self.scenes[self.active_scene].actual_fps = self.actual_fps
            self.scenes[self.active_scene].run(dt)

            if self.active_scene != self.scenes[self.active_scene].active_scene:
                self.active_scene = self.scenes[self.active_scene].active_scene
                self.scenes[self.active_scene].active_scene = self.active_scene

    def new_scene(self, id, scene, default = False):
        if id in self.scenes:
            raise IndexError(f"Scene ID {id} already registered")

        if self.default_scene_id != None and default:
            raise IndexError(f"Default scene is already registered")

        if default: self.default_scene_id = id
        self.scenes[id] = scene(self.window, self.default_scene_id)



class _Cursor:
    def __init__(self):
        self.isVisible = True
        self.rect = pygame.Rect(0, 0, 4, 4)
        self.left_click = False
        self.right_click = False
        self.middle_click = False

    def process(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] -2
        self.rect.y = pos[1] -2

    def render(self, window):
        if self.isVisible:
            pygame.draw.rect(window, pygame.Color("red"), self.rect)



class Scene:
    def __init__(self, window, active_scene):
        self.pause = True
        self.window = window
        self.active_scene = active_scene

        self.cursor = _Cursor()
        self.__hasMouseEvent = False

        self.___imgPaths = {}
        self.loaded = False

        self.delay = 0
        self.actual_fps = 0

        self.__keys = {}
        self.__widgets = []

        self.background_color = pygame.Color("black")

    def __keyManager(self):
        if self.__hasMouseEvent:
            self.__hasMouseEvent = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key in self.__keys:
                    self.__keys[event.key]()

            if event.type == pygame.MOUSEBUTTONDOWN:
                button = event.button
                self.__hasMouseEvent = True

                if button == 1:
                    self.cursor.left_click = True
                    self.on_left_click()

        if not self.__hasMouseEvent:
            self.cursor.left_click = False

    def on_left_click(self):
        pass
        #print("TEST")

    def on_right_click(self):
        pass

    def on_middle_click(self):
        pass

    def __widgetsManager(self, window):
        for widget in self.__widgets:
            if type(widget) == Button: widget.process(self.cursor)

            widget.render(window)

    def eventManager(self):
        pass

    def processManager(self, dt):
        """
        This will be executed every time.
        """
        pass

    def renderManager(self, window):
        pass

    def run(self, dt):
        if not self.loaded:
            for name, image in self. ___imgPaths.items():
                self.___imgPaths[name] = pygame.image.load(image)
            self.loaded = True

        self.pause = False
        if not self.pause:
            start = time.time()
            self.cursor.process()
            self.__keyManager()
            self.eventManager()
            self.processManager(dt)

            if self.background_color != None:
                self.window.fill(self.background_color)
            else:
                self.window.blit(self.___imgPaths["BGimg"], (0, 0))

            self.renderManager(self.window)
            self.__widgetsManager(self.window)
            self.cursor.render(self.window)
            pygame.display.flip()

            end = time.time()
            self.delay = end - start

    def keybind(self, key, function):
        self.__keys[key] = function

    def setActiveScene(self, id):
        self.active_scene = id

    def setBGcolor(self, color):
        self.background_color = color
        self.background_image = None

    def setBGimg(self, imagepath):
        self.background_color = None
        self.___imgPaths["BGimg"] = imagepath

    def add(self, object):
        if isinstance(object, Widget):
            self.__widgets.append(object)