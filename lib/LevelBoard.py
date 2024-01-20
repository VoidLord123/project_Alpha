import pygame.draw

from lib.Cell import Cell
from lib.constants import LINKS, SPRITES, GROUPS, BASIC_GROUPS, CLASS_NAME_TO_CLASS
from lib.Board import Board
from lib.SpriteGroup import SpriteGroup
from lib.entities.DialogSprite import DialogSprite

"""
Класс уровня. Имеет сохранения и загрузки в файлы .alphamap

"""


class LevelBoard(Board):
    def __init__(self, screen_size: tuple[int, int], offset_horizontal: int, offset_vertical: int, linked_loader=None):
        """
        Инициализирует клеточное поле, но не загружает его. Если его не загрузить использовать нельзя
        :param screen_size: Размер экрана
        :param offset_horizontal: Отступ по горизонтали
        :param offset_vertical: Отступ по вертикали
        """

        super().__init__(1, 1, screen_size, offset_horizontal, offset_vertical)
        self.linked_loader = linked_loader
        self.debug_mode = False  # режим отладки для простоты работы
        self.named_sprites = {}
        self.groups = {}
        self.all_sprites = SpriteGroup()
        sprite = DialogSprite(10, 10, 100, 100, 'Hi iii ww aass asss assdd lflkfkj dkllkfdf sd sdsdsds', pygame.font.Font("fonts/pixel_font2.ttf"), 1)
        self.all_sprites.add(sprite)

    def load(self, filename: str):
        with open(filename, encoding="utf-8", mode="r") as file:
            source = list(map(lambda x: x.strip("\n"), file))
            wh_string = source[0]
            source = source[1:]
            assert wh_string.startswith("size: ")
            wh_string = wh_string[6:]
            wh_string = wh_string.split(";")
            wh_string = list(map(int, wh_string))
            self.rewrite_board(*wh_string, self.screen_size)
            source = list(map(lambda x: x.split(";"), source))
            for i in range(self.m):
                for j in range(self.n):
                    self.board[i][j] = LINKS[source[i][j]]()

    def save(self, filename: str):
        with open(filename, mode="w", encoding="utf-8") as file:
            links_to_str = {}
            strs = LINKS.items()
            for i, j in strs:
                links_to_str[j] = i
            map_str = [f"size: {self.n}; {self.m}\n"]
            for i in self.board:
                map_str.append(";".join(map(lambda x: links_to_str[x.__class__], i)) + "\n")
                # Понимаю что данное решение не лучшее, но мне хочется разнести ячейки на отдельные классы
                # для возможности реализации что-то в конкретной ячейке или добавить разное поведение
                # для разных ячеек
            file.writelines(map_str)

    def load_sprites(self, filename):
        with open(filename, mode='r', encoding="utf-8") as file:
            info = file.readlines()
            info = list(map(lambda x1: x1.strip("\n").replace("    ", "$").replace("\t", "$"), info))
            info = info[1:]
            i = 0
            while info[i].startswith("$"):
                item = info[i]
                item = item[1:]
                item = item.split(": ")
                self.groups[item[0]] = GROUPS[item[1]]()
                i += 1
            i += 1
            while i < len(info) and info[i].startswith("$"):
                item = info[i]
                item = item[1:]
                item = item.split(": ")
                name = item[0]
                sprite_type = SPRITES[item[1]]
                i += 1
                item = info[i]
                x = float(item.split(": ")[1])
                i += 1
                item = info[i]
                y = float(item.split(": ")[1])
                x, y = self.get_cell_coord(x, y)
                i += 1
                item = info[i]
                vx = float(item.split(": ")[1])
                i += 1
                item = info[i]
                vy = float(item.split(": ")[1])
                i += 1
                item = info[i]
                state = int(item.split(": ")[1])
                groups = [self.all_sprites]
                i += 1
                item = info[i]
                while i < len(info) and info[i].startswith("$$"):
                    item = info[i]
                    groups.append(self.groups[item[2:]])
                    i += 1
                if name == "no-name":
                    sprite_type(x, y, vx, vy, self.cells_width, self.cells_height, *groups, state=state,
                                linked_levelboard=self)
                else:
                    self.named_sprites[name] = sprite_type(x, y, vx, vy, self.cells_width, self.cells_height,
                                                           *groups, state=state, linked_levelboard=self)
                    self.named_sprites[name].name = name  # name, name, name, name. Нужно для некоторых возможностей.

    def get_cell_float(self, x, y):
        x_new, y_new = x - self.offset_horizontal, y - self.offset_vertical
        if self.cells_width * self.n >= x_new >= 0 and self.cells_height * self.m >= y_new >= 0:
            return x_new / self.cells_width, y_new / self.cells_height
        return None

    def save_sprites(self, filename):
        with open(filename, mode='w', encoding="utf-8") as file:
            string = "groups:\n"
            grp_to_string = {}
            grp = GROUPS.items()
            for i, j in grp:
                grp_to_string[j] = i

            spr = SPRITES.items()
            spr_to_string = {}
            for i, j in spr:
                spr_to_string[j] = i

            for i, j in self.groups.items():
                string += f"    {i}: {grp_to_string[j.__class__]}\n"
            self_grp = self.groups.items()
            self_grp_to_string = {}
            for i, j in self_grp:
                self_grp_to_string[j] = i
            string += "sprites:\n"

            names_items = self.named_sprites.items()
            names = {}
            for i, j in names_items:
                names[j] = i
            n_of_exit = 1
            for i in self.all_sprites.sprites():
                if names.get(i, 'no-name') == "no-name" and  spr_to_string[i.__class__] == "exit":
                    names[i] = "exit" + str(n_of_exit)
                    n_of_exit += 1
                string += f"    {names.get(i, 'no-name')}: {spr_to_string[i.__class__]}\n"
                string += f"        x: {self.get_cell_float(i.rect.x, i.rect.y)[0]}\n"
                string += f"        y: {self.get_cell_float(i.rect.x, i.rect.y)[1]}\n"
                string += f"        vx: {i.vx}\n"
                string += f"        vy: {i.vy}\n"
                string += f"        state: {i.state}\n"
                for j in i.groups():
                    if self_grp_to_string.get(j, False):
                        string += "        " + self_grp_to_string.get(j) + "\n"
            file.write(string)

    def add_sprite(self, sprite):
        class_name = sprite.__class__.__name__
        group = BASIC_GROUPS[class_name]
        self.groups.setdefault(group, SpriteGroup())
        find = self.find_obj(sprite.rect.x, sprite.rect.y)
        if find:
            find[0].kill()
        sprite = CLASS_NAME_TO_CLASS[class_name](sprite.rect.x * self.cells_width + self.offset_horizontal,
                                                 sprite.rect.y * self.cells_height + self.offset_vertical, sprite.vx,
                                                 sprite.vy, self.cells_width, self.cells_height, self.all_sprites,
                                                 self.groups[BASIC_GROUPS[class_name]], state=sprite.state)

    def find_obj(self, x, y):
        find = list(filter(lambda z: (x * self.cells_width + self.offset_horizontal,
                                      y * self.cells_height + self.offset_vertical) == (z.rect.x, z.rect.y),
                           self.all_sprites.sprites()))
        return find

    def get_collide_objects(self):
        collide_list = []
        y = 0
        for i in self.board:
            x = 0
            for j in i:
                if j.is_collide:
                    a = j.get_image(self.cells_width, self.cells_height).get_rect()
                    a.x, a.y = self.get_cell_coord(x, y)
                    collide_list.append(a)
                x += 1
            y += 1

        return collide_list

    def get_collide_sprites(self):
        sprites = self.groups.get("collide", None)
        if sprites is not None:
            return sprites

    def get_player_sprites(self):
        sprites = self.groups.get("player", None)
        if sprites is not None:
            return sprites

    def get_action_sprites(self):
        sprites = self.groups.get("action", None)
        if sprites is not None:
            return sprites

    def render(self, screen):
        super().render(screen)
        self.all_sprites.draw(screen)

    def update(self, *args):
        self.all_sprites.update(*args)
