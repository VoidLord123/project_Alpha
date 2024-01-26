import pygame

from lib.modules.LevelLoader import LevelLoader
from lib.modules.MainMenu import MainMenu
from lib.modules.MapMaker import MapMaker
from lib.constants import FPS


class Game:
    def __init__(self, window_size):
        self.window_size = window_size
        self.state = "menu"
        self.current_module = MainMenu(self.window_size, self)
        self.is_fullscreen = False
        self.screen = pygame.display.set_mode(window_size)
        self.running = True
        self.esc_mode = False
        self.clock = pygame.time.Clock()
        self.show_fps = True
        self.fps_font = pygame.font.Font("fonts/pixel_font2.ttf", 20)
        pygame.mixer.music.load("sounds/music.wav")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def toggle_fullscreen(self):
        if self.is_fullscreen:
            self.screen = pygame.display.set_mode(self.window_size)
            self.current_module.set_screen_size(self.window_size)
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.current_module.set_screen_size(self.screen.get_size())
        self.is_fullscreen = not self.is_fullscreen

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if (not self.esc_mode and event.type == pygame.MOUSEBUTTONDOWN and
                    self.state in ["mapmaker", "menu", "official_level", 'loader']):
                self.current_module.on_click(*event.pos)
            if self.state == "menu":
                self.current_module.update(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if self.state == "menu" and self.current_module.mode == "menu":
                    exit()
                else:
                    self.change_to_menu()
        if self.state == "menu":
            self.current_module.update_tick()
        else:
            self.current_module.update()
        self.current_module.render(self.screen)
        if self.show_fps:
            self.screen.blit(self.fps_font.render(str(self.clock.get_fps()), 1, "black"), (20, 20))
        pygame.display.flip()
        self.clock.tick(FPS)

    def change_to_mapmaker(self, level_name):
        self.current_module = MapMaker(self.screen.get_size(), level_name + ".alphamap")
        self.state = "mapmaker"

    def change_to_menu(self, mode="menu"):
        self.current_module = MainMenu(self.screen.get_size(), self)
        self.current_module.mode = mode
        self.state = "menu"

    def load_user_level(self, level_name):
        self.current_module = LevelLoader(self.screen.get_size(), "user_levels/" + level_name, True, self)
        self.state = "user_level"

    def start_official_game(self):
        with open("save", mode="r", encoding="utf-8") as file:
            self.current_module = LevelLoader(self.screen.get_size(), "main_levels/" + file.read(), False, self)
            self.state = "official_level"
