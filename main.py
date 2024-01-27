import pygame
from lib.Game import Game


if __name__ == "__main__":

    pygame.init()
    pygame.display.set_icon(pygame.image.load("logo.png"))
    pygame.display.set_caption("Project Alpha")
    size = w, h = (1600, 900)
    game = Game(size)
    while game.running:
        game.update()
    pygame.quit()
