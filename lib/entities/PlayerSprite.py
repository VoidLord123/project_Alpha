import pygame
from lib.Sprite import Sprite

ACCELERATION_PLAYER_X = 0.2
ACCELERATION_PLAYER_Y = 0.3
MAX_VELOCITY_PLAYER_X = 10
MAX_GRAVITY_SPEED = 10
VELOCITY_PLAYER_JUMP = -15
TRANSFORM = 0.01


class PlayerSprite(Sprite):
    paths = ["img/players/blue_player.png", "img/players/green_player.png"]

    def __init__(self, x, y, vx, vy, wc, hc,  *group, state=0, linked_levelboard=None):
        self.extra_x_speed = 0
        self.extra_y_speed = 0
        super().__init__(x, y, vx, vy, wc, hc,  *group, state=state, linked_levelboard=linked_levelboard)

    def check_collides(self):
        if self.linked_levelboard is not None:
            collide_list = self.linked_levelboard.get_collide_objects()
            collide_sprites = self.linked_levelboard.get_collide_sprites()
            for i in collide_list:
                if self.rect.colliderect(i):
                    return True
            for i in collide_sprites.sprites():
                if pygame.sprite.collide_mask(self, i):
                    return True
        return False

    def collide_with_move_sprite(self):
        if self.linked_levelboard is not None:
            collide_sprites = self.linked_levelboard
            for i in collide_sprites.sprites():
                if pygame.sprite.collide_mask(self, i):
                    return True

    def update(self, *args):
        super().update(*args)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.vx += ACCELERATION_PLAYER_X
        if keys[pygame.K_LEFT]:
            self.vx -= ACCELERATION_PLAYER_X

        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.vx += (-1 if self.vx > 0 else 1) * ACCELERATION_PLAYER_X

        if abs(self.vx) > MAX_VELOCITY_PLAYER_X:
            self.vx = MAX_VELOCITY_PLAYER_X * (self.vx // abs(self.vx))
        self.rect.y += 1
        on_block = self.check_collides()
        self.rect.y -= 1

        self.rect.y -= 1
        under_block = self.check_collides()
        self.rect.y += 1
        if on_block:
            self.vy = 0
        if keys[pygame.K_UP] and not self.check_collides() and on_block:
            self.vy = VELOCITY_PLAYER_JUMP
        if under_block and self.vy < 0:
            self.vy = 0

        self.rect.x += 1
        right_block = self.check_collides()
        self.rect.x -= 1

        self.rect.x -= 1
        left_block = self.check_collides()
        self.rect.x += 1

        if left_block and self.vx < 0 or right_block and self.vx > 0:
            self.vx = 0

        self.vy += ACCELERATION_PLAYER_Y
        if self.vy > MAX_GRAVITY_SPEED:
            self.vy = MAX_GRAVITY_SPEED
        self.rect.x += self.vx * self.wc * TRANSFORM
        while self.check_collides() and self.vx != 0:
            self.rect.x -= self.vx / abs(self.vx)
        self.rect.y += self.vy * self.hc * TRANSFORM
        while self.check_collides():
            self.rect.y -= self.vy / abs(self.vy)