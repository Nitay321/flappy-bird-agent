import pygame as pg


class Sounds:
    def __init__(self):
        self.music = pg.mixer.music.load('sounds/music.mp3')

        self.hit_sound = pg.mixer.Sound('sounds/hit.ogg')
        self.die_sound = pg.mixer.Sound('sounds/die.wav')
        self.jumping_sound = pg.mixer.Sound('sounds/jumping.mp3')
        self.scoring_sound = pg.mixer.Sound('sounds/point.ogg')

        self.is_jumping_sound = None
        self.is_scoring_sound = None
        self.is_death_sound = None
        self.is_music_sound = None

    def check_if_to_play_jumping_sound(self):
        if self.is_jumping_sound:
            self.jumping_sound.play()

    def check_if_to_play_scoring_sound(self):
        if self.is_scoring_sound:
            self.scoring_sound.play()

    def check_if_to_play_music_sound(self):
        if self.is_music_sound:
            pg.mixer.music.play(-1)
        else:
            pg.mixer.music.stop()

    def check_if_to_play_death_sound(self):
        if self.is_death_sound:
            self.hit_sound.play()
            self.die_sound.play()
