import pygame as pg
from related_to_menu.menu import Menu


class MainMenu(Menu):
    def __init__(self):
        text_lst = ['play', 'agent', 'options', 'credits', 'controls']
        number_of_text = len(text_lst)

        super().__init__(text_lst, number_of_text)

    def events(self, event, place):
        if event.type == pg.KEYDOWN:
            self.events_from_menu(event)
            if event.key == pg.K_RETURN:
                place += 1
        return place

    def draw(self):
        self.draw_by_given_text()
