import pygame as pg

from envs.environment import Environment
from static_classes.window import Window
from only_training_objects.agent import Agent
from only_training_objects.episode import Episode


def lst_of_pipe_x_and_pipe_y_up(pipe):
    return [pipe.rect_up.x, pipe.rect_up.bottomright[1]]


class Training(Environment):
    def __init__(self):
        super().__init__()

        self.agent = Agent()

        self.episode = Episode()

        self.record = False
        self.show = True

        self.positive_reward = 1  # 0 / 1
        self.save_pipes = []
        self.save_bird_moves = []

    def add_states_to_birds(self):
        for bird in self.birds:
            bird.state = self.get_state()
            self.agent.check_state(bird.state)

    def save_last_birds(self):
        close_pipe = self.pipes[self.close_pipe_index]
        lst = [self.bird.rect.y, self.bird.speed, self.bird.vy]
        if self.bird.rect.centerx == close_pipe.rect_up.centerx + close_pipe.vx:
            self.save_bird_moves = [lst]
        else:
            self.save_bird_moves.append(lst)

    def save_last_pipes(self):
        close_pipe = self.pipes[self.close_pipe_index]
        far_pipe = self.pipes[self.next_pipe()]
        lst = [lst_of_pipe_x_and_pipe_y_up(close_pipe), lst_of_pipe_x_and_pipe_y_up(far_pipe)]
        if self.bird.rect.centerx == close_pipe.rect_up.centerx + 2:
            self.save_pipes = [lst]
        else:
            self.save_pipes.append(lst)

    def record_env(self):
        if self.record:
            self.save_last_pipes()
            self.save_last_birds()


    def starting_point_for_training(self):
        self.starting_point()
        self.add_states_to_birds()

    def update_check_point(self):
        if not self.record:
            self.starting_point_for_training()
        else:
            self.update_starting_point()

    def update_starting_point(self):
        x_of_pipe = self.save_pipes[0][0][0]
        x_of_pipe_2 = self.save_pipes[0][1][0]

        self.pipe[0].update_values(x_of_pipe, self.save_pipes[0][0][1])
        self.pipe[1].update_values(x_of_pipe_2, self.save_pipes[0][1][1])

        self.bird.rect.y = self.save_bird_moves[0][0]
        self.bird.speed = self.save_bird_moves[0][1]
        self.bird.vy = self.save_bird_moves[0][2]

        self.birds.append(self.bird)

        self.close_pipe_index = 0

        self.score.number = 0

    def calculate_horizontal_distance(self, close_pipe):
        horizontal_distance = close_pipe.rect_up.x - self.bird.rect.bottomright[0]
        return horizontal_distance

    def calculate_vertical_distance(self, close_pipe):
        vertical_distance = self.bird.rect.y - close_pipe.rect_up.bottomright[1]
        return vertical_distance

    def get_state(self):
        height_differences = None

        if self.time_to_switch_pipe():
            self.close_pipe_index = self.next_pipe()
            close_pipe = self.pipes[self.close_pipe_index]
            horizontal_distance = self.calculate_horizontal_distance(close_pipe)
            vertical_distance = self.calculate_vertical_distance(close_pipe)
            state = (horizontal_distance, vertical_distance, self.bird.speed)
            return state
        else:
            close_pipe = self.pipes[self.close_pipe_index]
            if self.bird.rect.bottomright[0] < close_pipe.rect_up.x:
                horizontal_distance = self.calculate_horizontal_distance(close_pipe)

            elif self.bird.rect.centerx <= close_pipe.rect_up.centerx:
                horizontal_distance = 0

            else:
                far_pipe = self.pipes[self.next_pipe()]
                horizontal_distance = 0
                height_differences = close_pipe.rect_down.y - far_pipe.rect_down.y  # calculate_height_differences
            vertical_distance = self.calculate_vertical_distance(close_pipe)

            if height_differences is not None:
                state = (horizontal_distance, vertical_distance, self.bird.speed, height_differences)
                return state
            state = (horizontal_distance, vertical_distance, self.bird.speed)
            return state

    def step(self, action):
        if action == 1:
            self.bird.jump()
            self.sounds.check_if_to_play_jumping_sound()
        else:
            self.bird.fall()

        if self.check_collision_with_pipe():
            reward = -1000
            self.birds.remove(self.bird)

            self.sounds.check_if_to_play_death_sound()

        elif self.check_collision_with_floor():
            reward = -1000
            self.birds.remove(self.bird)

            self.sounds.check_if_to_play_death_sound()

        else:
            reward = self.positive_reward

        state = self.get_state()

        return state, reward

    def determine_according_to_record(self):
        if not self.record:
            self.positive_reward = 1

            self.episode.current_color = self.episode.WHITE
        else:
            self.positive_reward = 0
            self.save_bird_moves = []
            self.save_pipes = []

            self.episode.current_color = self.episode.YELLOW

    def update_size_training(self):
        self.update_size_game_objects()
        self.episode.update_size()

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
                elif not self.game_is_on:
                    self.check_if_to_start_game(event)
                if event.key == pg.K_s:
                    self.show = not self.show
                elif event.key == pg.K_RETURN:
                    self.agent.save_q_table()
                    print('###### q_table_is_saved ######')
                elif event.key == pg.K_r:
                    self.record = not self.record
                    self.determine_according_to_record()

            self.bird_animation(event)

    def draw(self, clock):
        if self.show:
            self.draw_from_env()
            if self.game_is_on:
                self.episode.draw()
            clock.tick(self.fps)
            pg.display.flip()

    def training_agent(self):
        self.agent.load_q_table()

        clock = self.time_vals()
        self.stay = True
        self.size_of_window_changed = False
        self.episode.episode_number = 0

        run = True
        while run:
            self.episode.episode_number += 1
            done = False

            self.update_check_point()

            while not done:
                self.events()
                self.draw(clock)
                self.base.move()
                if not self.stay:
                    self.game_is_on = False
                    self.record = False
                    return
                elif self.game_is_on:
                    self.record_env()
                    self.update_score()
                    self.pipes[0].move()
                    self.pipes[1].move()
                    for bird in self.birds:
                        self.bird = bird

                        self.agent.the_chosen_action(self.bird.state)

                        next_state, reward = self.step(self.agent.action)

                        self.agent.update_value(self.bird.state, next_state, reward)

                        self.bird.state = next_state
                    if not self.birds:
                        done = True
                    elif self.score.number == 10000000:
                        self.agent.save_q_table()
                        self.game_is_on = False
                        done = True

                else:
                    for bird in self.birds:
                        bird.starting_movement()

        self.agent.save_q_table()
        print('###### q_table_is_saved ######')


if __name__ == '__main__':
    Window.init_window()

    t = Training()

    t.training_agent()
