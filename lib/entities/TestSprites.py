from lib.Sprite import Sprite
from lib.SpriteGroup import SpriteGroup


class TestSprite1(Sprite):
    paths = ["img/test_sprite.png"]
    cell_width = 1
    cell_height = 1

    def __init__(self, x, y, vx, vy, *group, state=0):
        super().__init__(x, y, vx, vy, *group, state=state)


class TestGroup1(SpriteGroup):
    pass
