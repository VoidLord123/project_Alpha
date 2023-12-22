from lib.Cell import Cell

"""
Тестовые блоки
"""


class TestWhite(Cell):
    states = ["test_white.png", "test_white_st1.png"]

    def __init__(self):
        super().__init__(["test_white.png", "test_white_st1.png"])


class TestBlack(Cell):
    states = ["test_black.png", "test_black_st1.png"]

    def __init__(self):
        super().__init__(["test_black.png", "test_black_st1.png"])