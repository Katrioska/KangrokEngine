import pygame
import random
import math
from KangrokEngine.WarIA_2D.v1.bullet import Bullet
from ..constvars import *

class Unit:
    def __init__(self, pos, team, teamid, color = (255, 0, 0), team_color = (128, 0, 0)):
        self.pos = pos
        self.color = color
        self.team = team
        self.teamid = teamid
        self.team_color = team_color
        self.speed = 10 #5
        self.angle = random.uniform(-90, 90)

        self.attack_range = 10
        self.attack_speed = 40
        self.attack_reload = 0

        self.hasShoot = False
        self.hp = 100

        #self.brain = UnitV1_NN()

        self.rect = pygame.Rect(self.pos[0]*g_w, self.pos[1]*g_w, 10, 10)

    def shot(self, projectiles):
        if not self.hasShoot:
            projectiles.append(Bullet(self.angle, [self.rect.centerx, self.rect.centery], self.teamid, self))
            self.hasShoot = True

    def process(self, dt, window, projectiles):

        if self.hasShoot:
            if self.attack_reload >= self.attack_speed:
                self.hasShoot = False
                self.attack_reload = 0
            else:
                self.attack_reload += 1
        self.shot(projectiles)

        #actions = self.brain.predict([[self.pos[0], self.pos[1], self.angle]], verbose=False)
        #self.angle += actions[1][0][0]

        self.angle += random.uniform(-0.25, 0.25)

        x = self.speed * math.cos(self.angle) * movement_factor * dt #* actions[0][0][0]
        y = self.speed * math.sin(self.angle) * movement_factor * dt #* actions[0][0][0]

        self.rect.move_ip(x,y)
        self.rect.clamp_ip(window.get_rect())

        #self.rect.centerx += self.speed * math.cos(self.angle) * dt#random.uniform(self.speed, -self.speed)
        #self.rect.centery += self.speed * math.sin(self.angle) * dt#random.uniform(self.speed, -self.speed)
        #self.rect.centerx = clamp(self.rect.centerx, 0, g_w*g_s)
        #self.rect.centery = clamp(self.rect.centery, 0, g_w*g_s)
        self.pos = [clamp(int(self.rect.centery/g_w), 0, g_s-1),
                    clamp(int(self.rect.centerx/g_w), 0, g_s-1)]

    def render(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        x = self.rect.centerx + math.cos(self.angle) * self.attack_range
        y = self.rect.centery + math.sin(self.angle) * self.attack_range

        pygame.draw.line(window, (255, 255, 255), (self.rect.centerx, self.rect.centery), (x, y), 1)