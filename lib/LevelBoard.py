import pygame
from lib.MapDict import LINKS
from lib.Board import Board

"""
Класс уровня. Имеет сохранения и загрузки в файлы .alphamap

"""


class LevelBoard(Board):
    def __init__(self, screen_size: tuple[int, int], offset_horizontal: int, offset_vertical: int):
        """
        Инициализирует клеточное поле, но не загружает его. Если его не загрузить использовать нельзя
        :param screen_size: Размер экрана
        :param offset_horizontal: Отступ по горизонтали
        :param offset_vertical: Отступ по вертикали
        """
        super().__init__(1, 1, screen_size, offset_horizontal, offset_vertical)
        self.debug_mode = False  # режим отладки для простоты работы

    def load(self, filename: str):
        with open(filename, encoding="utf-8", mode="r") as file:
            source = list(map(lambda x: x.strip("\n"), file))
            wh_string = source[0]
            source = source[1:]
            assert wh_string.startswith("size: ")
            wh_string = wh_string[6:]
            wh_string = wh_string.split(";")
            wh_string = list(map(int, wh_string))
            self.rewrite_board(*wh_string)
            source = list(map(lambda x: x.split(";"), source))
            for i in range(self.m):
                for j in range(self.n):
                    self.board[i][j] = LINKS[source[i][j]]()

    def save(self, filename: str):
        with open(filename, mode="w", encoding="utf-8") as file:
            links_to_str = {}
            strs = LINKS.items()
            for i, j in strs:
                links_to_str[j] = i
            map_str = [f"size: {self.n}; {self.m}\n"]
            for i in self.board:
                map_str.append(";".join(map(lambda x: links_to_str[x.__class__], i)) + "\n")
                # Понимаю что данное решение не лучшее, но мне хочется разнести ячейки на отдельные классы
                # для возможности реализации что-то в конкретной ячейке или добавить разное поведение
                # для разных ячеек
            file.writelines(map_str)

    def render(self, screen):
        y = 0
        for i in self.board:
            x = 0
            for j in i:
                screen.blit(j.get_image(self.cells_width, self.cells_height), self.get_cell_coord(x, y))
                if self.debug_mode:
                    pygame.draw.rect(screen, "white", (*self.get_cell_coord(x, y), self.cells_width,
                                                       self.cells_height), 1)

                x += 1
            y += 1
