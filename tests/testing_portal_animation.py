import pygame
from lib.LevelBoard import LevelBoard
from lib.SpriteGroup import SpriteGroup

"""
Тестирование и демонстрация класса AnimationSprite
"""


if __name__ == "__main__":

    pygame.init()
    size = w, h = (1000, 1000)
    screen = pygame.display.set_mode(size)
    board = LevelBoard(size, 100, 100)
    board.load("test1.alphamap")
    board.load_sprites("test3.alphaspm")
    board.debug_mode = False
    running = True
    board.groups["collide"] = SpriteGroup()
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('black')
        board.all_sprites.update()
        board.render(screen)
        board.all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()
