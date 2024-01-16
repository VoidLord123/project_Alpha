import pygame


class SpriteGroup(pygame.sprite.Group):
    def __init__(self, *group):
        super().__init__(*group)
