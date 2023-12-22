import pygame
from lib.modules.MapMaker import MapMaker

"""
Тестирование и демонстрация класса LevelBoard
"""


if __name__ == "__main__":

    pygame.init()
    size = w, h = (1280, 720)
    screen = pygame.display.set_mode(size)
    mapmaker = MapMaker(size, "")
    mapmaker.main_board.debug_mode = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        mapmaker.main_board.render(screen)
        pygame.display.flip()
    pygame.quit()

