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
        fps = clock.get_fps()
        game.screen.blit(font.render(str(round(fps, 2)), 0, "white"), (10, 10))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
