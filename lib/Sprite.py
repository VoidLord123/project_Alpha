import pygame


class Sprite(pygame.sprite.Sprite):
    paths = []
    cell_width = 1
    cell_height = 1

    def __init__(self, x, y, vx, vy, wc, hc,  *group, state=0, linked_levelboard=None):
        super().__init__(*group)
        self.images = []
        self.linked_levelboard = linked_levelboard
        self.hc = hc
        self.wc = wc
        self.vx = vx
        self.vy = vy
        self.state = state
        self.init_images()
        if len(self.paths) > 0:
            self.set_image(self.state)
        else:
            self.image = pygame.surface.Surface((10, 10))
            self.scale()
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
        self.set_rect(x, y)

    def set_image(self, state):
        self.image = self.images[state]
        self.scale()
        try:
            x, y = self.rect.x, self.rect.y
            self.rect = self.image.get_rect()
            self.set_rect(x, y)
        except AttributeError:
            self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def change_state(self, new_state=None, interval=1):
        if new_state:
            self.state = new_state
        else:
            self.state = (self.state + 1) % (len(self.paths) * interval)
        self.set_image(self.state // interval)

    def set_rect(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        pass

    def init_images(self):
        self.images = []
        for i in self.paths:
            self.images.append(pygame.image.load(i))

    def scale(self):
        new_image = pygame.transform.scale(self.image, (self.wc * self.cell_width, self.hc * self.cell_height))
        self.image = new_image
