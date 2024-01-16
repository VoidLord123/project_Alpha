import pygame

from lib.Board import Board
from lib.SpriteGroup import SpriteGroup
from lib.entities.InputSprite import InputSprite
import os
from lib.LevelBoard import LevelBoard


class MainMenu:
    def __init__(self, screen_size, linked_game=None):
        self.linked_game = linked_game
        self.screen = None
        self.screen_size = screen_size
        self.horizontal_offset = 0
        self.vertical_offset = 0
        self.set_screen_size(screen_size)
        self.board = Board(32, 18, screen_size, self.horizontal_offset, self.vertical_offset)
        self.mode = "menu"
        self.all_sprites = SpriteGroup()
        self.level_name = ""
        self.tick = 0

    def draw_text(self, text, color, coord, height, rect=False, alpha=255):
        text1 = self.get_text_image(text, color, height, rect)
        dx, dy = text1.get_width() / self.board.cells_width / 2, text1.get_height() / self.board.cells_height / 2
        coord = (coord[0] - dx, coord[1] - dy)
        text1.set_alpha(alpha)
        self.screen.blit(text1, self.board.get_cell_coord(*coord))

    def get_rect_by_text(self, text, color, coord, height, rect=False):
        text1 = self.get_text_image(text, color, height, rect)
        dx, dy = text1.get_width() / self.board.cells_width / 2, text1.get_height() / self.board.cells_height / 2
        rect = text1.get_rect()
        coord = (coord[0] - dx, coord[1] - dy)
        rect = rect.move(self.board.get_cell_coord(*coord))
        return rect

    def set_screen_size(self, screen_size):
        self.screen_size = screen_size
        self.vertical_offset = 0
        self.horizontal_offset = 0
        if round(screen_size[0] / screen_size[1], 2) != round(16 / 9, 2) and 16 / 9 <= \
                screen_size[0] / screen_size[1]:
            self.horizontal_offset = screen_size[0] - round(self.screen_size[1] / 9 * 16)
            self.horizontal_offset //= 2
        elif screen_size[0] / screen_size[1] <= 16 / 9:
            self.vertical_offset = screen_size[1] - round(self.screen_size[0] / 16 * 9)
            self.vertical_offset //= 2
        else:
            self.horizontal_offset = 0
            self.vertical_offset = 0
        self.screen = pygame.surface.Surface(screen_size)
        try:
            self.board.set_view(screen_size, self.horizontal_offset, self.vertical_offset)
        except Exception:
            pass

    def update(self, *args):
        self.all_sprites.update(*args)

    def get_text_image(self, text, color, height, rect=False):
        font = pygame.font.Font("fonts/pixel_font2.ttf", 128)
        text1 = font.render(text, 1, color)
        text1 = pygame.transform.scale(text1, ((text1.get_width() / text1.get_height() * height), height))
        if not rect:
            return text1
        dx, dy = round(self.board.cells_width * 0.1), round(self.board.cells_height * 0.1)
        image = pygame.surface.Surface((round(text1.get_width() + dx * 2), round(text1.get_height() + dy * 2)))
        pygame.draw.rect(image, color, (0, 0, image.get_width(), image.get_height()), 1 if dx // 4 == 0 else dx // 4)
        image.blit(text1, (round(dx), round(dy)))
        return image

    def update_tick(self):
        if self.tick > 0:
            self.tick -= 1

    def draw(self):
        self.screen.fill("black")
        self.board.render(self.screen)
        if self.mode == "menu":
            self.draw_text("Главное меню", "white", (16, 2), self.board.cells_height * 3)
            self.draw_text("Начать игру", "white", (16, 7), self.board.cells_height * 1, True)
            self.draw_text("Создатель уровней", "white", (16, 8.5), self.board.cells_height, True)
            self.draw_text("Загрузить уровень", "white", (16, 10), self.board.cells_height, True)
            self.draw_text("info", "white", (30.5, 17), self.board.cells_height, True),
            self.draw_text("full-screen", "white", (3.25, 17), self.board.cells_height, True)
        elif self.mode == "info":
            self.draw_text("Справка по проекту Альфа", "white", (16, 2), self.board.cells_height)
            self.draw_text("Управление стрелками, порталы проход в следующий уровень", "white",
                           (16, 4), self.board.cells_height)
            self.draw_text("Escape - выход в главное меню. Escape в главном меню выход из игры", "white",
                           (16, 5), self.board.cells_height * 0.75)
            self.draw_text("Рекомендуется играть в полноэкранном режиме", "white", (16, 6), self.board.cells_height)
            self.draw_text("Создатели:", "white", (16, 7), self.board.cells_height)
            self.draw_text("Калинин Иван(VoidLord)", "white", (16, 9), self.board.cells_height)
            # Я убрал убогую подпись 123 которая в моем гите чисто потому что оригинальный ник занят был(
            self.draw_text("Галюшин Ярослав(D4rkSn0w)", "white", (16, 10), self.board.cells_height)
            self.draw_text("Назад", "white", (16, 16), self.board.cells_height, True)
        elif self.mode == "creating1":
            self.draw_text("Введите имя уровня", "white", (16, 5), self.board.cells_height)
            self.draw_text("Далее", "white", (16, 10), self.board.cells_height, True)
            if self.tick > 0:
                self.draw_text("Ошибка! Введена пустая строка!", "red", (16, 12),
                               self.board.cells_height, alpha=self.tick)
        elif self.mode == "creating2":
            self.draw_text("Введите сторону квадрата в клетках", "white", (16, 5), self.board.cells_height)
            self.draw_text("Далее", "white", (16, 10), self.board.cells_height, True)
            if self.tick > 0:
                self.draw_text("Ошибка! Введено не число или некорректное число!", "red", (16, 12),
                               self.board.cells_height, alpha=self.tick)
        elif self.mode == "load":
            self.draw_text("Введите имя уровня", "white", (16, 5), self.board.cells_height)
            self.draw_text("Далее", "white", (16, 10), self.board.cells_height, True)
            if self.tick > 0:
                self.draw_text("Ошибка! Введена пустая строка или уровень не найден!", "red", (16, 12),
                               self.board.cells_height, alpha=self.tick)
        elif self.mode == "endgame":
            self.draw_text("Поздравляем! Вы сбежали из симуляции!", "white", (16, 3), self.board.cells_height * 1.5)
            self.draw_text("Спасибо за прохождение!", "white", (16, 5), self.board.cells_height)
            self.draw_text("Вы можете сбросить сохранение или сразу вернуться в главное меню", "white",
                           (16, 7), self.board.cells_height)
            self.draw_text("Выйти", "white", (12, 9), self.board.cells_height, True)
            self.draw_text("Сбросить", "white", (20, 9), self.board.cells_height, True)

        self.all_sprites.draw(self.screen)

    def on_click(self, x, y):
        actions = {}
        if self.mode == "menu":
            actions = {
                "start": self.get_rect_by_text("Начать игру", "white", (16, 7), self.board.cells_height, True),
                "maker": self.get_rect_by_text("Создатель уровней", "white", (16, 8.5), self.board.cells_height, True),
                "load": self.get_rect_by_text("Загрузить уровень", "white", (16, 10), self.board.cells_height, True),
                "info": self.get_rect_by_text("info", "white", (30.5, 17), self.board.cells_height, True),
                "full-screen": self.get_rect_by_text("full-screen", "white", (3.25, 17), self.board.cells_height, True)
            }
        elif self.mode == "info":
            actions = {
                "back": self.get_rect_by_text("Назад", "white", (16, 16), self.board.cells_height, True)
            }
        elif self.mode == "creating1":
            actions = {
                "next1": self.get_rect_by_text("Далее", "white", (16, 10), self.board.cells_height, True)
            }
        elif self.mode == "creating2":
            actions = {
                "next2": self.get_rect_by_text("Далее", "white", (16, 10), self.board.cells_height, True)
            }
        elif self.mode == "load":
            actions = {
                "next3": self.get_rect_by_text("Далее", "white", (16, 10), self.board.cells_height, True)
            }
        elif self.mode == "endgame":
            actions = {
                "return": self.get_rect_by_text("Выйти", "white", (12, 9), self.board.cells_height, True),
                "reset": self.get_rect_by_text("Сбросить", "white", (20, 9), self.board.cells_height, True)
            }
        for i in actions.keys():
            if actions[i].collidepoint(x, y):
                if i == "start":
                    self.linked_game.start_official_game()
                elif i == "maker":
                    font = pygame.font.Font("fonts/pixel_font2.ttf", 25)
                    cx, cy = self.board.get_cell_coord(11.75, 7)
                    InputSprite(cx, cy, font, 20, 1, self.all_sprites, height=self.board.cells_height)
                    self.mode = "creating1"

                elif i == "load":
                    font = pygame.font.Font("fonts/pixel_font2.ttf", 25)
                    cx, cy = self.board.get_cell_coord(11.75, 7)
                    InputSprite(cx, cy, font, 20, 1, self.all_sprites, height=self.board.cells_height)
                    self.mode = "load"
                elif i == "info":
                    self.mode = "info"
                elif i == "full-screen":
                    if self.linked_game:
                        self.linked_game.toggle_fullscreen()
                elif i == "back":
                    self.mode = "menu"
                elif i == "next1":
                    if self.all_sprites.sprites()[0].get_text() != "":
                        self.level_name = self.all_sprites.sprites()[0].get_text()

                        if not os.path.exists(os.path.join("user_levels",
                                                           self.all_sprites.sprites()[0].get_text() + ".alphamap")):
                            self.all_sprites = SpriteGroup()
                            self.mode = "creating2"
                            font = pygame.font.Font("fonts/pixel_font2.ttf", 25)
                            cx, cy = self.board.get_cell_coord(15.5, 7)
                            InputSprite(cx, cy, font, 2, 1, self.all_sprites, height=self.board.cells_height)
                        else:
                            self.linked_game.change_to_mapmaker(os.path.join(
                                "user_levels", self.all_sprites.sprites()[0].get_text()))
                    else:
                        self.tick = 255
                elif i == "next2":
                    try:
                        n = int(self.all_sprites.sprites()[0].get_text())
                        assert n > 0
                        if not os.path.exists(os.path.join("user_levels",
                                                           self.all_sprites.sprites()[0].get_text() + ".alphamap")):
                            level_board = LevelBoard((4000, 4000), 0, 0)
                            level_board.rewrite_board(n, n, (4000, 4000))
                            level_board.groups = {"player": SpriteGroup(),
                                                  "action": SpriteGroup(),
                                                  "collide": SpriteGroup()}
                            level_board.save(f"./user_levels/{self.level_name}.alphamap")
                            level_board.save_sprites(f"./user_levels/{self.level_name}.alphaspm")
                            self.linked_game.change_to_mapmaker(os.path.join(
                                "user_levels", self.level_name))
                    except Exception as e:
                        self.tick = 255
                        print(e)

                elif i == "next3":
                    text = self.all_sprites.sprites()[0].get_text()
                    if not os.path.exists(os.path.join("user_levels", text + ".alphamap")) or text == "":
                        self.tick = 255
                    else:
                        self.linked_game.load_user_level(text)
                elif i == "return":
                    self.mode = "menu"
                elif i == "reset":
                    with open("save", mode="w", encoding="utf-8") as file:
                        file.write("test1")

    def render(self, screen):
        self.draw()
        screen.blit(self.screen, (0, 0))
