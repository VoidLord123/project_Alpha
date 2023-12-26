from lib.SpriteGroup import SpriteGroup


class CollisionGroup(SpriteGroup):
    def __init__(self, *groups):
        super().__init__(*groups)
