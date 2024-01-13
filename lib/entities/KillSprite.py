from lib.Sprite import Sprite
import pygame


class KillSprite(Sprite):
    paths = ["img/test_sprite.png"]

    def action(self):
        self.linked_levelboard.linked_loader.load_level(self.linked_levelboard.linked_loader.current_level_name)

    def update(self, *args):
        super().update(*args)
        for i in self.linked_levelboard.get_player_sprites().sprites():
            if pygame.sprite.collide_mask(self, i):
                self.action()
                break
