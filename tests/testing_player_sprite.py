import pygame
from lib.LevelBoard import LevelBoard
from lib.SpriteGroup import SpriteGroup
from lib.entities.PlayerSprite import PlayerSprite
from lib.entities.TestSprites import TestSprite1

"""
Тестирование и демонстрация класса LevelBoard
"""


if __name__ == "__main__":

    pygame.init()
    size = w, h = (1000, 1000)
    screen = pygame.display.set_mode(size)
    board = LevelBoard(size, 100, 100)
    board.load("test1.alphamap")
    board.debug_mode = False
    running = True
    board.groups["collide"] = SpriteGroup()
    player = PlayerSprite(300, 100, 0, 0, board.cells_width, board.cells_height, board.all_sprites,
                          linked_levelboard=board)
    player.scale()
    r = player.rect.copy()
    r.x = 0
    r.y = 0
    pygame.draw.rect(player.image, "red", r, 1)
    TestSprite1(500, 300, 0, 0, board.cells_width, board.cells_height, board.all_sprites, board.groups["collide"])
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
