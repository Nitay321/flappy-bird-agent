from static_classes.window import Window
from static_classes.images_functions import Img


class Pipe:
    def __init__(self):
        self.image_down = Img.load('images/2000.png')
        self.image_up = None

        self.vx = 2

        self.distance_between_pipes = None
        self.thickness = None
        self.space = None

        self.update_size()

    def create_height(self, y):
        y_up = y
        y_down = y_up + self.space

        self.rect_up.bottomleft = (self.rect_up.x, y_up)
        self.rect_down.y = y_down

    def return_x_for_rects(self):
        try:
            x = Window.relative_w(self.rect_up.x)
            return x
        except ZeroDivisionError:
            x = 0
            return x

    def update_values(self, x, y_up):
        self.create_height(y_up)
        self.rect_up.x = x
        self.rect_down.x = x

    def update_size(self):
        self.thickness = Window.relative_w(80)
        height = 2000
        self.image_down = Img.resize(self.image_down, (self.thickness, height))
        self.image_up = Img.flip(self.image_down, False, True)

        self.space = Window.relative_h(180)

        try:
            x = self.return_x_for_rects()
            y_up = Window.relative_h(self.rect_up.bottomright[1])
            self.rect_down = self.image_up.get_rect()
            self.rect_up = self.image_up.get_rect()

            self.rect_up.x, self.rect_down.x = x, x
            self.create_height(y_up)

        except AttributeError:
            self.rect_down = self.image_up.get_rect()
            self.rect_up = self.image_up.get_rect()

        self.find_the_distance_between_pipes()

    def move(self):
        self.rect_down.x -= self.vx
        self.rect_up.x -= self.vx

        if self.rect_up.bottomright[0] <= 0:
            self.rect_down.x = Window.WIDTH
            self.rect_up.x = Window.WIDTH
            self.create_height(Window.get_random_number_for_pipe(self.space))

    def draw(self):
        Img.draw(self.image_up, self.rect_up.x, self.rect_up.y)
        Img.draw(self.image_down, self.rect_down.x, self.rect_down.y)

    def find_the_distance_between_pipes(self):
        self.distance_between_pipes = int((Window.WIDTH + self.thickness) / 2)
