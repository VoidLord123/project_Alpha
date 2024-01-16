from lib.Sprite import Sprite
from lib.SpriteGroup import SpriteGroup


class TestSprite1(Sprite):
    paths = ["img/test_sprite.png"]
    cell_width = 1
    cell_height = 1


class TestGroup1(SpriteGroup):
    pass
