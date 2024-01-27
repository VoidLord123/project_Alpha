import pygame

from lib.Sprite import Sprite


class ButtonSprite(Sprite):
    paths = ["img/button.png"]

    def __init__(self, x, y, vx, vy, wc, hc,  *group, state=0, linked_levelboard=None):
        super().__init__(x, y, vx, vy, wc, hc, *group, state=state, linked_levelboard=linked_levelboard)
        self.link = []

    def action(self):
        if self.link:
            for sprite in self.link:
                self.linked_levelboard.named_sprites[sprite].action()

    def update(self, *args):
        super().update(*args)
        if self.linked_levelboard is not None:
            for i in self.linked_levelboard.get_player_sprites().sprites():
                if pygame.sprite.collide_mask(self, i):
                    self.action()
                    break
