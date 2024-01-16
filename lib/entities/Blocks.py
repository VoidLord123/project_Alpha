from lib.Cell import Cell


class BlueBlock(Cell):
    states = ["blocks/blue_block.png"]
    is_collide = True

    def __init__(self):
        super().__init__(["blocks/blue_block.png"])


class GrayBlock(Cell):
    states = ["img/blocks/gray_block.png"]
    is_collide = True

    def __init__(self):
        super().__init__(["blocks/gray_block.png"])


class WhiteBlock(Cell):
    is_collide = True
    states = ["blocks/white_block.png"]

    def __init__(self):
        super().__init__(["blocks/white_block.png"])