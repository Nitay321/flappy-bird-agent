import pygame as pg
from envs.game import Game
from envs.training import Training
from static_classes.window import Window
from static_classes.images_functions import Img
from general_images import GeneralImages

from related_to_menu.main_menu import MainMenu
from related_to_menu.credits_menu import CreditsMenu
from related_to_menu.options_menu import OptionsMenu
from related_to_menu.controls_menu import ControlsMenu

from related_to_menu.input_dict import InputDict


class Main:
    def __init__(self):
        self.place = 0
        self.who_is_playing = None  # 0: play , 1: train

        self.input_dict = InputDict()
        self.input_dict.load_input_dict()

        #self.give_screen_value_from_input_dict()

        self.game = Game()
        self.training = Training()

        self.main_menu = MainMenu()
        self.credits_menu = CreditsMenu()
        self.options_menu = OptionsMenu()
        self.controls_menu = ControlsMenu()

        self.general_images = GeneralImages()

        self.update_values_by_input_dict()

        self.game.sounds.check_if_to_play_music_sound()

    def give_sound_value_from_input_dict(self):
        self.game.sounds.is_jumping_sound = self.input_dict.dict['jumping_sound']
        self.game.sounds.is_scoring_sound = self.input_dict.dict['score_sound']
        self.game.sounds.is_death_sound = self.input_dict.dict['death_sound']
        self.game.sounds.is_music_sound = self.input_dict.dict['music_sound']
        self.training.sounds.is_jumping_sound = self.input_dict.dict['jumping_sound']
        self.training.sounds.is_scoring_sound = self.input_dict.dict['score_sound']
        self.training.sounds.is_death_sound = self.input_dict.dict['death_sound']

    def give_mode_value_from_input_dict(self):
        self.game.mode = self.input_dict.dict['mode']

    def give_agent_name_value_from_input_dict(self):
        self.training.agent.name = self.input_dict.dict['agent_name']

    def give_bird_value_from_input_dict(self):
        self.game.rotate_bird = self.input_dict.dict['rotate_bird']
        self.game.number_of_birds = self.input_dict.dict['number_of_birds']
        self.game.random_place = self.input_dict.dict['random_place']
        self.training.rotate_bird = self.input_dict.dict['rotate_bird']
        self.training.number_of_birds = self.input_dict.dict['number_of_birds']
        self.training.random_place = self.input_dict.dict['random_place']

    def give_screen_value_from_input_dict(self):
        Window.WIDTH = self.input_dict.dict['x_screen']
        Window.HEIGHT = self.input_dict.dict['y_screen']

    def update_values_by_input_dict(self):
        self.give_agent_name_value_from_input_dict()
        self.give_mode_value_from_input_dict()
        self.give_sound_value_from_input_dict()
        self.give_bird_value_from_input_dict()
        self.give_screen_value_from_input_dict()

    def update_size_menu(self):
        self.main_menu.update_size_from_menu()
        self.credits_menu.update_size_from_menu()
        self.options_menu.update_size_from_menu()
        self.options_menu.agent_name.update_size()
        self.options_menu.mode.update_size()
        self.options_menu.screen.update_size()
        self.options_menu.sound.update_size()
        self.options_menu.bird.update_size()
        self.controls_menu.update_size_from_menu()
        self.controls_menu.esc.update_size()
        self.controls_menu.game_in_controls.update_size()
        self.controls_menu.agent_in_controls.update_size()
        self.controls_menu.menu_in_controls.update_size()

        self.general_images.update_size_background()
        self.general_images.update_size_frame_menu()

    def update_size_of_everything(self, w, h):
        w = Window.limit_w(w)
        h = Window.limit_h(h)
        Window.update_size_window(w, h)
        self.game.update_size_game_objects()
        self.training.update_size_training()
        self.update_size_menu()

    def events_menu(self):
        for event in pg.event.get():

            self.game.check_if_to_close_window(event)

            if event.type == pg.VIDEORESIZE or self.game.size_of_window_changed or self.training.size_of_window_changed:
                w, h = pg.display.get_surface().get_size()
                self.update_size_of_everything(w, h)
                self.game.size_of_window_changed = False
                self.training.size_of_window_changed = False

            the_chosen_category = self.main_menu.the_chosen_category
            if self.place == 0:
                self.place = self.main_menu.events(event, self.place)

            elif self.place == 1:
                if the_chosen_category == 0 or the_chosen_category == 1:
                    self.who_is_playing = the_chosen_category
                elif the_chosen_category == 2:
                    self.place = self.options_menu.events(event, self.place)
                elif the_chosen_category == 3:
                    self.place = self.credits_menu.events(event, self.place)
                else:
                    self.place = self.controls_menu.events(event, self.place)

            else:
                if the_chosen_category == 2:
                    the_chosen_category = self.options_menu.the_chosen_category
                    if the_chosen_category == 0:
                        self.place = self.options_menu.bird.events(event, self.place)
                        if self.options_menu.bird.clicked:
                            rotate_bird, number_of_birds, random_place = self.options_menu.bird.update_inputs()

                            self.input_dict.enter_to_dict('rotate_bird', rotate_bird)
                            self.input_dict.enter_to_dict('number_of_birds', number_of_birds)
                            self.input_dict.enter_to_dict('random_place', random_place)

                            self.input_dict.save_input_dict()

                            self.give_bird_value_from_input_dict()
                    elif the_chosen_category == 1:
                        self.place = self.options_menu.mode.events(event, self.place)
                        if self.options_menu.mode.clicked:
                            mode = self.options_menu.mode.update_inputs()
                            self.input_dict.enter_to_dict('mode', mode)

                            self.input_dict.save_input_dict()

                            self.give_mode_value_from_input_dict()

                    elif the_chosen_category == 2:
                        self.place = self.options_menu.agent_name.events(event, self.place)
                        if self.options_menu.agent_name.clicked:
                            agent_name = self.options_menu.agent_name.update_inputs()
                            self.input_dict.enter_to_dict('agent_name', agent_name)

                            self.input_dict.save_input_dict()

                            self.give_agent_name_value_from_input_dict()

                    elif the_chosen_category == 3:
                        self.place = self.options_menu.sound.events(event, self.place)
                        if self.options_menu.sound.clicked:
                            jumping_sound, scoring_sound, music_sound, death_sound = self.options_menu.sound.update_inputs()

                            self.input_dict.enter_to_dict('jumping_sound', jumping_sound)
                            self.input_dict.enter_to_dict('score_sound', scoring_sound)
                            self.input_dict.enter_to_dict('music_sound', music_sound)
                            self.input_dict.enter_to_dict('death_sound', death_sound)

                            self.input_dict.save_input_dict()

                            self.give_sound_value_from_input_dict()

                            self.game.sounds.check_if_to_play_music_sound()

                    else:
                        self.place = self.options_menu.screen.events(event, self.place)
                        if self.options_menu.screen.clicked:
                            x_screen, y_screen = self.options_menu.screen.update_inputs()
                            if x_screen is not None and y_screen is not None:
                                x_screen = Window.limit_w(x_screen)
                                y_screen = Window.limit_h(y_screen)
                                Window.update_size_window(x_screen, y_screen)
                                self.update_size_of_everything(x_screen, y_screen)
                                self.input_dict.enter_to_dict('x_screen', Window.WIDTH)
                                self.input_dict.enter_to_dict('y_screen', Window.HEIGHT)
                                self.input_dict.save_input_dict()

                else:
                    the_chosen_category = self.controls_menu.the_chosen_category
                    if the_chosen_category == 0:
                        self.place = self.controls_menu.esc.events(event, self.place)
                    elif the_chosen_category == 1:
                        self.place = self.controls_menu.game_in_controls.events(event, self.place)
                    elif the_chosen_category == 2:
                        self.place = self.controls_menu.agent_in_controls.events(event, self.place)
                    else:
                        self.place = self.controls_menu.menu_in_controls.events(event, self.place)

    def draw_menu(self):
        self.general_images.draw_background()
        self.general_images.draw_frame_menu()

        if self.place == 0:
            self.main_menu.draw()
        elif self.place == 1:
            the_chosen_category = self.main_menu.the_chosen_category
            if the_chosen_category == 2:
                self.options_menu.draw()
            elif the_chosen_category == 3:
                self.credits_menu.draw()
            elif the_chosen_category == 4:
                self.controls_menu.draw()
            else:
                self.main_menu.draw()

        else:
            if self.main_menu.the_chosen_category == 2:
                the_chosen_category = self.options_menu.the_chosen_category
                if the_chosen_category == 0:
                    self.options_menu.bird.draw()
                elif the_chosen_category == 1:
                    self.options_menu.mode.draw()
                elif the_chosen_category == 2:
                    self.options_menu.agent_name.draw()
                elif the_chosen_category == 3:
                    self.options_menu.sound.draw()
                else:
                    self.options_menu.screen.draw()
            else:
                the_chosen_category = self.controls_menu.the_chosen_category
                if the_chosen_category == 0:
                    self.controls_menu.esc.draw()
                elif the_chosen_category == 1:
                    self.controls_menu.game_in_controls.draw()
                elif the_chosen_category == 2:
                    self.controls_menu.agent_in_controls.draw()
                else:
                    self.controls_menu.menu_in_controls.draw()

        self.game.base.draw()

        pg.display.flip()

    def mainloop(self):
        run = True
        clock = pg.time.Clock()

        while run:
            self.events_menu()
            self.draw_menu()

            self.game.base.move()
            if self.who_is_playing == 0:
                self.game.play()
                self.who_is_playing = None
                self.place = 0

            elif self.who_is_playing == 1:
                self.training.training_agent()
                self.who_is_playing = None
                self.place = 0
            clock.tick(self.game.fps)


if __name__ == '__main__':
    Window.init_window()

    main = Main()

    main.mainloop()
