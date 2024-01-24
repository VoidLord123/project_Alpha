from lib.Sprite import Sprite
import pygame


class DialogSprite(Sprite):
    def __init__(self, x, y, w, h, text, font, max_len, border, *group, color="black"):
        super().__init__(x, y, 0, 0, 0, 0, *group)
        self.color = color
        self.font = font
        self.border = border
        self.w_sep = w // 100
        self.h_sep = h // 100
        self.w = w - self.w_sep * 2
        self.h = h - self.h_sep * 2
        self.text = text
        self.size = (w, h)
        self.image = self.dialog()
        self.change_image = False
        self.scale_to_height()

    def dialog(self):
        lines = []
        split_text = self.text.split()
        temp_line = []
        for word in split_text:
            new_size = self.count_text_size(' '.join(temp_line + [word]))
            if self.w < new_size[0] or word.endswith('\\n'):
                if word.endswith('\\n'):
                    temp_line.append(word.replace('\\n', ''))
                lines.append(' '.join(temp_line))
                if word.endswith('\\n'):
                    temp_line = []
                else:
                    temp_line = [word]
            elif self.w >= new_size[0]:
                temp_line.append(word)
        if temp_line:
            lines.append(' '.join(temp_line))
        y_sep = self.count_text_size(lines[-1])[1]
        yy = 0
        image = pygame.surface.Surface((self.w, self.h))
        image.fill("white")
        for line in lines:
            size = self.count_text_size(line)
            text_image = self.font.render(line, 1, 'black')
            image.blit(text_image, (self.border * 2 + self.w_sep, yy + self.border * 2 + self.h_sep))
            yy += y_sep + 5
        if self.border > 0:
            pygame.draw.rect(image, self.color,
                             (0, 0, self.size[0] - self.w_sep * 2, self.size[1] - self.h_sep * 2), self.border)
        return image

    def count_text_size(self, text):
        image = self.font.render(text, 1, 'black')
        if self.border > 0:
            return image.get_width() + self.border * 8, image.get_height() + self.border * 8
        return image.get_size()

    def update(self, *args):
        if self.change_image:
            self.image = self.dialog()
            self.scale_to_height()
            self.change_image = False

    def scale_to_height(self):
        new_image = pygame.transform.scale(self.image, (self.image.get_width() / self.image.get_height() *
                                                        self.h,
                                                        self.h))
        self.image = new_image

    def set_text(self, text):
        self.text = text
        self.change_image = True
