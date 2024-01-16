import pygame

from lib.Cell import Cell, BaseCell
from lib.LevelBoard import LevelBoard
from lib.Board import Board
from lib.SpriteGroup import SpriteGroup
from lib.constants import LINKS, SPRITES, BASIC_PARAMS


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
        self.inner_board.load_sprites(filename.split('.')[0] + '.alphaspm')
        self.screen = pygame.surface.Surface(screen_size)
        self.blocks = list(LINKS.keys())
        self.inner_board.debug_mode = True  # тут это уже значит не режим отладки, а рисование сетки
        self.sprites = list(SPRITES.keys())[1:] + ["move"]
        self.sprite_group = SpriteGroup()
        self.blocks_dict = {}
        self.chosen_block = ""
        x, y = 0, 1
        for i in self.blocks:
            x += 1
            x %= 6
            y = 7 + x // 6
            self.blocks_dict.setdefault(i, [])
            self.blocks_dict[i].append((False, x, y))
            self.main_board.board[y][x] = LINKS[i]()
        x, y = -1, 3
        state = 0
        for i in self.sprites:
            x += 1
            x %= 4
            y = y + (1 if x == 0 else 0)
            class_name = SPRITES[i].__name__
            self.blocks_dict.setdefault(i, [])
            self.blocks_dict[i].append((False, x + 28, y))
            sprite = SPRITES[i]((x + 28) * self.main_board.cells_width + self.main_board.offset_horizontal,
                                y * self.main_board.cells_height + self.main_board.offset_vertical,
                                *BASIC_PARAMS[class_name], self.main_board.cells_width, self.main_board.cells_height,
                                state=state)
            if class_name == "MovedSprite":
                state = (state + 1) % 2
            self.main_board.board[y][x + 28] = BaseCell()
            self.sprite_group.add(sprite)
        self.items = self.blocks + self.sprites

    def set_screen_size(self, screen_size):
        self.screen_size = screen_size
        self.vertical_offset = 0
        self.horizontal_offset = 0
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

    def on_click(self, x, y):
        pos = x, y
        if self.main_board.get_cell(*pos):
            cx, cy = self.main_board.get_cell(*pos)
            changed_block = None
            for i in self.items:
                for typee in range(len(self.blocks_dict[i])):
                    if self.blocks_dict[i][typee][1] == cx and self.blocks_dict[i][typee][2] == cy:
                        self.blocks_dict[i][typee] = (True, cx, cy)
                        changed_block = [i, typee]
                        self.chosen_block = [i, typee]
                        break
            if (cx, cy) in [(1, 1), (2, 1), (3, 1), (4, 1)]:
                self.inner_board.save(self.filename)
                self.inner_board.save_sprites(self.filename.split('.')[0] + '.alphaspm')
            if changed_block:
                for i in self.items:
                    for typee in range(len(self.blocks_dict[i])):
                        if changed_block[0] != i or (changed_block[0] == i and changed_block[1] != typee):
                            self.blocks_dict[i][typee] = (False, self.blocks_dict[i][typee][1],
                                                          self.blocks_dict[i][typee][2])
        cell = self.inner_board.get_cell(*pos)
        if self.chosen_block and self.inner_board.get_cell(*pos) and cell[0] < self.inner_board.n and cell[1] < self.inner_board.m:
            cx, cy = self.inner_board.get_cell(*pos)
            if len(self.chosen_block[0]) == 1:
                find = self.inner_board.find_obj(cx, cy)
                if find:
                    find[0].kill()
                self.inner_board.board[cy][cx] = LINKS[self.chosen_block[0]]()
            else:
                sprite = SPRITES[self.chosen_block[0]](cx, cy, *BASIC_PARAMS[SPRITES[self.chosen_block[0]].__name__],
                                                       self.main_board.cells_width, self.main_board.cells_height,
                                                       state=self.chosen_block[1])
                self.inner_board.board[cy][cx] = BaseCell()
                self.inner_board.add_sprite(sprite)

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
        self.screen.fill('white')
        self.main_board.render(self.screen)
        pygame.draw.rect(self.screen, "black", self.get_rect((1, 1), 4, 1), 2)
        self.draw_text("Сохранить", "black", (1, 1), self.main_board.cells_height - 15)
        self.draw_text("Блоки:", "black", (1, 5), self.main_board.cells_height - 15)
        self.draw_text("Спрайты:", "black", (28, 2), self.main_board.cells_height - 15)
        x1 = 1
        y1 = 7
        for i in range(12):
            pygame.draw.line(self.screen, "black", self.main_board.get_cell_coord(x1, y1 + i),
                             self.main_board.get_cell_coord(x1 + 6, y1 + i))
        for i in range(7):
            pygame.draw.line(self.screen, "black", self.main_board.get_cell_coord(x1 + i, y1),
                             self.main_board.get_cell_coord(x1 + i, y1 + 10))
        x1, y1 = 28, 4
        for i in range(5):
            pygame.draw.line(self.screen, "black", self.main_board.get_cell_coord(x1, y1 + i),
                             self.main_board.get_cell_coord(x1 + 4, y1 + i))
        for i in range(5):
            pygame.draw.line(self.screen, "black", self.main_board.get_cell_coord(x1 + i, y1),
                             self.main_board.get_cell_coord(x1 + i, y1 + 4))
        self.inner_board.render(self.screen)
        self.sprite_group.draw(self.screen)
        for i in self.items:
            for typee in range(len(self.blocks_dict[i])):
                # print(i)
                el = self.blocks_dict[i][typee]
                if el[0]:
                    pygame.draw.rect(self.screen, "red", self.get_rect((el[1], el[2]),
                                                                       1, 1), 3)

    def render(self, screen):
        self.draw()
        screen.blit(self.screen, (0, 0))

    def update(self, *args):
        pass