from lib.Sprite import Sprite
import pygame


class InputSprite(Sprite):
    def __init__(self, x, y, font: pygame.font.Font, max_len, border, *group, standard_symbol="A", height,
                 color="black"):
        super().__init__(x, y, 0, 0, 0, 0, *group)
        self.height = height
        self.color = color
        self.standard_symbol = standard_symbol
        self.max_len = max_len
        self.font = font
        self.border = border
        self.text = ""
        self.size = self.count_size()
        self.image = self.generate_image()
        self.scale_to_height()

    def update(self, *args):
        text_prev = self.text
        if not args:
            return
        i = args[0]
        if i.type == pygame.KEYDOWN:
            if i.key != pygame.K_BACKSPACE and len(self.text) < self.max_len:
                self.text += i.unicode
            elif i.key == pygame.K_BACKSPACE and len(self.text) > 0:
                self.text = self.text[:-1]

        if text_prev != self.text:
            self.image = self.generate_image()
            self.scale_to_height()

    def generate_image(self):
        text_image = self.font.render(self.text, 1, self.color)
        image = pygame.surface.Surface(self.size)
        image.fill("white")
        image.blit(text_image, (self.border * 2, self.border * 2))
        if self.border > 0:
            pygame.draw.rect(image, self.color, (0, 0, *self.size), self.border)
        return image

    def count_size(self):
        image = self.font.render(self.standard_symbol * self.max_len, 1, self.color)
        if self.border > 0:
            return image.get_width() + 4 * self.border, image.get_height() + self.border * 4
        return image.get_size()

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def scale_to_height(self):
        new_image = pygame.transform.scale(self.image, (self.image.get_width() / self.image.get_height() * self.height,
                                                        self.height))
        self.image = new_image
