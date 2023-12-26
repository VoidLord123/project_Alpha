import json
import os
import pygame

from lib.MapDict import LINKS
from lib.Board import Board
from lib.Sprite import Sprite

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
        self.sprite_groups = {}

    def load_level(self, filename: str):
        with open(filename, encoding="utf-8", mode="r") as file:
            source = list(map(lambda x: x.strip("\n"), file))
            wh_string = source[0]
            source = source[1:]
            assert wh_string.startswith("size: ")
            wh_string = wh_string[6:]
            wh_string = wh_string.split(";")
            wh_string = list(map(int, wh_string))
            self.rewrite_board(*wh_string, self.screen_size)
            source = list(map(lambda x: x.split(";"), source))
            for i in range(self.m):
                for j in range(self.n):
                    self.board[i][j] = LINKS[source[i][j]]()

    def save_level(self, filename: str):
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

    def load_sprite(self, filename: str):
        path = os.path.join('sprite_saves', (filename + '.json' if filename.endswith('.json') else filename))
        with open(path, encoding="utf-8", mode="r") as file:
            sprites = json.load(file)
        self.sprite_groups = sprites

    def save_sprite(self, filename: str):
        path = os.path.join('sprite_saves', (filename + '.json' if filename.endswith('.json') else filename))
        with open(path, encoding="utf-8", mode="r") as file:
            json.dump(self.sprite_groups, file)

    def parse_to_coord(self):
        for k, v in self.sprite_groups.items():
            self.sprite_groups[k][v] = list(map(lambda x: self.return_full_coordinates(x), self.sprite_groups[k][v]))

    def parse_to_sprites(self):
        for k, v in self.sprite_groups.items():
            self.sprite_groups[k][v] = list(map(lambda x: self.return_full_coordinates(x), self.sprite_groups[k][v]))

    def return_sprite(self, group, coord):
        coord = [coord[0] + coord[1] * self.cells_width, coord[2] + coord[3] * self.cells_height]
        sprite = Sprite()
        sprite.set_rect(*coord)
        return sprite

    def return_full_coordinates(self, sprite):
        c_w = self.cells_width
        c_h = self.cells_height
        c_x = sprite.rect.x // c_w
        c_y = sprite.rect.y // c_h
        x_in = sprite.rect.x % c_w / c_w
        y_in = sprite.rect.y % c_h / c_h
        return c_x, x_in, c_y, y_in