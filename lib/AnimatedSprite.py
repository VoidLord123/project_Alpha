from lib.Sprite import Sprite


class AnimatedSprite(Sprite):
    interval = 1

    def __init__(self, x, y, vx, vy, wc, hc, *group, state=0, linked_levelboard=None):
        super().__init__(x, y, vx, vy, wc, hc, *group, state=state, linked_levelboard=linked_levelboard)

    def update(self, *args):
        super().update(*args)
        self.change_state(interval=self.interval)
