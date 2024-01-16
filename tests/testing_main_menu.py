import pygame
from lib.modules.MainMenu import MainMenu


"""
Тестирование и демонстрация класса MainMenu
"""


if __name__ == "__main__":

    pygame.init()
    size = w, h = (1280, 720)
    screen = pygame.display.set_mode(size)
    main_menu = MainMenu(size)
    # main_menu.board.debug_mode = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu.on_click(*event.pos)
            main_menu.update(event)
        main_menu.draw()
        main_menu.update_tick()
        screen.blit(main_menu.screen, (0, 0))
        pygame.display.flip()
    pygame.quit()

