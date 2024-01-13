from lib.AnimatedSprite import AnimatedSprite
from lib.Sprite import Sprite
import pygame


class ExitSprite(AnimatedSprite):
    def __init__(self, x, y, vx, vy, wc, hc, *group, state=0, linked_levelboard=None):
        for i in range(1, 19):
            self.paths.append(f"img\\portal_images\\sprite_{i}.png")
        super().__init__(x, y, vx, vy, wc, hc, *group, state=state, linked_levelboard=linked_levelboard)
        self.interval = 5

    def action(self):
        self.linked_levelboard.linked_loader.exit(self.name)  # Спрайт задумывался как именованный

    def update(self, *args):
        super().update(*args)
        if self.linked_levelboard is not None:
            for i in self.linked_levelboard.get_player_sprites().sprites():
                if pygame.sprite.collide_mask(self, i):
                    self.action()
                    break
