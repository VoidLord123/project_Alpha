from lib.Sprite import Sprite
import pygame


class DialogSprite(Sprite):
    def __init__(self, x, y, w, h, text, font: pygame.font.Font, border, *group, color="black"):
        super().__init__(x, y, 0, 0, 0, 0, *group)
        self.color = color
        self.font = font
        self.border = border
        self.w = w
        self.h = h
        self.text = text
        self.size = (w, h)
        self.image = self.dialog()

    def dialog(self):
        lines = []
        split_text = self.text.split()
        temp_line = []
        for word in split_text:
            new_size = self.count_text_size(' '.join(temp_line + [word]))
            if self.w >= new_size[0]:
                temp_line.append(word)
            else:
                lines.append(' '.join(temp_line))
                temp_line = [word]
        if temp_line:
            lines.append(' '.join(temp_line))
        y_sep = self.count_text_size(lines[-1])[1]
        yy = 0
        image = pygame.surface.Surface((self.w, self.h))
        image.fill("white")
        for line in lines:
            size = self.count_text_size(line)
            text_image = self.font.render(line, 1, 'black')
            image.blit(text_image, (self.border * 2, yy + self.border * 2))
            yy += y_sep + 5
        if self.border > 0:
            pygame.draw.rect(image, self.color, (0, 0, *self.size), self.border)
        return image

    def count_text_size(self, text):
        image = self.font.render(text, 1, 'black')
        if self.border > 0:
            return image.get_width() + 4 * self.border, image.get_height() + self.border * 4
        return image.get_size()

    def update(self, *args):
        self.image = self.dialog()
