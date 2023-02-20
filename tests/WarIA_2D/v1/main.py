from constvars import *

from KangrokEngine import App
from KangrokEngine import Scene
from KangrokEngine.Widgets import Text

from tests.WarIA_2D.v1.world import World

class GameScene(Scene):
    def __init__(self, window, active_scene):
        super().__init__(window, active_scene)
        self.cursor.isVisible = False
        self.world = World()
        self.info = Text(f"ACTUAL FPS: {self.actual_fps}", [0, 0])
        self.add(self.info)

    def processManager(self, dt):
        self.world.process(dt, self.window)

        info = f"ACTUAL FPS: {self.actual_fps}\n\n" \
               f"Delay: {self.delay}\n\n" \
               f"STEPS: {self.world.actual_steps}\n" \
               f"GENERATIONS: {self.world.generations}\n\n"

        for team in self.world.teams:
            info += f"TEAM {team.team_id} - SCORE {team.score}\n" \
                    f"TEAM {team.team_id} - UNITS {team.units}\n\n"

        self.info.update(info)

    def renderManager(self, window):
        self.world.render(window)

if __name__ == "__main__":
    MyApp = App("WarIA_2D Test", size)
    MyApp.fps = 60
    MyApp.new_scene(id=0, scene=GameScene, default=True)
    MyApp.run()