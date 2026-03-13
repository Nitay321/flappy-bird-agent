import pygame as pg
from static_classes.window import Window
from static_classes.draw_text import DrawText


class Menu:
    def __init__(self, text_lst=None, number_of_text=None):

        self.ORANGE = (247, 109, 1)
        self.BLUE = (60, 80, 200)

        self.x = None
        self.y = None
        self.size = None
        self.space_h = None

        self.update_size_from_menu()

        self.the_chosen_category = 0
        self.text_lst = text_lst
        self.number_of_text = number_of_text

    def update_size_from_menu(self):
        self.x = Window.relative_w(240)
        self.y = Window.relative_h(125)
        self.size = Window.relative_h(33)
        self.space_h = Window.relative_h(76)

    def forward_key(self):
        self.the_chosen_category = (self.the_chosen_category + 1) % self.number_of_text

    def backwards_key(self):
        self.the_chosen_category = (self.the_chosen_category - 1) % self.number_of_text

    def events_from_menu(self, event):
        if event.key == pg.K_DOWN:
            self.forward_key()
        elif event.key == pg.K_UP:
            self.backwards_key()

    def draw_by_given_text(self):
        for i in range(self.number_of_text):
            if self.the_chosen_category == i:
                DrawText.draw_text(self.text_lst[i], self.size, self.x, self.y + i * self.space_h, self.BLUE)
            else:
                DrawText.draw_text(self.text_lst[i], self.size, self.x, self.y + i * self.space_h, self.ORANGE)
