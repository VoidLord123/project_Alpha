import pygame


class Sprite(pygame.sprite.Sprite):
    paths = []
    cell_width = 0
    cell_height = 0

    def __init__(self, x, y, vx, vy, *group, state=0):
        super().__init__(*group)
        self.vx = vx
        self.vy = vy
        self.state = state
        if len(self.paths) > 0:
            self.set_image(self.paths[self.state])
        else:
            self.image = pygame.surface.Surface((10, 10))
            self.rect = self.image.get_rect()
        self.set_rect(x, y)

    def set_image(self, path):
        image = pygame.image.load(path)
        self.image = image
        try:
            x, y = self.rect.x, self.rect.y
            self.rect = image.get_rect()
            self.set_rect(x, y)
        except AttributeError:
            self.rect = image.get_rect()

    def change_state(self, new_state=None):
        if new_state:
            self.state = new_state
        else:
            self.state = (self.state + 1) % len(self.paths)
        self.set_image(self.paths[self.state])

    def set_rect(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        pass
