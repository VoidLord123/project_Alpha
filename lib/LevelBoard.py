from lib.Board import Board

"""
Класс уровня. Имеет сохранения и загрузки в файлы .alphamap

"""


class LevelBoard(Board):
    # WORK IN PROGRESS
    def __init__(self, screen_size: tuple[int, int], offset_horizontal: int, offset_vertical: int):
        """
        Инициализирует клеточное поле, но не загружает его. Если его не загрузить использовать нельзя
        :param screen_size: Размер экрана
        :param offset_horizontal: Отступ по горизонтали
        :param offset_vertical: Отступ по вертикали
        """
        super().__init__(1, 1, screen_size, offset_horizontal, offset_vertical)

    def load(self, filename: str):
        with open(filename, encoding="utf-8", mode="r") as file:
            source = list(map(lambda x: x.strip("\n"), file))
            wh_string = source[0]
            source = source[1:]
            assert wh_string.startswith("size: ")
            wh_string = wh_string[6:]
            wh_string = wh_string.split(";")
            wh_string = list(map(int, wh_string))
            self.n = wh_string[0]
            self.m = wh_string[1]

    def save(self):
        pass


a = LevelBoard((1, 1), 0 ,0)
a.load("test.alphamap")
print(a.n, a.m)