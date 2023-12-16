import pygame


class Board:
    def __init__(self, n: int, m: int, screen_size: tuple[int, int], offset_horizontal: int, offset_vertical: int):
        """
        Инициализация поля.
        :param n: Ширина в клетках
        :param m: Высота в клетках
        :param screen_size: Размер экрана
        :param offset_horizontal: Смещение по горизонтали
        :param offset_vertical: Смещение по вертикали
        """

        self.offset_vertical = offset_vertical
        self.offset_horizontal = offset_horizontal
        self.screen_size = screen_size
        self.m = m
        self.n = n
        self.cells_height = (screen_size[1] - 2 * offset_vertical) // m
        self.cells_width = (screen_size[0] - 2 * offset_horizontal) // n
        self.board = [[None] * self.n for _ in range(m)]

    def get_cell(self, x, y):
        """
        Возвращает координаты ячейки по координатам на экране или None если вне поля.
        :param x: Координаты по горизонтали
        :param y: Координаты по вертикали
        :return: Координаты в клетках
        """
        x_new, y_new = x - self.offset_horizontal, y - self.offset_vertical
        if x_new <= self.cells_width * self.n and y_new <= self.cells_height * self.m and x_new >= 0 and y_new >= 0:
            return x_new // self.cells_width, y_new // self.cells_height
        return None

    def get_cell_coord(self, cx, cy):  #
        """
        Координаты левого верхнего угла по ячейке
        :param cx: координата x в ячейках
        :param cy: координата y в ячейках
        :return: координаты на экране
        """
        return self.offset_horizontal + cx * self.cells_width, self.offset_vertical + cy * self.cells_height

    def set_view(self, screen_size: tuple[int, int], offset_horizontal: int, offset_vertical: int):
        """
        Изменение параметров экрана
        :param screen_size: Размер экрана
        :param offset_horizontal: Смещение по горизонтали
        :param offset_vertical: Смещение по вертикали
        """

        self.offset_vertical = offset_vertical
        self.offset_horizontal = offset_horizontal
        self.screen_size = screen_size
        self.cells_height = (screen_size[1] - 2 * offset_vertical) // self.m
        self.cells_width = (screen_size[0] - 2 * offset_horizontal) // self.n

