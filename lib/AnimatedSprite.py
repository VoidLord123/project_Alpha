from lib.Sprite import Sprite


class AnimatedSprite(Sprite):
    def __init__(self, x, y, vx, vy, wc, hc, *group, state=0, linked_levelboard=None):
        super().__init__(x, y, vx, vy, wc, hc, *group, state=state, linked_levelboard=linked_levelboard)
        self.interval = 1

    def update(self, *args):
        super().update(*args)
        self.change_state(interval=self.interval)
