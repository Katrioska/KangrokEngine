
biome_colors = {
    "plains" : (86, 125, 70),
    "water" : (39, 75, 113)
}

class Cell:
    def __init__(self):
        self.type = "plains"

class World:
    def __init__(self):
        self.world_grid = []