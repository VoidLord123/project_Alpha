import os

from lib.AnimatedSprite import AnimatedSprite


class PortalSprite(AnimatedSprite):
    def __init__(self, x, y, vx, vy, wc, hc, *group, state=0, linked_levelboard=None):
        super().__init__(x, y, vx, vy, wc, hc, *group, state=state, linked_levelboard=linked_levelboard)
        self.interval = 5
        for i in range(1, 19):
            self.paths.append(os.path.abspath(f"img\\portal_images\\sprite_{i}.png"))

