import pygame
from lib.Cell import Cell, BaseCell


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

        self.debug_mode = False
        self.offset_vertical = offset_vertical
        self.offset_horizontal = offset_horizontal
        self.screen_size = screen_size
        self.m = m
        self.n = n
        self.cells_height = (screen_size[1] - 2 * offset_vertical) // m
        self.cells_width = (screen_size[0] - 2 * offset_horizontal) // n
        self.offset_x_sm = 0  # offset horizontal smooth
        self.offset_y_sm = 0  # offset vertical smooth
        # В нормальной ситуации эти два доп оффсеты будут равны 0))). Нооооооо есть допустим 480p )))
        if self.cells_width * n != screen_size[0]:
            self.offset_x_sm = (screen_size[0] - self.cells_width * n - self.offset_horizontal * 2) // 2
        if self.cells_height * m != screen_size[1]:
            self.offset_y_sm = (screen_size[1] - self.cells_height * m - self.offset_vertical * 2) // 2
        self.offset_vertical += self.offset_y_sm
        self.offset_horizontal += self.offset_x_sm
        self.board = [[Cell(self.cells_width, self.cells_height, [])] * self.n for _ in range(m)]

    def get_cell(self, x, y):
        """
        Возвращает координаты ячейки по координатам на экране или None если вне поля.
        :param x: Координаты по горизонтали
        :param y: Координаты по вертикали
        :return: Координаты в клетках
        """
        x_new, y_new = x - self.offset_horizontal, y - self.offset_vertical
        if self.cells_width * self.n >= x_new >= 0 and self.cells_height * self.m >= y_new >= 0:
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
        self.offset_x_sm = 0
        self.offset_y_sm = 0
        if self.cells_width * self.n != self.screen_size[0]:
            self.offset_x_sm = (self.screen_size[0] - self.cells_width * self.n - self.offset_horizontal * 2) // 2
        if self.cells_height * self.m != self.screen_size[1]:
            self.offset_y_sm = (self.screen_size[1] - self.cells_height * self.m - self.offset_vertical * 2) // 2
        self.offset_vertical += self.offset_y_sm
        self.offset_horizontal += self.offset_x_sm

    def rewrite_board(self, n, m, screen_size):
        self.n = n
        self.m = m
        self.screen_size = screen_size

        # self.offset_vertical -= self.offset_y_sm
        # self.offset_horizontal -= self.offset_x_sm
        self.cells_height = (self.screen_size[1] - 2 * self.offset_vertical) // m
        self.cells_width = (self.screen_size[0] - 2 * self.offset_horizontal) // n
        self.cells_width, self.cells_height = (
            min(self.cells_width, self.cells_height), min(self.cells_width, self.cells_height))
        self.offset_x_sm = 0
        self.offset_y_sm = 0
        self.board = [[BaseCell(self.cells_width, self.cells_height)] * n for _ in range(m)]
        if self.cells_width * n != self.screen_size[0]:
            self.offset_x_sm = (self.screen_size[0] - self.cells_width * n - self.offset_horizontal * 2) // 2
        if self.cells_height * m != self.screen_size[1]:
            self.offset_y_sm = (self.screen_size[1] - self.cells_height * m - self.offset_vertical * 2) // 2
        self.offset_vertical += self.offset_y_sm
        self.offset_horizontal += self.offset_x_sm

    def render(self, screen):
        y = 0
        for i in self.board:
            x = 0
            for j in i:
                screen.blit(j.get_image(self.cells_width, self.cells_height), self.get_cell_coord(x, y))
                if self.debug_mode:
                    pygame.draw.rect(screen, "black", (*self.get_cell_coord(x, y), self.cells_width,
                                                       self.cells_height), 1)

                x += 1
            y += 1
