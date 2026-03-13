import pygame as pg
from related_to_menu.menu import Menu
from static_classes.window import Window


class ControlsMenu(Menu):
    def __init__(self):
        text_lst = ['esc', 'game', 'agent', 'menu']
        number_of_text = len(text_lst)

        super().__init__(text_lst, number_of_text)

        self.esc = Esc()
        self.game_in_controls = GameInControls()
        self.agent_in_controls = AgentInControls()
        self.menu_in_controls = MenuInControls()

    def events(self, event, place):
        if event.type == pg.KEYDOWN:
            self.events_from_menu(event)
            if event.key == pg.K_ESCAPE:
                place -= 1
            elif event.key == pg.K_RETURN:
                place += 1
        return place

    def draw(self):
        self.draw_by_given_text()


class Esc(Menu):
    def __init__(self):

        text_lst = ['esc', 'going back']
        number_of_text = len(text_lst)

        super().__init__(text_lst, number_of_text)

        self.update_size()

    def update_size(self):
        self.update_size_from_menu()
        self.size = Window.relative_h(27)
        self.space_h = Window.relative_h(55)

    def events(self, event, place):
        if event.type == pg.KEYDOWN:
            self.events_from_menu(event)
            if event.key == pg.K_ESCAPE:
                place -= 1
        return place

    def draw(self):
        self.draw_by_given_text()


class GameInControls(Menu):
    def __init__(self):
        text_lst = ['jump', 'button space']
        number_of_text = len(text_lst)

        super().__init__(text_lst, number_of_text)

        self.update_size()

    def update_size(self):
            self.update_size_from_menu()
            self.size = Window.relative_h(23)
            self.space_h = Window.relative_h(55)

    def events(self, event, place):
        if event.type == pg.KEYDOWN:
            self.events_from_menu(event)
            if event.key == pg.K_ESCAPE:
                place -= 1
        return place

    def draw(self):
        self.draw_by_given_text()


class AgentInControls(Menu):
    def __init__(self):
        super().__init__()

        text_lst = ['s show', 'r record', 'enter save']
        number_of_text = len(text_lst)

        super().__init__(text_lst, number_of_text)

        self.update_size()
    def update_size(self):
        self.update_size_from_menu()
        self.size = Window.relative_h(25)
        self.space_h = Window.relative_h(50)

    def events(self, event, place):
        if event.type == pg.KEYDOWN:
            self.events_from_menu(event)
            if event.key == pg.K_ESCAPE:
                place -= 1
        return place

    def draw(self):
        self.draw_by_given_text()


class MenuInControls(Menu):
    def __init__(self):
        super().__init__()

        text_lst = ['backspace', 'delete letter', 'enter forward']
        number_of_text = len(text_lst)

        super().__init__(text_lst, number_of_text)

        self.size = Window.relative_h(20)
        self.space_h = Window.relative_h(50)

    def update_size(self):
        self.update_size_from_menu()
        self.size = Window.relative_h(20)
        self.space_h = Window.relative_h(50)

    def events(self, event, place):
        if event.type == pg.KEYDOWN:
            self.events_from_menu(event)
            if event.key == pg.K_ESCAPE:
                place -= 1
        return place

    def draw(self):
        self.draw_by_given_text()
