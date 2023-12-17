import os

import pygame


class Cell:

    def __init__(self, states:list[str]):
        self.states = states
        self.images = list(map(Cell.load_image, states))
        self.image = self.images[0]
        self.state = 0

    @staticmethod
    def load_image(name, colorkey=None):
        fullname = os.path.join('img', name)
        image = pygame.image.load(fullname)
        return image

    def get_image(self, cell_width, cell_height):
        return pygame.transform.scale(self.images[self.state], (cell_width, cell_height))

    def change_state(self, new_state: int):
        self.state = new_state
