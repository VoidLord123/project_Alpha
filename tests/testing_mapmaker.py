import pygame
from lib.modules.MapMaker import MapMaker

"""
Тестирование и демонстрация класса MapMaker
"""


if __name__ == "__main__":

    pygame.init()
    size = w, h = (1280, 720)
    screen = pygame.display.set_mode(size)
    mapmaker = MapMaker(size, "test4.alphamap")
    # mapmaker.main_board.debug_mode = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mapmaker.on_click(event.pos)
        mapmaker.draw()
        screen.blit(mapmaker.screen, (0, 0))
        pygame.display.flip()
    pygame.quit()

