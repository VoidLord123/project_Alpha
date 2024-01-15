import pygame
from pygame.locals import VIDEORESIZE

from lib.constants import FPS
from lib.modules.Game import Game

"""
Тестирование и демонстрация класса Game
"""


if __name__ == "__main__":
    pygame.init()
    size = w, h = (1280, 720)
    screen = pygame.display.set_mode(size)
    game = Game(size)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.on_click(event.pos)
            if event.type == VIDEORESIZE:
                info = pygame.display.Info()
                x, y = info.current_w, info.current_h
                if event.size != (x, y) and event.size != game.last_size:
                    game.change_size(event.size)
        game.draw()
        screen.blit(game.screen, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

