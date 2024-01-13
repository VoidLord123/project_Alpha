import pygame
from lib.LevelBoard import LevelBoard


class LevelLoader:
    board: LevelBoard

    def __init__(self, screen_size: tuple[int, int], first_level_name: str, user_level_mode=False):
        self.user_level_mode = user_level_mode
        self.current_level_data = {}
        self.vertical_offset = 0
        self.horizontal_offset = 0
        self.screen_size = screen_size
        self.current_exits = {}
        self.load_level(first_level_name)
        self.screen = pygame.surface.Surface(screen_size)
        self.current_level_name = first_level_name

    def set_screen_size(self, screen_size: tuple[int, int], cells_size: tuple[int, int]):
        self.screen_size = screen_size
        if screen_size[-1] // cells_size[-1] > screen_size[0] // cells_size[0]:
            square_side = screen_size[0] // cells_size[0]
        else:
            square_side = screen_size[-1] // cells_size[-1]
        self.horizontal_offset = (screen_size[0] - square_side * cells_size[0]) // 2
        self.vertical_offset = (screen_size[1] - square_side * cells_size[1]) // 2
        self.screen = pygame.surface.Surface(screen_size)

    def load_level(self, level_name):
        self.current_level_name = level_name
        self.board = LevelBoard(self.screen_size, 0, 0, self)
        self.board.load(level_name + ".alphamap")
        self.set_screen_size(self.screen_size, (self.board.n, self.board.m))
        self.board.set_view(self.screen_size, self.horizontal_offset, self.vertical_offset)
        self.board.load_sprites(level_name + ".alphaspm")
        if not self.user_level_mode:
            self.load_extended(level_name + ".alphaextended")

    def draw(self):
        self.screen.fill("black")
        self.board.render(self.screen)

    def render(self, screen):
        self.draw()
        screen.blit(self.screen, (0, 0))

    def update(self, *args):
        self.board.update(*args)

    def exit(self, name_exit):
        if not self.user_level_mode:
            self.load_level(self.current_exits[name_exit])

    def load_extended(self, filename: str):
        with open(filename, encoding="utf-8", mode="r") as file:
            source = list(map(lambda x:  x.strip("\n").replace("    ", "$").replace("\t", "$"), file.readlines()))
            self.current_level_data["preview_text"] = source[0].split(": ")[1]
            i = 2
            while i < len(source) and source[i].startswith("$"):
                exit_name, name = source[i].split(": ")
                self.current_exits[exit_name[1:]] = name
                i += 1

