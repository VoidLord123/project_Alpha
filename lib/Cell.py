import os
import pygame


class Cell:
    is_collide = False

    def __init__(self, states: list[str]):
        #  Наследники Cell не должны иметь states в конструкторе
        self.states = states
        self.images = list(map(Cell.load_image, states))
        if len(self.states) > 0:
            self.image = self.images[0]
        else:
            self.images = [pygame.surface.Surface((1, 1))]
            self.image = self.images[0]
            self.image.fill("white")
        self.state = 0

    @staticmethod
    def load_image(name):
        fullname = os.path.join('img', name)
        image = pygame.image.load(fullname)
        return image

    def get_image(self, cell_width, cell_height):
        return pygame.transform.scale(self.images[self.state], (cell_width, cell_height))

    def change_state(self, new_state: int):
        self.state = new_state


class BaseCell(Cell):
    def __init__(self):
        super().__init__([])
