import pygame
from lib.LevelBoard import LevelBoard
from lib.Board import Board
from lib.constants import LINKS


class MapMaker:
    def __init__(self, screen_size: tuple[int, int], filename: str):
        self.vertical_offset = 0
        self.horizontal_offset = 0
        self.filename = filename
        self.screen_size = screen_size
        self.set_screen_size(screen_size)

        self.main_board = Board(32, 18, screen_size, self.horizontal_offset, self.vertical_offset)
        self.inner_board = LevelBoard(self.screen_size,
                                      self.main_board.offset_horizontal + self.main_board.cells_width * 8,
                                      self.main_board.offset_vertical + self.main_board.cells_height)
        self.inner_board.load(filename)
        self.screen = pygame.surface.Surface(screen_size)
        self.blocks = list(LINKS.keys())
        self.inner_board.debug_mode = True  # тут это уже значит не режим отладки, а рисование сетки
        self.blocks_dict = {}
        self.main_block = ""
        x, y = 0, 1
        for i in self.blocks:
            x += 1
            x %= 6
            y = 7 + x // 6
            self.blocks_dict[i] = (False, x, y)
            self.main_board.board[y][x] = LINKS[i]()

    def set_screen_size(self, screen_size):
        self.screen_size = screen_size
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
        self.screen = pygame.surface.Surface(screen_size)

    def on_click(self, pos):
        if self.main_board.get_cell(*pos):
            cx, cy = self.main_board.get_cell(*pos)
            changed_block = None
            for i in self.blocks:
                if self.blocks_dict[i][1] == cx and self.blocks_dict[i][2] == cy:
                    self.blocks_dict[i] = (True, cx, cy)
                    changed_block = i
                    self.main_block = i
                    break
            if (cx, cy) in [(1, 1), (2, 1), (3, 1), (4, 1)]:
                self.inner_board.save(self.filename)
            if changed_block:
                for i in self.blocks:
                    if changed_block != i:
                        self.blocks_dict[i] = (False, self.blocks_dict[i][1], self.blocks_dict[i][2])
        if self.main_block and self.inner_board.get_cell(*pos):
            cx, cy = self.inner_board.get_cell(*pos)
            self.inner_board.board[cy][cx] = LINKS[self.main_block]()

    def get_rect(self, start_cell, w, h):  # все в ячейках
        start_cell_real = self.main_board.get_cell_coord(*start_cell)
        return *start_cell_real, w * self.main_board.cells_width, h * self.main_board.cells_height

    def draw_text(self, text, color, coord, size):
        font = pygame.font.Font("fonts/pixel_font2.ttf", size)
        text1 = font.render(text, 1, color)
        coord1_source = self.main_board.get_cell_coord(*coord)
        coord1 = ((self.main_board.cells_width * 4 - text1.get_width()) // 2 + coord1_source[0],
                  (self.main_board.cells_height - text1.get_height()) // 2 + coord1_source[1])
        self.screen.blit(text1, coord1)

    def draw(self):
        self.main_board.render(self.screen)
        pygame.draw.rect(self.screen, "white", self.get_rect((1, 1), 4, 1), 2)
        self.draw_text("Сохранить", "white", (1, 1), self.main_board.cells_height - 15)
        self.draw_text("Блоки:", "White", (1, 5), self.main_board.cells_height - 15)
        x1 = 1
        y1 = 7
        for i in range(12):
            pygame.draw.line(self.screen, "white", self.main_board.get_cell_coord(x1, y1 + i),
                             self.main_board.get_cell_coord(x1 + 6, y1 + i))
        for i in range(7):
            pygame.draw.line(self.screen, "white", self.main_board.get_cell_coord(x1 + i, y1),
                             self.main_board.get_cell_coord(x1 + i, y1 + 10))
        self.inner_board.render(self.screen)
        for j in self.blocks:
            i = self.blocks_dict[j]
            # print(i)
            if i[0]:
                pygame.draw.rect(self.screen, "red", self.get_rect((i[1], i[2]), 1, 1), 3)

