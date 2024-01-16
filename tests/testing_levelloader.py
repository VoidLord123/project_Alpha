import pygame
from lib.modules.LevelLoader import LevelLoader
from lib.constants import FPS

"""
Тестирование и демонстрация класса LevelLoader а так же некоторых классов спрайтов
"""


if __name__ == "__main__":

    pygame.init()
    size = w, h = (1280, 720)
    screen = pygame.display.set_mode(size)

    level_loader = LevelLoader(size, "test1")
    # mapmaker.main_board.debug_mode = True
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                size = w, h = screen.get_size()
                level_loader.set_screen_size(size, (level_loader.board.n, level_loader.board.m))
                level_loader.load_level(level_loader.current_level_name)

        level_loader.update()
        level_loader.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

