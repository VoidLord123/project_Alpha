import pygame
from lib.LevelBoard import LevelBoard
from lib.SpriteGroup import SpriteGroup
from lib.entities.PlayerSprite import PlayerSprite

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
    group = SpriteGroup()
    player = PlayerSprite(300, 500, 0, 0, 100, 100, group)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.get_cell(*event.pos):
                    a, b = board.get_cell(*event.pos)
                    board.board[b][a].change_state(0 if board.board[b][a].state == 1 else 1)
        screen.fill('black')
        group.update()
        board.render(screen)
        group.draw(screen)
        pygame.display.flip()
    pygame.quit()
