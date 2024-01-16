import pygame
from lib.constants import FPS
from lib.Game import Game


if __name__ == "__main__":

    pygame.init()
    size = w, h = (1280, 720)
    game = Game(size)
    clock = pygame.time.Clock()
    font = pygame.font.Font("fonts/pixel_font2.ttf", 30)
    while game.running:
        game.update()
        clock.tick(FPS)

    pygame.quit()
