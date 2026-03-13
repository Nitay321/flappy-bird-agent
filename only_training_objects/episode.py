from static_classes.draw_text import DrawText
from static_classes.window import Window


class Episode:
    def __init__(self):

        self.episode_number = 0

        self.size = None
        self.x = None
        self.y = None

        self.update_size()
        self.WHITE = (255, 234, 246)
        self.YELLOW = (255, 255, 40)
        self.current_color = self.WHITE

    def update_size(self):
        self.size = Window.relative_h(20)
        self.x = Window.relative_w(25)
        self.y = Window.relative_h(25)

    def draw(self):
        text = 'episode ' + str(self.episode_number)
        DrawText.draw_text_not_from_center(text, self.size, self.x, self.y, self.current_color)
