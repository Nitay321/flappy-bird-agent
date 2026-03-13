from static_classes.images_functions import Img
from static_classes.window import Window


class GeneralImages:
    def __init__(self):
        self.background = Img.load('images/background.png')
        self.message = Img.load('images/message.png')

        self.frame_menu = Img.load('images/frame1.png')

        self.x_message = None
        self.y_message = None

        self.x_frame_menu = None
        self.y_frame_menu = None

        self.update_size_background()
        self.update_size_message()
        self.update_size_frame_menu()

    def update_size_background(self):
        self.background = Img.resize(self.background, (Window.WIDTH, Window.HEIGHT))

    def update_size_message(self):
        self.x_message = Window.relative_w(80)
        self.y_message = Window.relative_h(50)

        w = Window.WIDTH - 2 * self.x_message
        h = (Window.HEIGHT - Window.BASE_HEIGHT) - 2 * self.y_message
        self.message = Img.resize(self.message, (w, h))

    def update_size_frame_menu(self):
        self.x_frame_menu = Window.relative_w(15)
        self.y_frame_menu = Window.relative_h(12)

        w = Window.WIDTH - 2 * self.x_frame_menu
        h = (Window.HEIGHT - Window.BASE_HEIGHT) - 2 * self.y_frame_menu

        self.frame_menu = Img.resize(self.frame_menu, (w, h))

    def draw_background(self):
        Img.draw(self.background, 0, 0)

    def draw_message(self):
        Img.draw(self.message, self.x_message, self.y_message)

    def draw_frame_menu(self):
        Img.draw(self.frame_menu, self.x_frame_menu, self.y_frame_menu)
