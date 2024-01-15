import pygame

from lib.SpriteGroup import SpriteGroup
from lib.entities.InputSprite import InputSprite


class Game:
    def __init__(self, screen_size: tuple[int, int]):
        self.state = 'mainmenu'
        self.screen = pygame.surface.Surface(screen_size)
        self.changed_fullscreen = False
        self.last_size = (0, 0)
        self.sprite_group = SpriteGroup()
        self.change_size(screen_size)

    def draw_text(self, text, color, coord, size):
        font = pygame.font.Font("fonts/pixel_font2.ttf", size)
        text1 = font.render(text, 1, color)
        # coord1_source = self.main_board.get_cell_coord(*coord)
        # coord1 = ((self.main_board.cells_width * 4 - text1.get_width()) // 2 + coord1_source[0],
        #           (self.main_board.cells_height - text1.get_height()) // 2 + coord1_source[1])
        self.screen.blit(text1, coord)

    def change_size(self, size, mode=pygame.RESIZABLE):
        if self.changed_fullscreen:
            mode = pygame.RESIZABLE
            size = self.last_size
            self.changed_fullscreen = not self.changed_fullscreen
        if mode is pygame.FULLSCREEN:
            self.last_size = self.screen.get_size()
            self.changed_fullscreen = not self.changed_fullscreen
        self.screen = pygame.display.set_mode(size, mode)
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

    def on_click(self, pos):
        x, y = pos

        if int(self.width / 10 * 9) <= x <= int(self.width / 20 * 19) and 0 <= y <= self.width // 20:
            self.sprite_group.sprites()[0].kill()
            self.state = 'main_menu'
        elif int(self.width / 20 * 19) <= x <= self.width and 0 <= y <= self.width // 20:
            self.change_size((0, 0), pygame.FULLSCREEN)
        elif 0 <= x <= 100 and 0 <= y <= 100:
            #Это затычка для теста
            self.state = 'game_over'
        elif 100 <= x <= 200 and 0 <= y <= 100:
            #Это затычка для теста
            self.state = 'create_level'

        if self.state == 'main_menu':
            self.on_click_main_menu(pos)
        elif self.state == 'redact_level':
            pass
        elif self.state == 'info':
            pass
        elif self.state == 'mapmaker':
            pass

    def on_click_main_menu(self, pos):
        x, y = pos
        if (x, y) in [(x + 12, y + 8) for x in range(8) for y in range(1)]:
            #Тут называй как хочешь
            self.state = 'level1'
        elif (x, y) in [(x + 11, y + 11) for x in range(10) for y in range(1)]:
            self.state = 'create_level'
        elif (x, y) in [(x + 11, y + 11) for x in range(10) for y in range(1)]:
            self.state = 'redact_level'
        elif int(self.width / 20 * 17) <= x <= int(self.width / 10 * 9) and 0 <= y <= self.width // 20:
            self.state = 'info'

    def on_click_create_level(self, pos):
        x, y = pos
        if (x, y) in [(x + 12, y + 8) for x in range(8) for y in range(1)]:
            pass

    def draw(self):
        if self.state == 'main_menu':
            self.draw_main_menu()
        elif self.state == 'redact_level':
            pass
        elif self.state == 'info':
            self.draw_info()
        elif self.state == 'mapmaker':
            pass
        elif self.state == 'game_over':
            self.draw_game_over()
        elif self.state == 'create_level':
            input_sprite = InputSprite((self.width - self.width * 2 // 3) // 2, self.height // 2,
                                       pygame.font.Font("fonts/pixel_font2.ttf", self.width // 10), 10, 2, self.sprite_group)
            self.draw_create_level()

        pygame.draw.rect(self.screen, "white",
                         pygame.rect.Rect(int(self.width / 20 * 19), 0, self.width // 20, self.width // 20), 2)
        pygame.draw.rect(self.screen, "white",
                         pygame.rect.Rect(int(self.width / 20 * 18), 0, self.width // 20, self.width // 20), 2)

    def draw_main_menu(self):
        #Оставляю работу с координатами на тебя, я уже замучисля их выставлять. Не забудь потом их добавить в проверку клика.

        self.screen.fill('black')
        self.draw_text("Главное меню", "white", (self.width // 6, self.height // 100), self.width // 10)
        self.draw_text("Начать игру", "white", ((self.width - self.width // 32 * 11) // 2, self.height // 3), self.width // 20)
        self.draw_text("Создать уровень", "white", ((self.width - self.width // 32 * 11) // 2, self.height // 2), self.width // 20)
        self.draw_text("Редактировать уровень", "white", ((self.width - self.width // 32 * 11) // 2, self.height // 3 * 2), self.width // 20)

        pygame.draw.rect(self.screen, "white", pygame.rect.Rect((self.width - self.width // 32 * 11) // 2 - self.width // 100, self.height // 3, self.width // 20 * 6 + self.width // 40, self.height // 20 * 6 // 4 + self.height // 40), 2)
        pygame.draw.rect(self.screen, "white", pygame.rect.Rect((self.width - self.width // 32 * 11) // 2 - self.width // 100, self.height // 2, self.width // 20 * 6 + self.width // 40, self.height // 20 * 6 // 4 + self.height // 40), 2)
        pygame.draw.rect(self.screen, "white", pygame.rect.Rect((self.width - self.width // 32 * 11) // 2 - self.width // 100, self.height // 3 * 2, self.width // 20 * 6 + self.width // 40, self.height // 20 * 6 // 4 + self.height // 40), 2)
        pygame.draw.rect(self.screen, "white",
                         pygame.rect.Rect(int(self.width / 20 * 17), 0, self.width // 20, self.width // 20), 2)

    def draw_info(self):
        self.screen.fill('black')
        self.draw_text("Информация", "white", (self.width // 6 // 10 * 12, self.height // 100), self.width // 10)

    def draw_game_over(self):
        self.screen.fill('black')
        self.draw_text("Вы погибли", "white", (self.width // 6 // 10 * 12, self.height // 100), self.width // 10)
        self.draw_text("Вернитесь в главное меню", "white", (self.width // 6 // 26 * 23, self.height // 3), self.width // 20)

    def draw_create_level(self):
        self.screen.fill('black')
        self.draw_text("Введите название файла с уровнем", "white", (self.width // 20, self.height // 10), self.width // 20)
        self.sprite_group.update()
        self.sprite_group.draw(self.screen)

