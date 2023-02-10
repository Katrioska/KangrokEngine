from KangrokEngine.WarIA_2D.v1.unit import Unit

class Team:
    def __init__(self, pos, team_id, unit_color, team_color, world, units = 5):
        self.base_pos = pos
        self.team_color = team_color
        self.unit_color = unit_color
        self.team_id = team_id
        self.world = world
        self.units = units

        for _ in range(units):
            self.world.units.append(Unit(pos, self, team_id, unit_color, team_color))

        self.score = 0