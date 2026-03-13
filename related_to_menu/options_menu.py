import pygame as pg
from related_to_menu.menu import Menu
from related_to_menu.input_dict import InputDict
from static_classes.window import Window
from static_classes.images_functions import Img
from static_classes.draw_text import DrawText


class OptionsMenu(Menu):
    def __init__(self):
        text_lst = ['bird', 'mode', 'name', 'sound', 'screen']
        number_of_text = len(text_lst)

        super().__init__(text_lst, number_of_text)

        self.input_dict = InputDict()
        self.input_dict.load_input_dict()

        self.agent_name = AgentName(self.input_dict)
        self.sound = Sound(self.input_dict)
        self.screen = Screen(self.input_dict)
        self.bird = Bird(self.input_dict)
        self.mode = Mode(self.input_dict)

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


class InputBox:
    def __init__(self, passive_text, active_text, limit_letters=3, limit_width=75):
        self.limit_letters = limit_letters
        self.limit_width = limit_width

        self.active_text = active_text
        self.passive_text = passive_text

        self.passive_frame = (106, 12, 182)
        self.active_frame = (41, 54, 234)

        self.passive_color = (160, 160, 160)
        self.active_color = self.passive_frame

        self.txt_surface = None
        self.rect = None
        self.font = None
        self.give_space_to_rect_w = None
        self.give_space_to_surface_x = None
        self.middle_x = None

        self.update_size()

    def update_size(self):

        w = Window.relative_w(75)
        h = Window.relative_h(30)

        self.rect = pg.Rect(0, 0, w, h)
        font_size = h - Window.relative_h(6)

        self.font = pg.font.Font(DrawText.font_name, font_size)

        self.give_space_to_rect_w = Window.relative_w(15)
        self.give_space_to_surface_x = int((self.give_space_to_rect_w * 2) / 3)
        self.middle_x = Window.relative_w(240)
        self.rect.centerx = self.middle_x

        self.surface_according_to_active_text()

        self.resize_width()

    def surface_according_to_active_text(self):
        if self.active_text is None:
            self.active_text = ''
            self.txt_surface = self.font.render(self.passive_text, True, self.passive_color)
        elif type(self.active_text) == bool:
            if self.active_text:
                self.active_text = 'yes'
            else:
                self.active_text = 'no'
            self.txt_surface = self.font.render(self.active_text, True, self.active_color)

        else:

            self.active_text = str(self.active_text)
            self.txt_surface = self.font.render(self.active_text, True, self.active_color)

    def resize_width(self):
        # Resize the box if the text is too long.

        width = max(self.limit_width, self.txt_surface.get_width() + self.give_space_to_rect_w)
        self.rect.w = width

    def events(self, event):

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:
                self.active_text = self.active_text[:-1]
            elif len(self.active_text) < self.limit_letters:
                char = event.unicode
                if char.isdigit() or char.isalpha():
                    self.active_text += char

        # Re-render the text.

        if self.active_text == '' or self.active_text.isspace():
            self.txt_surface = self.font.render(self.passive_text, True, self.passive_color)

        else:
            self.txt_surface = self.font.render(self.active_text, True, self.active_color)

        self.resize_width()

    def draw(self, color):
        # Blit the text.
        x = self.rect.x + self.give_space_to_surface_x
        y = self.rect.y
        Img.draw(self.txt_surface, x, y)
        # Blit the rect.
        self.rect.centerx = self.middle_x
        pg.draw.rect(Window.window, color, self.rect, 3)  # draw text box


class CategoryInOptionMenu(Menu):
    def __init__(self, text_lst, number_of_text):

        super().__init__(text_lst, number_of_text)

        self.space_h = int(self.space_h / 2)

        self.lst_of_inputs = self.text_lst[1::2]  # only inputboxes

        self.clicked = False

    def update_size_from_category(self):
        self.update_size_from_menu()
        self.space_h = int(self.space_h / 2)
        for input_box in self.text_lst:
            if type(input_box) != str:
                input_box.update_size()
                input_box.resize_width()

    def take_all_inputs(self):
        for i in range(self.number_of_text):
            if i % 2 != 0:
                index = int(i / 2)
                self.lst_of_inputs[index] = self.text_lst[i].active_text

    def events(self, event, place):
        self.clicked = False
        input_box = self.text_lst[self.the_chosen_category]
        if type(input_box) != str:
            input_box.events(event)
        if event.type == pg.KEYDOWN:
            self.events_from_menu(event)
            if event.key == pg.K_ESCAPE:
                place -= 1
            elif event.key == pg.K_RETURN:
                self.take_all_inputs()
                self.clicked = True

        return place

    def draw(self):
        for i in range(self.number_of_text):
            if self.the_chosen_category == i:
                if type(self.text_lst[i]) == str:
                    DrawText.draw_text(self.text_lst[i], self.size, self.x, self.y + i * self.space_h + 10, self.BLUE)
                else:
                    self.text_lst[i].rect.y = self.y + i * self.space_h
                    self.text_lst[i].draw(self.text_lst[i].active_frame)
            else:

                if type(self.text_lst[i]) == str:
                    DrawText.draw_text(self.text_lst[i], self.size, self.x, self.y + i * self.space_h + 10, self.ORANGE)
                else:
                    self.text_lst[i].rect.y = self.y + i * self.space_h
                    self.text_lst[i].draw(self.text_lst[i].passive_frame)


def check_if_boolean_value(value):
    if value.lower() == 'yes':
        value = True
    elif value.lower() == 'no':
        value = False
    else:
        value = None
    return value


def check_if_number(string):
    if string.isnumeric():
        return int(string)
    else:
        return None


class Mode(CategoryInOptionMenu):
    def __init__(self, input_dict):
        limit_letters = 4
        text_lst = ['play forever or once', InputBox('live or die', input_dict.dict['mode'], limit_letters)]
        number_of_text = len(text_lst)
        super().__init__(text_lst, number_of_text)

        self.size = Window.relative_h(14.28)

    def update_size(self):
        self.update_size_from_category()
        self.size = Window.relative_h(14.28)

    def update_inputs(self):
        mode = self.lst_of_inputs[0]
        if mode == 'live' or mode == 'die':
            return mode
        return None


class AgentName(CategoryInOptionMenu):
    def __init__(self, input_dict):
        limit_letters = 11
        text_lst = ['agent name', InputBox('letters', input_dict.dict['agent_name'], limit_letters, 150)]
        number_of_text = len(text_lst)

        super().__init__(text_lst, number_of_text)

        self.size = Window.relative_h(25)

    def update_size(self):
        self.update_size_from_category()
        self.size = Window.relative_h(25)

    def update_inputs(self):
        name = self.lst_of_inputs[0]
        if name == '' or name.isspace():
            name = None
        elif not all(x.isalpha() or x.isspace() for x in name):
            name = None

        return name


class Bird(CategoryInOptionMenu):
    def __init__(self, input_dict):
        text_lst = ['rotate bird', InputBox('yes or no', input_dict.dict['rotate_bird']),
                    'birds number', InputBox('number', input_dict.dict['number_of_birds']),
                    'random place', InputBox('yes or no', input_dict.dict['random_place']),
                    ]
        number_of_text = len(text_lst)

        super().__init__(text_lst, number_of_text)

        self.size = Window.relative_h(20)

    def update_size(self):
        self.update_size_from_category()
        self.size = Window.relative_h(20)

    def update_inputs(self):
        rotate_bird = self.lst_of_inputs[0]
        rotate_bird = check_if_boolean_value(rotate_bird)

        birds_number = self.lst_of_inputs[1]
        birds_number = check_if_number(birds_number)

        random_place = self.lst_of_inputs[2]
        random_place = check_if_boolean_value(random_place)

        return rotate_bird, birds_number, random_place


class Sound(CategoryInOptionMenu):
    def __init__(self, input_dict):
        text_lst = ['jump', InputBox('yes or no', input_dict.dict['jumping_sound']),
                    'score', InputBox('yes or no', input_dict.dict['score_sound']),
                    'music', InputBox('yes or no', input_dict.dict['music_sound']),
                    'death', InputBox('yes or no', input_dict.dict['death_sound'])]
        number_of_text = len(text_lst)

        super().__init__(text_lst, number_of_text)

    def update_size(self):
        self.update_size_from_category()

    def update_inputs(self):
        jump_sound = self.lst_of_inputs[0]
        score_sound = self.lst_of_inputs[1]
        music_sound = self.lst_of_inputs[2]
        death_sound = self.lst_of_inputs[3]

        jump_sound = check_if_boolean_value(jump_sound)
        score_sound = check_if_boolean_value(score_sound)
        music_sound = check_if_boolean_value(music_sound)
        death_sound = check_if_boolean_value(death_sound)

        return jump_sound, score_sound, music_sound, death_sound


class Screen(CategoryInOptionMenu):
    def __init__(self, input_dict):
        text_lst = ['x screen', InputBox('number', input_dict.dict['x_screen'], 5),
                    'y screen', InputBox('number', input_dict.dict['y_screen'], 5)]
        number_of_text = len(text_lst)

        super().__init__(text_lst, number_of_text)
        self.size = Window.relative_h(30)

    def update_size(self):
        self.update_size_from_category()
        self.size = Window.relative_h(30)

    def update_inputs(self):
        x_screen = self.lst_of_inputs[0]
        y_screen = self.lst_of_inputs[1]

        x_screen = check_if_number(x_screen)
        y_screen = check_if_number(y_screen)

        return x_screen, y_screen
