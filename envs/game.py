import pygame as pg
from envs.environment import Environment
from static_classes.window import Window


class Game(Environment):
    def __init__(self):
        super().__init__()
        self.jumping_button = False
        self.mode = None

    def bird_jump_or_fall(self):

        if self.jumping_button:
            self.bird.jump()
            self.sounds.check_if_to_play_jumping_sound()
        else:
            self.bird.fall()

    def events(self):
        for event in pg.event.get():

            self.check_if_to_close_window(event)

            if event.type == pg.VIDEORESIZE:
                w, h = event.w, event.h
                w = Window.limit_w(w)
                h = Window.limit_h(h)
                Window.update_size_window(w, h)
                self.update_size_game_objects()
                self.size_of_window_changed = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.stay = False
                if self.last_bird_death:
                    if event.key == pg.K_SPACE:
                        self.last_bird_death = False
                        self.birds = []
                        self.starting_point()
                elif not self.game_is_on:
                    self.check_if_to_start_game(event)

                elif event.key == pg.K_SPACE:
                    self.jumping_button = True

            self.bird_animation(event)

    def draw_game_over(self):
        if self.mode == 'die' and len(self.birds) == 1 and self.bird.is_on_ground():
            self.visual_info_of_game_over.score_number = self.score.number

            self.visual_info_of_game_over.draw()

    def draw(self):
        self.draw_from_env()
        self.draw_game_over()

        pg.display.flip()

    def play(self):
        clock = self.time_vals()
        run = True
        self.stay = True
        self.last_bird_death = False
        self.size_of_window_changed = False

        while run:
            done = False
            self.starting_point()

            while not done:

                self.jumping_button = False

                self.events()
                self.draw()

                self.base.move()

                if not self.stay:
                    self.game_is_on = False
                    return

                elif self.game_is_on:
                    self.update_score()
                    self.pipes[0].move()
                    self.pipes[1].move()

                    for bird in self.birds:
                        self.bird = bird
                        self.bird_jump_or_fall()
                        death = self.check_collision_with_pipe() or self.check_collision_with_floor()
                        if self.time_to_switch_pipe():
                            self.close_pipe_index = self.next_pipe()
                        if death:
                            self.sounds.check_if_to_play_death_sound()
                            if len(self.birds) > 1:
                                self.birds.remove(self.bird)
                            else:
                                self.bird.death_movement()
                                self.last_bird_death = True
                                self.game_is_on = False
                elif self.last_bird_death:
                    if self.mode == 'die':
                        for bird in self.birds:
                            bird.death_movement()

                    else:
                        self.game_is_on = True
                        self.last_bird_death = False
                        done = True
                else:
                    for bird in self.birds:
                        bird.starting_movement()

                clock.tick(self.fps)


if __name__ == '__main__':
    Window.init_window()

    game = Game()

    game.play()
