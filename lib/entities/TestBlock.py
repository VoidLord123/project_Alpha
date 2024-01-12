from lib.Cell import Cell

"""
Тестовые блоки
"""


class TestWhite(Cell):
    states = ["test_white.png", "test_white_st1.png"]
    is_collide = True

    def __init__(self):
        super().__init__(["test_white.png", "test_white_st1.png"])


class TestBlue(Cell):
    is_collide = True
    states = ["test_blue.png", "test_blue_st1.png"]

    def __init__(self):
        super().__init__(["test_blue.png", "test_blue_st1.png"])
