import pygame

from lib.Sprite import Sprite


class Player(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

    def horizontal_move(self, v, collision_group):
        self.rect = self.rect.move(v, 0)
        if pygame.sprite.spritecollideany(self, collision_group):
            self.rect = self.rect.move(-v, 0)

    def vertical_move(self, v, collision_group):
        self.rect = self.rect.move(0, v)
        if pygame.sprite.spritecollideany(self, collision_group):
            self.rect = self.rect.move(0, -v)

    def interact(self, interact_group):
        if pygame.sprite.spritecollideany(self, interact_group):
            pass
