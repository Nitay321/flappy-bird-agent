import pygame as pg
from .window import Window
from .images_functions import Img

class DrawText:
    font_name = 'fonts/8-BIT WONDER.TTF'

    @staticmethod
    def draw_text(text, size, x, y, color):
        font = pg.font.Font(DrawText.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        Img.draw(text_surface, text_rect.x, text_rect.y)

    @staticmethod
    def draw_text_not_from_center(text, size, x, y, color):
        font = pg.font.Font(DrawText.font_name, size)
        text_surface = font.render(text, True, color)
        Img.draw(text_surface, x, y)

