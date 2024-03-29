import os

import pygame

from lib.LevelBoard import LevelBoard
from lib.SpriteGroup import SpriteGroup
from lib.modules.MapMaker import MapMaker

"""
Тестирование и демонстрация класса MapMaker
"""


if __name__ == "__main__":

    pygame.init()
    level_name = "m2"
    next_level_name = "c6"
    n, m = 10, 10
    size = w, h = (1600, 900)
    if not os.path.exists(os.path.join("main_levels",
                                       level_name + ".alphamap")):
        level_board = LevelBoard((4000, 4000), 0, 0)
        level_board.rewrite_board(n, m, (4000, 4000))
        level_board.groups = {"player": SpriteGroup(),
                              "action": SpriteGroup(),
                              "collide": SpriteGroup()}
        level_board.save(f"./main_levels/{level_name}.alphamap")
        level_board.save_sprites(f"./main_levels/{level_name}.alphaspm")
    screen = pygame.display.set_mode(size)
    mapmaker = MapMaker(size, f"main_levels/{level_name}.alphamap")
    if not os.path.exists(f"main_levels/{level_name}.alphaextended"):
        with open(f"main_levels/{level_name}.alphaextended", mode="w", encoding="utf-8") as file:
            file.write(f"""preview_text: Some4
exits:
    exit1: main_levels/{next_level_name}""")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mapmaker.on_click(*event.pos)
        mapmaker.draw()
        screen.blit(mapmaker.screen, (0, 0))
        pygame.display.flip()
    pygame.quit()

