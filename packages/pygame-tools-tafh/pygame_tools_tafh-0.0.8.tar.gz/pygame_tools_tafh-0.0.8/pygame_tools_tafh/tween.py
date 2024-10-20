import asyncio

class Tweens:

    tweens: list = []

    def __init__(self):
        self.tweens = []

    def add(self, target: any,
            property: str,
            fr: float,
            to: float,
            repeat: int = -1,
            duration: int = 1000,
            delay: int = 0):
        loop = asyncio.get_event_loop()
        loop.create_task(self.start_tween(target, property, fr, to, repeat, duration, delay))
        
    async def start_tween(self, target: any,
            property: str,
            fr: float,
            to: float,
            repeat: int = -1,
            duration: int = 1000,
            delay: int = 0):
        await asyncio.sleep(delay)
        for i in range((repeat, 1)[repeat == -1]):
            for i in range(60 * duration):
                setattr(target, property, fr + (to - fr) * (i / (60 * duration)))
                await asyncio.sleep(1 / 60)
