import datetime
import math
import pickle
import random

import pygame

from tests.WarIA_2D.v1.constvars import *
from tests.WarIA_2D.v1.team import Team
from tests.WarIA_2D.v1.terrain import Terrain
from tests.WarIA_2D.v1.unit import Unit

MUTATION = 0.005
MIX = 0.25

def mix(weight_a, weight_b):
    new_weights = []
    for anidado_a, anidado_b in zip(weight_a, weight_b):
        new = []
        for i, j in zip(anidado_a, anidado_b):
            new.append(i + j * MIX)
        new_weights.append(new)
    weight_a = new_weights

def mutate(weights):
    new_weights = []
    for anidado in weights:
        new = []
        for i in anidado:
            new.append(i + random.uniform(MUTATION, -MUTATION))
        new_weights.append(new)
    return new_weights

class World:
    def __init__(self):
        self.world_grid = [[Terrain() for x in range(g_s)] for y in range(g_s)]
        self.units = []
        self.projectiles = []

        self.generations = 0
        self.steps = 128*10 + 1
        self.actual_steps = 0

        self.a_start_pos = [10, 40]
        self.b_start_pos = [70, 40]

        self.teams = [Team(self.a_start_pos, "A", (200, 100, 100), (128, 0, 0), self),#],
                      Team(self.b_start_pos, "B", (100, 100, 200), (0, 0, 128), self)]
        for _ in self.teams:
            _.init()

        print(size)

    def process(self, dt, window):
        for unit in self.units:


            closest = []
            for other_unit in self.units:

                if unit != other_unit and len(closest) < unit.view_count:
                    dst = math.sqrt((other_unit.pos[0] - unit.pos[0]) ** 2 + (other_unit.pos[1] - unit.pos[1]) ** 2)
                    if dst < unit.view_distance:
                        angle = math.atan2(other_unit.pos[1] - unit.pos[1], other_unit.pos[0] - unit.pos[0])

                        if unit.team == other_unit.team:
                            enemy = 0
                        else:
                            enemy = 1

                        closest.append([dst, angle, enemy])

            unit.process(dt, window, self.projectiles, closest, size)

            self.world_grid[unit.pos[0]][unit.pos[1]].color = unit.team_color

        for team in self.teams:
            team.score = 0

        for bullet in self.projectiles:
            for unit in self.units:
                if unit != bullet.shooter and bullet.shooter.teamid != unit.teamid:
                    if bullet.rect.colliderect(unit.rect):
                        unit.team.units -= 1
                        bullet.shooter.kills += 1
                        self.units.remove(unit)

            if bullet.process(dt):
                self.projectiles.remove(bullet)

        for row in self.world_grid:
            for column in row:
                for team in self.teams:
                    if column.color == team.team_color:
                        team.score += 1

        self.actual_steps += 1

        if self.actual_steps > self.steps:
            winner_team = None
            winner_units = []

            if self.teams[0].score > self.teams[1].score:
                winner_team = self.teams[0]
            else:
                winner_team = self.teams[1]

            for unit in self.units:
                if unit.teamid == winner_team.team_id:
                    winner_units.append(unit)

            self.units = []

            print(winner_team.team_id, len(winner_units))

            a = sorted(winner_units, key=lambda x: (-x.kills, -x.distance))

            real_winners = a[:5]

            #for w in real_winners:
            #    print(w.distance, w.kills)

            self.teams = [Team(self.a_start_pos, "A", (200, 100, 100), (128, 0, 0), self),  # ],
                          Team(self.b_start_pos, "B", (100, 100, 200), (0, 0, 128), self)]


            for i in real_winners:
                for j in real_winners:
                    if i != j:
                        mix(i.brain.weights_input, j.brain.weights_input)
                        mix(i.brain.weights_hidden, j.brain.weights_hidden)
                        mix(i.brain.weights_output, j.brain.weights_output)

            print(winner_units[0].brain.weights_input)


            for team in self.teams:
                team.units = 0
                for w in real_winners:
                    for i in range(4):
                        u = Unit(team.base_pos, team, team.team_id, team.unit_color, team.team_color)

                        u.brain.weights_input = mutate(w.brain.weights_input)
                        u.brain.weights_hidden = mutate(w.brain.weights_hidden)
                        u.brain.weights_output = mutate(w.brain.weights_output)

                        team.units += 1

                        self.units.append(u)

            self.world_grid = [[Terrain() for x in range(g_s)] for y in range(g_s)]

            data = {
                "generations" : self.generations,
                "winner_team" : winner_team,
                "winner_units" : winner_units
            }

            with open(f"v1\\weights\\{datetime.datetime.now().strftime('%d%m%Y_%H%M%S')}_{self.generations}.pickle", "wb") as f:
                pickle.dump(data, f)

            self.actual_steps = 0
            self.generations += 1


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