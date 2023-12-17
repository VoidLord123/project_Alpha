from lib.Board import Board

"""
Класс уровня. Имеет сериализацию и десериализацию в файлы .alphamap

"""


class LevelBoard(Board):
    def __init__(self, n: int, m: int, screen_size: tuple[int, int], offset_horizontal: int, offset_vertical: int):
        super().__init__(n, m, screen_size, offset_horizontal, offset_vertical)

