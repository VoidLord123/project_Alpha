from lib.Sprite import Sprite
import pygame


class KillSprite(Sprite):
    paths = ["img/spike0.png", "img/spike1.png"]

    def __init__(self, x, y, vx, vy, wc, hc,  *group, state=0, linked_levelboard=None):
        super().__init__(x, y, vx, vy, wc, hc,  *group, state=state, linked_levelboard=linked_levelboard)
        self.sound = pygame.mixer.Sound("sounds/kill.wav")

    def action(self):
        self.sound.play()
        self.linked_levelboard.linked_loader.load_level(self.linked_levelboard.linked_loader.current_level_name)

    def update(self, *args):
        super().update(*args)
        if self.linked_levelboard is not None:
            for i in self.linked_levelboard.get_player_sprites().sprites():
                if pygame.sprite.collide_mask(self, i):
                    self.action()
                    break
