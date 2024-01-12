import pygame
from lib.LevelBoard import LevelBoard


class LevelLoader:
    board: LevelBoard

    def __init__(self, screen_size: tuple[int, int], first_level_name: str):
        self.vertical_offset = 0
        self.horizontal_offset = 0
        self.screen_size = screen_size
        self.load_level(first_level_name)
        self.screen = pygame.surface.Surface(screen_size)

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
        self.board = LevelBoard(self.screen_size, 0, 0)
        self.board.load(level_name + ".alphamap")
        self.set_screen_size(self.screen_size, (self.board.n, self.board.m))
        self.board.set_view(self.screen_size, self.horizontal_offset, self.vertical_offset)
        self.board.load_sprites(level_name + ".alphaspm")

    def draw(self):
        self.screen.fill("black")
        self.board.render(self.screen)

    def render(self, screen):
        self.draw()
        screen.blit(self.screen, (0, 0))

    def update(self, *args):
        self.board.update(*args)