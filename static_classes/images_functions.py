import pygame as pg
from .window import Window


class Img:

    @staticmethod
    def load(name):
        return pg.image.load(name).convert_alpha()

    @staticmethod
    def draw(img, x, y):
        Window.window.blit(img, (x, y))

    @staticmethod
    def resize(img, size):
        return pg.transform.scale(img, size)

    @staticmethod
    def flip(img, bool_val1, bool_val2):
        return pg.transform.flip(img, bool_val1, bool_val2)

