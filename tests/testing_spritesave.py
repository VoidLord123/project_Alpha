import pygame
from lib.LevelBoard import LevelBoard
from lib.entities.TestSprites import TestGroup1, TestSprite1
"""
Тестирование и демонстрация сохранений спрайтов
"""


if __name__ == "__main__":

    pygame.init()
    size = w, h = (1000, 1000)
    screen = pygame.display.set_mode(size)
    board = LevelBoard(size, 100, 100)
    board.load("test1.alphamap")
    board.debug_mode = False
    board.groups["test"] = TestGroup1()
    board.named_sprites["tst"] = TestSprite1(200, 200, 0, 0, board.groups["test"], board.all_sprites)
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
                board.save_sprites("test2.alphaspm")
        board.render(screen)
        board.all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
