from lib.Cell import Cell


class CellMapmaker(Cell):
    def __init__(self, states: list[str]):
        super().__init__(states)
        self.activated = False
