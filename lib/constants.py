from lib.entities.TestBlock import *
from lib.Cell import BaseCell
from lib.entities.TestSprites import *
from lib.SpriteGroup import SpriteGroup
from lib.entities.PlayerSprite import PlayerSprite


LINKS = {"W": TestWhite, "B": TestBlue, "N": BaseCell}

SPRITES = {"tst": TestSprite1, "player": PlayerSprite}

GROUPS = {"testGroup1": TestGroup1, "BaseGroup": SpriteGroup}

FPS = 100
