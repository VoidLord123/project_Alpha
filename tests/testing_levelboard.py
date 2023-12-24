import pygame
from lib.LevelBoard import LevelBoard

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
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.get_cell(*event.pos):
                    a, b = board.get_cell(*event.pos)
                    board.board[b][a].change_state(0 if board.board[b][a].state == 1 else 1)
            if event.type == pygame.KEYDOWN:
                board.save("test2.alphamap")
        board.render(screen)
        pygame.display.flip()
    pygame.quit()

