from lib.entities.ButtonSprite import ButtonSprite
from lib.entities.MovedSprite import MovedSprite
from lib.entities.TestBlock import *
from lib.Cell import BaseCell
from lib.entities.TestSprites import *
from lib.SpriteGroup import SpriteGroup
from lib.entities.PlayerSprite import PlayerSprite
from lib.entities.ExitSprite import ExitSprite
from lib.entities.KillSprite import KillSprite


LINKS = {"W": TestWhite, "B": TestBlue, "N": BaseCell, "C": Cell}

SPRITES = {"tst": TestSprite1, "player": PlayerSprite, "exit": ExitSprite, "kill": KillSprite, "button": ButtonSprite,
           "move": MovedSprite}

BASIC_PARAMS = {"PlayerSprite": (0.1, 0.1), "ExitSprite": (0, 0), "KillSprite": (0, 0),
                "ButtonSprite": (0, 0), "MovedSprite": (0, 0)}

BASIC_GROUPS = {"PlayerSprite": "player", "ExitSprite": "action", "KillSprite": "collide",
                "ButtonSprite": "action", "MovedSprite": "collide"}

CLASS_NAME_TO_CLASS = {"PlayerSprite": PlayerSprite, "ExitSprite": ExitSprite, "KillSprite": KillSprite,
                       "ButtonSprite": ButtonSprite, "MovedSprite": MovedSprite}


GROUPS = {"testGroup1": TestGroup1, "BaseGroup": SpriteGroup}

FPS = 100
