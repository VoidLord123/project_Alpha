import os
import pygame


class Cell:
    is_collide = False

    def __init__(self, width, height, states=[]):
        #  Наследники Cell не должны иметь states в конструкторе
        self.height = height
        self.width = width
        self.states = states
        self.images = list(map(Cell.load_image, states))
        self.state = 0
        if len(self.states) > 0:
            self.image = pygame.transform.scale(self.images[self.state], (self.width, self.height))
        else:
            self.images = [pygame.surface.Surface((1, 1))]
            self.image = pygame.transform.scale(self.images[self.state], (self.width, self.height))
            self.image.fill("white")

    @staticmethod
    def load_image(name):
        filename = 'img' + '/' + name
        image = pygame.image.load(filename)
        return image

    def get_image(self, cell_width, cell_height):
        return self.image

    def change_state(self, new_state: int):
        self.state = new_state
        self.image = pygame.transform.scale(self.images[self.state], (self.width, self.height))

    def scale(self):
        self.image = pygame.transform.scale(self.images[self.state], (self.width, self.height))

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.width}x{self.height}"


class BaseCell(Cell):
    def __init__(self, width, height):
        super().__init__(width, height, [])
