from .ui import UI
from .ui.widgets import Widget
from .game_object import GameObject, Prefab

class Scene:
    widgets: list[Widget] = []

    def __init__(self):
        pass

    def load(self):
        pass

    def destroy(self):
        for i in GameObject.objects:
            GameObject.destroy(i)

        UI.widgets = []
        GameObject.objects = []
