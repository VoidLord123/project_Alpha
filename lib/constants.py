from lib.entities.PortalSprite import PortalSprite
from lib.entities.TestBlock import *
from lib.Cell import BaseCell
from lib.entities.TestSprites import *
from lib.SpriteGroup import SpriteGroup
from lib.entities.PlayerSprite import PlayerSprite
from lib.entities.ExitSprite import ExitSprite
from lib.entities.KillSprite import KillSprite


LINKS = {"W": TestWhite, "B": TestBlue, "N": BaseCell}

SPRITES = {"tst": TestSprite1, "player": PlayerSprite, "exit": ExitSprite, "kill": KillSprite}


GROUPS = {"testGroup1": TestGroup1, "BaseGroup": SpriteGroup}

SPRITES["P"] = PortalSprite

FPS = 100
