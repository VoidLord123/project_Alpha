import pygame
from lib.LevelBoard import LevelBoard
from lib.Board import Board


class MapMaker:
    def __init__(self, screen_size: tuple[int, int], filename: str):
        self.vertical_offset = 0
        self.horizontal_offset = 0
        self.filename = filename
        self.screen_size = screen_size
        self.set_screen_size(screen_size)

        self.main_board = Board(32, 18, screen_size, self.horizontal_offset, self.vertical_offset)

    def set_screen_size(self, screen_size):
        if round(screen_size[0] / screen_size[1], 2) != round(16 / 9, 2) and 16 / 9 <= \
                screen_size[0] / screen_size[1]:
            self.horizontal_offset = screen_size[0] - round(self.screen_size[1] / 9 * 16)
            self.horizontal_offset //= 2
        elif screen_size[0] / screen_size[1] <= 16 / 9:
            self.vertical_offset = screen_size[1] - round(self.screen_size[0] / 16 * 9)
            self.vertical_offset //= 2
        else:
            self.horizontal_offset = 0
            self.vertical_offset = 0