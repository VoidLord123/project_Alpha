from lib.AnimatedSprite import AnimatedSprite
import pygame


class ExitSprite(AnimatedSprite):
    paths = [f"img\\blue_portal\\sprite_{i}.png" for i in range(0, 18)]
    interval = 5

    def __init__(self, x, y, vx, vy, wc, hc, *group, state=0, linked_levelboard=None):
        super().__init__(x, y, vx, vy, wc, hc, *group, state=state, linked_levelboard=linked_levelboard)
        self.portal_sound = pygame.mixer.Sound("sounds/portal.wav")

    def action(self):
        self.portal_sound.play()
        self.linked_levelboard.linked_loader.exit(self.name)  # Спрайт задумывался как именованный

    def update(self, *args):
        super().update(*args)
        if self.linked_levelboard is not None:
            for i in self.linked_levelboard.get_player_sprites().sprites():
                if pygame.sprite.collide_mask(self, i):
                    self.action()
                    break


class GreenExitSprite(ExitSprite):
    paths = [f"img\\green_portal\\sprite_{i:02}.png" for i in range(0, 18)]


class TheTrueExit(ExitSprite):
    interval = 2
    paths = [f"img\\true_portal\\sprite_{i}.png" for i in range(0, 8)]
    cell_width = 2
    cell_height = 2


class CoreExit(ExitSprite):
    paths = [f"img\\core\\sprite_{i:02}.png" for i in range(0, 20)]
    cell_height = 3
    cell_width = 3


class TheTrueExitRed(TheTrueExit):
    paths = [f"img\\red_true_portal\\sprite_{i}.png" for i in range(0, 8)]
    cell_width = 3
    cell_height = 3


class RedExitSprite(GreenExitSprite):
    paths = [f"img\\red_portal\\sprite_{i:02}.png" for i in range(0, 18)]
