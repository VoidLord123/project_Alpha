import pygame
from lib.Game import Game


if __name__ == "__main__":

    pygame.init()
    pygame.display.set_icon(pygame.image.load("logo.png"))
    pygame.display.set_caption("Project Alpha")
    size = w, h = (1280, 720)
    game = Game(size)
    game.show_fps = True
    while game.running:
        game.update()
    pygame.quit()
