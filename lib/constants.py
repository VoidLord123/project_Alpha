from lib.entities.PortalSprite import PortalSprite
from lib.entities.TestBlock import *
from lib.Cell import BaseCell
from lib.entities.TestSprites import *

LINKS = {}

LINKS["W"] = TestWhite  # Добавлено в целях тестирования. В будущем будут настоящие блоки
LINKS["B"] = TestBlue
LINKS["N"] = BaseCell

SPRITES = {}

SPRITES["tst"] = TestSprite1
SPRITES["P"] = PortalSprite


GROUPS = {}

GROUPS["testGroup1"] = TestGroup1

FPS = 100

ACCELERATION_PLAYER_X = 0.1
ACCELERATION_PLAYER_Y = 0.1
MAX_VELOCITY_PLAYER_X = 10
MAX_GRAVITY_SPEED = 10
VELOCITY_PLAYER_JUMP = -10
