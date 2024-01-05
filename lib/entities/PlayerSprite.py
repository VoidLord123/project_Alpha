import pygame
from lib.Sprite import Sprite
from lib.constants import VELOCITY_X, VELOCITY_Y, MAX_VELOCITY_PLAYER_X, ACCELERATION_PLAYER_X


class PlayerSprite(Sprite):
    paths = ["img/test_yellow.png"]

    def __init__(self, x, y, vx, vy, wc, hc, *group):
        super().__init__(x, y, vx, vy, wc, hc, *group)

    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.vx += ACCELERATION_PLAYER_X
        if keys[pygame.K_LEFT]:
            self.vx -= ACCELERATION_PLAYER_X

        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.vx += (-1 if self.vx > 0 else 1) * ACCELERATION_PLAYER_X

        if abs(self.vx) > MAX_VELOCITY_PLAYER_X:
            self.vx = MAX_VELOCITY_PLAYER_X * (self.vx // abs(self.vx))
        self.rect.x += self.vx * self.cell_width