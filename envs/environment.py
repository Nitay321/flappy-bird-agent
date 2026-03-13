import pygame as pg
import sys

from game_objects.base import Base
from game_objects.bird import Bird
from general_images import GeneralImages
from game_objects.sounds import Sounds
from game_objects.pipe import Pipe
from game_objects.score import Score
from game_objects.visual_info_of_game_over import VisualInfoOfGameOver
from static_classes.window import Window
from static_classes.images_functions import Img


class Environment:
    def __init__(self):
        self.base = Base()

        self.pipes = [Pipe(), Pipe()]
        self.close_pipe_index = 0

        self.bird = Bird()
        self.birds = []

        self.number_of_birds = None
        self.rotate_bird = None

        self.score = Score()
        self.visual_info_of_game_over = VisualInfoOfGameOver()

        self.general_images = GeneralImages()
        self.sounds = Sounds()

        self.game_is_on = False
        self.last_bird_death = False
        self.stay = True
        self.size_of_window_changed = False
        self.random_place = None

        self.fps = 100
        self.bird_flap = None

    def epoch_bird(self):
        self.birds = []
        for i in range(self.number_of_birds):
            bird = Bird()
            self.birds.append(bird)

            if self.random_place:
                y = Window.get_random_number_for_bird()
                self.birds[i].rect.y = y
            else:
                self.birds[i].rect.y = self.bird.start_y

            self.birds[i].min_y_and_max_y()

            self.birds[i].rotate = self.rotate_bird
            self.birds[i].vy = 1
            self.birds[i].speed = 1

        self.bird = self.birds[0]

    def starting_point(self):
        x_of_pipe_2 = Window.WIDTH + self.pipes[0].distance_between_pipes

        self.pipes[0].rect_up.x = Window.WIDTH
        self.pipes[0].rect_down.x = Window.WIDTH

        self.pipes[1].rect_up.x = x_of_pipe_2
        self.pipes[1].rect_down.x = x_of_pipe_2

        self.pipes[0].create_height(Window.get_random_number_for_pipe(self.pipes[0].space))
        self.pipes[1].create_height(Window.get_random_number_for_pipe(self.pipes[0].space))

        self.close_pipe_index = 0
        self.score.number = 0

        self.epoch_bird()

    def time_to_switch_pipe(self):
        return self.bird.rect.x > self.pipes[self.close_pipe_index].rect_up.bottomright[0]

    def check_collision_with_floor(self):
        return self.bird.rect.bottomright[1] >= Window.HEIGHT - self.base.height

    def check_collision_with_pipe(self):
        return self.bird.is_collided_with(self.pipes[self.close_pipe_index])

    def check_if_to_start_game(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.game_is_on = True
                self.last_bird_death = False
                for bird in self.birds:
                    bird.jump()
                self.sounds.check_if_to_play_jumping_sound()

    def bird_animation(self, event):
        if event.type == self.bird_flap:
            for bird in self.birds:
                if bird.current_image_index < 2:
                    bird.current_image_index += 1
                else:
                    bird.current_image_index = 0
                bird.animation()

    def next_pipe(self):
        next_pipe = (self.close_pipe_index + 1) % 2
        return next_pipe

    def update_score(self):
        if int(self.bird.rect.centerx / self.pipes[0].vx) == int(
                self.pipes[self.close_pipe_index].rect_up.centerx / self.pipes[0].vx):
            self.score.number += 1
            self.sounds.check_if_to_play_scoring_sound()

            if (self.score.number + 1) % 10000 == 0:
                print(self.score.number)

    def time_vals(self):
        clock = pg.time.Clock()
        self.bird_flap = pg.USEREVENT
        pg.time.set_timer(self.bird_flap, 200)
        return clock

    def update_size_game_objects(self):
        self.general_images.update_size_background()
        self.general_images.update_size_message()
        self.pipes[0].update_size()
        self.pipes[1].update_size()
        self.base.update_size()
        self.score.update_size()
        self.visual_info_of_game_over.update_size()

        for bird in self.birds:
            bird.update_size()

    def check_if_to_close_window(self, event):
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    def draw_from_env(self):
        self.general_images.draw_background()
        if len(self.birds) == 1 and self.bird.is_on_ground():
            pass
        elif self.game_is_on:
            self.pipes[0].draw()
            self.pipes[1].draw()
            self.score.draw()
        elif self.last_bird_death:
            self.pipes[0].draw()
            self.pipes[1].draw()
            self.score.draw()
        else:
            self.general_images.draw_message()

        self.base.draw()
        for bird in self.birds:
            bird.draw()
