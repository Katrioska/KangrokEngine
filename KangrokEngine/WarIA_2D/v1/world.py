import pygame

from ..constvars import *
from KangrokEngine.WarIA_2D.v1.team import Team
from KangrokEngine.WarIA_2D.v1.terrain import Terrain


class World:
    def __init__(self):
        self.world_grid = [[Terrain() for x in range(g_s)] for y in range(g_s)]
        self.units = []
        self.projectiles = []

        self.teams = [Team([20, 20], "A", (200, 100, 100), (128, 0, 0), self),
                      Team([60, 60], "B", (100, 100, 200), (0, 0, 128), self)]

        print(size)

    def process(self, dt, window):
        for unit in self.units:
            unit.process(dt, window, self.projectiles)

            self.world_grid[unit.pos[0]][unit.pos[1]].color = unit.team_color

        for team in self.teams:
            team.score = 0

        for bullet in self.projectiles:
            for unit in self.units:
                if unit != bullet.shooter and bullet.shooter.teamid != unit.teamid:
                    if bullet.rect.colliderect(unit.rect):
                        unit.team.units -= 1
                        self.units.remove(unit)

            if bullet.process(dt):
                self.projectiles.remove(bullet)

        for row in self.world_grid:
            for column in row:
                for team in self.teams:
                    if column.color == team.team_color:
                        team.score += 1

        return self.teams


    def render(self, window):
        x = 0
        y = 0
        for row in self.world_grid:
            for column in row:
                rect = pygame.Rect(x, y, g_w, g_w)
                pygame.draw.rect(window, column.color, rect)

                x = x + g_w
            y = y + g_w
            x = 0

        for unit in self.units:
            unit.render(window)

        for bullet in self.projectiles:
            bullet.render(window)