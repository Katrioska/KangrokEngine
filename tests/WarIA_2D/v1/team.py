from tests.WarIA_2D.v1.unit import Unit


class Team:
    def __init__(self, pos, team_id, unit_color, team_color, world, units = 20):
        self.base_pos = pos
        self.team_color = team_color
        self.unit_color = unit_color
        self.team_id = team_id
        self.world = world
        self.units = units

        self.score = 0

    def init(self):
        for _ in range(self.units):
            self.world.units.append(Unit(self.base_pos, self, self.team_id, self.unit_color, self.team_color))