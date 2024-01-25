from lib.entities.ButtonSprite import ButtonSprite
from lib.entities.MovedSprite import MovedSprite
from lib.entities.Blocks import *
from lib.Cell import BaseCell
from lib.entities.TestSprites import *
from lib.SpriteGroup import SpriteGroup
from lib.entities.PlayerSprite import PlayerSprite
from lib.entities.ExitSprite import ExitSprite, GreenExitSprite, TheTrueExit, CoreExit
from lib.entities.KillSprite import KillSprite


LINKS = {"G": GrayBlock, "B": BlueBlock, "W": WhiteBlock, "N": BaseCell, "R": ReverseBlock}

SPRITES = {"tst": TestSprite1, "player": PlayerSprite, "exit": ExitSprite, "kill": KillSprite, "button": ButtonSprite,
           "move": MovedSprite, "green_exit": GreenExitSprite, "true_exit": TheTrueExit, "core": CoreExit}

BASIC_PARAMS = {"PlayerSprite": (0.1, 0.1), "ExitSprite": (0, 0), "KillSprite": (0, 0),
                "ButtonSprite": (0, 0), "MovedSprite": (0, 0), "GreenExitSprite": (0, 0), "TheTrueExit": (0, 0),
                "CoreExit": (0, 0)}

BASIC_GROUPS = {"PlayerSprite": "player", "ExitSprite": "action", "KillSprite": "action",
                "ButtonSprite": "action", "MovedSprite": "collide", "GreenExitSprite": "action",
                "TheTrueExit": "action", "CoreExit": "action"}

CLASS_NAME_TO_CLASS = {"PlayerSprite": PlayerSprite, "ExitSprite": ExitSprite, "KillSprite": KillSprite,
                       "ButtonSprite": ButtonSprite, "MovedSprite": MovedSprite, "GreenExitSprite": GreenExitSprite,
                       "TheTrueExit": TheTrueExit, "CoreExit": CoreExit}


GROUPS = {"testGroup1": TestGroup1, "BaseGroup": SpriteGroup}

FPS = 100
