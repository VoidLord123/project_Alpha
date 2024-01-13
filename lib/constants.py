from lib.entities.ButtonSprite import ButtonSprite
from lib.entities.MovedSprite import MovedSprite
from lib.entities.TestBlock import *
from lib.Cell import BaseCell
from lib.entities.TestSprites import *
from lib.SpriteGroup import SpriteGroup
from lib.entities.PlayerSprite import PlayerSprite
from lib.entities.ExitSprite import ExitSprite
from lib.entities.KillSprite import KillSprite


LINKS = {"W": TestWhite, "B": TestBlue, "N": BaseCell}

SPRITES = {"tst": TestSprite1, "player": PlayerSprite, "exit": ExitSprite, "kill": KillSprite, "button": ButtonSprite,
           "move": MovedSprite}


GROUPS = {"testGroup1": TestGroup1, "BaseGroup": SpriteGroup}

FPS = 100
