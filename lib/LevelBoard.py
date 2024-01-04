from lib.constants import LINKS, SPRITES, GROUPS
from lib.Board import Board
from lib.SpriteGroup import SpriteGroup

"""
Класс уровня. Имеет сохранения и загрузки в файлы .alphamap

"""


class LevelBoard(Board):
    def __init__(self, screen_size: tuple[int, int], offset_horizontal: int, offset_vertical: int):
        """
        Инициализирует клеточное поле, но не загружает его. Если его не загрузить использовать нельзя
        :param screen_size: Размер экрана
        :param offset_horizontal: Отступ по горизонтали
        :param offset_vertical: Отступ по вертикали
        """
        super().__init__(1, 1, screen_size, offset_horizontal, offset_vertical)
        self.debug_mode = False  # режим отладки для простоты работы
        self.named_sprites = {}
        self.groups = {}
        self.all_sprites = SpriteGroup()

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
            pass

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
            for i in self.all_sprites.sprites():
                string += f"    {self.named_sprites.get(i, 'no-name')}: {spr_to_string[i.__class__]}\n"
                string += f"        x: {self.get_cell_float(i.rect.x, i.rect.y)[0]}\n"
                string += f"        y: {self.get_cell_float(i.rect.x, i.rect.y)[1]}\n"
                string += f"        vx: {i.vx}\n"
                string += f"        vy: {i.vy}\n"
                string += f"        state: {i.state}\n"
                for j in i.groups():
                    if self_grp_to_string.get(j, False):
                        string += "        " + self_grp_to_string.get(j) + "\n"
            file.write(string)