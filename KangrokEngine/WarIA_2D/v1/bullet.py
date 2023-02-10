import math
import pygame

from ..constvars import *


class Bullet:
    def __init__(self, angle, startpos, id, shooter, speed=300, size = 3, damage=25):
        self.angle = angle
        self.pos = startpos
        self.speed = speed
        self.damage = damage
        self.id = id
        self.shooter = shooter
        self.time = 75
        self.actual_time = 0
        self.color = (200, 200, 200)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 2, 2)


    def process(self, dt):
        self.pos[0] = self.pos[0] + self.speed * math.cos(self.angle) * dt
        self.pos[1] = self.pos[1] + self.speed * math.sin(self.angle) * dt
        self.rect.center = self.pos

        self.actual_time += 1
        if self.actual_time > self.time:
            return True
        return False

    def render(self, window):
        pygame.draw.rect(window, self.color, self.rect)