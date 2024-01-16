import pygame

from lib.Sprite import Sprite


class MovedSprite(Sprite):
    paths = ["img/left.png", "img/right.png", "img/up.png", "img/down.png"]
    cell_width = 1
    cell_height = 1

    def action(self):
        self.vx = -1 if self.state == 0 else 1 if self.state == 1 else 0
        self.vy = -1 if self.state == 2 else 1 if self.state == 3 else 0

    def check_collides(self):
        if self.linked_levelboard is not None:
            collide_list = self.linked_levelboard.get_collide_objects()
            collide_sprites = self.linked_levelboard.get_collide_sprites()
            for i in collide_list:
                if self.rect.colliderect(i):
                    return True
            for i in collide_sprites.sprites():
                if i is not self and pygame.sprite.collide_mask(self, i):
                    return True
        return False

    def update(self, *args):
        super().update(*args)
        if self.vx != 0 or self.vy != 0:
            self.rect.x += self.vx * self.cell_width
            f1 = False
            f2 = False
            while self.check_collides():
                f1 = True
                self.rect.x -= self.vx / abs(self.vx)
            self.rect.y += self.vy * self.cell_height
            while self.check_collides():
                f2 = True
                self.rect.y -= self.vy / abs(self.vy)
            if f1:
                self.vx = 0
            if f2:
                self.vy = 0
