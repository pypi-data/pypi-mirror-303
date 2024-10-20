import asyncio
from .scene import Scene
from .game_object import GameObject
from .ui import UI
from . import events

import pygame as pg
import logging


class Engine:

    logger: logging.Logger
    scene: Scene
    display: pg.Surface
    fps: int

    def __init__(self, app_name: str, fps: int, resolution: tuple[int, int] = (800, 600)):
        self.fps = fps
        self.app_name = app_name
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("[%(levelname)s][%(name)s]: %(message)s"))
        self.logger.addHandler(handler)
        self.init(resolution)

    def init(self, resolution: tuple[int, int] = (800, 600)):
        pg.init()
        pg.font.init()
        logging.basicConfig()
        self.display = pg.display.set_mode(resolution)
        pg.display.set_caption(self.app_name)
        logging.info("Game initialized.")

    async def run(self, scene: Scene):
        if (scene):
            scene.destroy()
            
        self.scene = scene
        scene.load()
        
        try:
            while True:
                await self.iteration()
                await asyncio.sleep(1 / self.fps)
        except Exception as e:
            logging.critical(e.with_traceback(None))
            exit(1)

    def event_processing(self, event: pg.event.Event):
        if event.type == pg.QUIT:
            logging.info("Quitting")
            exit()

    async def iteration(self):
        
        events.set(pg.event.get())
        
        for event in events.get():
            self.event_processing(event)
        
        for i in (GameObject.objects + UI.widgets):
            i.update()

        self.display.fill((0, 0, 0))
        for i in (GameObject.objects + UI.widgets):
            i.draw(self.display)

        pg.display.flip()
            
