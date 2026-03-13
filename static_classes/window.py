import pygame as pg
from random import randint


class Window:
    WIDTH = 480
    HEIGHT = 600
    BASE_HEIGHT = 60
    window = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)

    @staticmethod
    def init_window():
        pg.init()
        pg.display.set_caption('flappy bird')

    @staticmethod
    def update_size_window(w, h):
        Window.WIDTH = w
        Window.HEIGHT = h
        Window.window = pg.display.set_mode((w, h), pg.RESIZABLE)

    @staticmethod
    def get_random_number_for_pipe(space_in_pipe):
        extreme_point = Window.relative_h(100)
        return randint(extreme_point, Window.HEIGHT - Window.BASE_HEIGHT - space_in_pipe - extreme_point)
    # (100, 600 - 75 - 180 - 100

    @staticmethod
    def get_random_number_for_bird():
        extreme_point = Window.relative_h(150)
        return randint(extreme_point, Window.HEIGHT - Window.BASE_HEIGHT - extreme_point)

    # (100, 600 - 75 - 180 - 100

    @staticmethod
    def relative_w(w):
        orignal_w = 480
        return int(Window.WIDTH / (orignal_w / w))

    @staticmethod
    def relative_h(h):
        orignal_h = 600
        return int(Window.HEIGHT / (orignal_h / h))

    @staticmethod
    def limit_w(w):
        if w < 300:
            return 300

        if w > 4999:
            return 5000
        return w

    @staticmethod
    def limit_h(h):
        if h < 400:
            return 400

        if h > 4999:
            return 5000

        return h
