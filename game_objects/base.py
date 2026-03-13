from static_classes.window import Window
from static_classes.images_functions import Img


class Base:
    def __init__(self):
        self.height = Window.BASE_HEIGHT
        self.image = Img.load('images/base.png')

        self.update_size()

        self.vx = 2

    def move(self):
        self.rect1.x -= self.vx
        self.rect2.x -= self.vx

        if int(self.rect1.bottomright[0]/self.vx) <= 0:
            self.rect1.x = Window.WIDTH

        if int(self.rect2.bottomright[0]/self.vx) <= 0:
            self.rect2.x = Window.WIDTH

    def update_size(self):
        self.image = Img.resize(self.image, (Window.WIDTH, self.height))

        self.rect1 = self.image.get_rect()
        self.rect2 = self.image.get_rect()

        self.rect1.x = 0
        self.rect1.y = Window.HEIGHT - self.height

        self.rect2.x = Window.WIDTH
        self.rect2.y = Window.HEIGHT - self.height

    def draw(self):
        Img.draw(self.image, self.rect1.x, self.rect1.y)
        Img.draw(self.image, self.rect2.x, self.rect2.y)


