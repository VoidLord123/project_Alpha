from lib.Sprite import Sprite
import pygame


class ExitSprite(Sprite):
    paths = ["img/exit_test.webp"]

    def action(self):
        self.linked_levelboard.linked_loader.exit(self.name)  # Спрайт задумывался как именованный

    def update(self, *args):
        super().update(*args)
        for i in self.linked_levelboard.get_player_sprites().sprites():
            if pygame.sprite.collide_mask(self, i):
                self.action()
                break
