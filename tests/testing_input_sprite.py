import pygame
from lib.SpriteGroup import SpriteGroup
from lib.entities.InputSprite import InputSprite

"""
Тестирование и демонстрация класса LevelBoard
"""


if __name__ == "__main__":

    pygame.init()
    size = w, h = (700, 700)
    screen = pygame.display.set_mode(size)
    running = True

    group = SpriteGroup()
    tst_sprite = InputSprite(pygame.font.Font("fonts/pixel_font2.ttf", 40), 28, 0, group, color="violet")
    tst_sprite.rect.x = 10
    tst_sprite.rect.y = 100
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            group.update(event)
        group.draw(screen)
        pygame.display.flip()
    pygame.quit()
