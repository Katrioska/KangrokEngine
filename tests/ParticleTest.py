import pygame

from KangrokEngine import App
from KangrokEngine import Scene

class Particle:
    def __init__(self, pos, radius = 5):
        self.position = pos
        self.radius = radius
        self.old_position = [0, 0]
        self.acceleration = [0, 0]

    def updatePosition(self, dt):
        velocity = [0, 0]
        #velocity = [self.position[0] - self.old_position[0], self.position[1], self.old_position[1]]
        self.old_position = self.position
        self.position = [self.position[0] + velocity[0] + self.acceleration[0] * dt,
                         self.position[1] + velocity[1] + self.acceleration[1] * dt]
        self.acceleration = [0, 0]

    def accelerate(self, acc):
        self.acceleration = [self.acceleration[0] + acc[0],
                             self.acceleration[1] + acc[1]]

    def render(self, window):
        pygame.draw.circle(window, pygame.Color("white"), self.position, self.radius)

class World:
    def __init__(self):
        self.gravity = [0, 4]

        self.particles = [Particle([400, 400])]

    def update(self, dt):
        self.applyGravity()
        self.updatePositions(dt)

    def updatePositions(self, dt):
        for particle in self.particles:
            particle.updatePosition(dt)
            print(particle.position)

    def applyGravity(self):
        for particle in self.particles:
            particle.accelerate(self.gravity)

    def renderAll(self, window):
        for particle in self.particles:
            particle.render(window)

class WorldScene(Scene):
    def __init__(self, window, active_scene):
        super().__init__(window, active_scene)
        self.world = World()

    def processManager(self, dt):
        self.world.update(dt)

    def renderManager(self, window):
        self.world.renderAll(window)

MyApp = App("Particle Test", (800, 800))
MyApp.new_scene(id=0, scene=WorldScene, default=True)
MyApp.run( )