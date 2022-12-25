from KangrokEngine import App, Scene
from KangrokEngine.Widgets import Text, Button

class MyScene(Scene):
    def __init__(self, window, active_scene):
        super().__init__(window, active_scene)
        self.add(Text("TEXTO DE PRUEBA", (400, 100), size=30))
        self.setBGimg("D:\Varios\Programacion\Python\Proyectos\KangrokEngine\\tests\mommmyyyyyy.png")
        self.add(Button((400, 400)))

MyApp = App("Widget Test", (800, 800))
MyApp.new_scene(0, MyScene, default=True)

MyApp.run()