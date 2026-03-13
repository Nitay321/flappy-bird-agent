import pygame as pg
from static_classes.window import Window
from static_classes.images_functions import Img


class Score:
    def __init__(self):
        self.digits_images = {}
        self.number = 0
        self.digits = 1

        self.x = None
        self.y = None
        self.distance_between_numbers = None

        self.update_size()

    def load_and_resize_all_images(self):
        for i in range(10):
            img_name = 'images/' + str(i) + '.png'
            image = pg.image.load(img_name)
            if i == 1:
                self.digits_images[i] = Img.resize(image, (int((Window.relative_w(24))), Window.relative_h(54)))
            else:
                self.digits_images[i] = Img.resize(image, (Window.relative_w(36), Window.relative_h(54)))

    def update_size(self):
        self.load_and_resize_all_images()
        self.distance_between_numbers = Window.relative_w(36)  # 24*1.5

        self.x = Window.relative_w(240)
        self.y = Window.relative_h(60)

    def number_of_digits(self):
        val = self.number
        count = 1
        while val > 9:
            count += 1
            val //= 10
        return count

    def draw(self):
        self.digits = self.number_of_digits()
        val = self.number
        digit_number = val % 10

        self.x += (self.digits - 1) * (int(self.distance_between_numbers / 2))
        self.x -= int(self.digits_images[digit_number].get_width() / 2)

        for i in range(self.digits):
            Img.draw(self.digits_images[digit_number], self.x, self.y)
            val //= 10
            digit_number = val % 10
            if digit_number == 1:
                self.distance_between_numbers = Window.relative_w(24)
            else:
                self.distance_between_numbers = Window.relative_w(36)
            self.x -= self.distance_between_numbers

        self.x = Window.relative_w(240)
