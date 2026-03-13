import pygame as pg
from static_classes.window import Window
from static_classes.images_functions import Img
from random import randint


def create_bird_flap_images(name):
    img = Img.load('images/' + name + '.png').convert_alpha()
    w, h = 62, 52
    img = Img.resize(img, (Window.relative_w(w), Window.relative_h(h)))
    return img


class Bird:
    def __init__(self):

        self.current_image_index = 0

        self.rect = None
        self.min_y = None
        self.max_y = None
        self.bird_frames = None
        self.image = None

        self.start_y = None

        self.update_size()

        self.vy = None
        self.speed = None

        self.state = None

        self.rotate = None

    def update_size(self):
        bird_downflap = create_bird_flap_images('yellowbird-downflap')
        bird_midflap = create_bird_flap_images('yellowbird-midflap')
        bird_upflap = create_bird_flap_images('yellowbird-upflap')
        self.bird_frames = [bird_downflap, bird_midflap, bird_upflap]
        self.image = self.bird_frames[self.current_image_index]

        self.start_y = Window.relative_h(300)

        try:
            x, y = self.rect.x, self.rect.y
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = Window.relative_w(x), Window.relative_h(y)
        except AttributeError:
            self.rect = self.image.get_rect()

        self.rect.centerx = Window.relative_w(240)

    def min_y_and_max_y(self):  # for movement at start
        self.min_y = self.rect.y
        self.max_y = self.rect.y + 40

    def fall(self):
        if self.vy <= (Window.HEIGHT / 120):
            self.vy += 108 / Window.HEIGHT
        self.convert_vy_to_speed()

    def jump(self):
        self.vy = -Window.HEIGHT / 130.43
        self.convert_vy_to_speed()

    def is_on_ground(self):
        return (Window.HEIGHT - Window.BASE_HEIGHT) <= self.rect.bottomright[1]

    def death_movement(self):
        if not self.is_on_ground():
            if self.vy <= (Window.HEIGHT / 120):
                self.vy += 108 / Window.HEIGHT
            self.rect.y += self.vy
        else:
            vx = 2
            if self.rect.bottomright[0] > 0:
                self.rect.x -= vx

    def starting_movement(self):
        if self.rect.y > self.max_y:
            self.vy = -1

        elif self.rect.y < self.min_y:
            self.vy = 1

        self.rect.y += self.vy

    def convert_vy_to_speed(self):
        last_rect_y = self.rect.y
        self.rect.y += self.vy
        self.speed = self.rect.y - last_rect_y

    def draw(self):
        if self.rotate:
            new_image = self.rotate_bird()
            Img.draw(new_image, self.rect.x, self.rect.y)
        else:
            Img.draw(self.image, self.rect.x, self.rect.y)

    def is_collided_with(self, pipe):
        if pipe.rect_up.x <= self.rect.x <= pipe.rect_up.bottomright[0]:
            if self.rect.y <= pipe.rect_up.bottomright[1] or self.rect.bottomright[1] >= pipe.rect_down.y:
                return True
        if pipe.rect_up.x <= self.rect.bottomright[0] <= pipe.rect_up.topright[0]:
            if self.rect.y <= pipe.rect_up.bottomright[1] or self.rect.bottomright[1] >= pipe.rect_down.y:
                return True

        if self.rect.bottomright[1] <= 0:
            if self.rect.topright[0] >= pipe.rect_up.x:
                return True

        return False

    def rotate_bird(self):
        new_img = pg.transform.rotozoom(self.image, -self.vy * 10, 1)
        return new_img

    def animation(self):
        self.image = self.bird_frames[self.current_image_index]
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
