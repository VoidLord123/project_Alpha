from lib.entities.TestBlock import *
from lib.Cell import BaseCell

LINKS = {}

LINKS["W"] = TestWhite  # Добавлено в целях тестирования. В будущем будут настоящие блоки
LINKS["B"] = TestBlue
LINKS["N"] = BaseCell

SPRITES = {}

GROUPS = {}

FPS = 100
VELOCITY_X = 0.05
VELOCITY_Y = 0.05
