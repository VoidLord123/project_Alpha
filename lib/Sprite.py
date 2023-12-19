import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, *group, paths=[], state=0):
        super().__init__(*group)
        self.paths = paths
        self.state = state
        self.set_image(self.paths[self.state])

    def set_image(self, path):
        image = pygame.image.load(path)
        self.image = image
        self.rect = image.get_rect()

    def change_state(self, new_state=None):
        if new_state:
            self.state = new_state
        else:
            self.state = (self.state + 1) % len(self.paths)

    def set_rect(self, x, y):
        self.rect.x = x
        self.rect.y = y
