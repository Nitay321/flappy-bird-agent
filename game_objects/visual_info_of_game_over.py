from static_classes.window import Window
from static_classes.images_functions import Img
from static_classes.draw_text import DrawText


class VisualInfoOfGameOver(DrawText):
    def __init__(self, score_number=0):

        super().__init__()

        self.WHITE = (240, 240, 240)
        self.ORANGE = (236, 144, 44)

        self.score_number = score_number
        self.best_score = 0

        self.medal_bronze = Img.load('images/medal_bronze.png')
        self.medal_silver = Img.load('images/medal_silver.png')
        self.medal_gold = Img.load('images/medal_gold.png')

        self.game_over = Img.load('images/game_over.png')

        self.dict_of_values = {'text_size': None,
                               'x_score': None,
                               'y_score': None,
                               'space_h_score': None,
                               'space_w_score': None,
                               'x_medal': None,
                               'y_medal': None,
                               'x_game_over': None,
                               'y_game_over': None,
                               'x_text_information': None,
                               'y_text_information': None,
                               'space_h_text_information': None
                               }

        self.update_size()

    def values_for_score(self):

        self.dict_of_values['x_score'] = Window.relative_w(332)
        self.dict_of_values['y_score'] = Window.relative_h(245)

        self.dict_of_values['space_h_score'] = Window.relative_h(75)
        self.dict_of_values['space_w_score'] = Window.relative_w(5)

    def values_for_medals(self):
        self.dict_of_values['x_medal'] = Window.relative_w(123)
        self.dict_of_values['y_medal'] = Window.relative_h(250)

        w, h = Window.relative_w(70), Window.relative_h(70)
        self.medal_bronze = Img.resize(self.medal_bronze, (w, h))  # 70
        self.medal_silver = Img.resize(self.medal_silver, (w, h))  # 70
        self.medal_gold = Img.resize(self.medal_gold, (w, h))  # 70

    def values_for_game_over(self):
        self.dict_of_values['x_game_over'] = Window.relative_w(90)
        self.dict_of_values['y_game_over'] = Window.relative_h(50)

        w, h = Window.relative_w(300), Window.relative_h(500)
        self.game_over = Img.resize(self.game_over, (w, h))

    def values_for_text_information(self):
        self.dict_of_values['x_text_information'] = Window.relative_w(240)
        self.dict_of_values['y_text_information'] = Window.relative_h(470)

        self.dict_of_values['space_h_text_information'] = Window.relative_h(30)

    def update_size(self):

        self.dict_of_values['text_size'] = Window.relative_h(20)

        self.values_for_score()
        self.values_for_medals()
        self.values_for_game_over()
        self.values_for_text_information()

    def find_best_score(self):
        if self.score_number > self.best_score:
            self.best_score = self.score_number

    def draw_medal(self):
        if self.score_number < 10:
            Img.draw(self.medal_bronze, self.dict_of_values['x_medal'], self.dict_of_values['y_medal'])
        elif 9 < self.score_number < 100:
            Img.draw(self.medal_silver, self.dict_of_values['x_medal'], self.dict_of_values['y_medal'])
        else:
            Img.draw(self.medal_gold, self.dict_of_values['x_medal'], self.dict_of_values['y_medal'])

    def draw_current_score(self):

        self.draw_text(str(self.score_number),
                       self.dict_of_values['text_size'],
                       self.dict_of_values['x_score'],
                       self.dict_of_values['y_score'],
                       self.WHITE)

    def draw_best_score(self):
        self.find_best_score()
        self.draw_text(str(self.best_score),
                       self.dict_of_values['text_size'],
                       self.dict_of_values['x_score'] + self.dict_of_values['space_w_score'],
                       self.dict_of_values['y_score'] + self.dict_of_values['space_h_score'],
                       self.WHITE)

    def draw_information(self):
        self.draw_text('space for game', self.dict_of_values['text_size'],
                       self.dict_of_values['x_text_information'],
                       self.dict_of_values['y_text_information'],
                       self.ORANGE)

        self.draw_text('esc for menu', self.dict_of_values['text_size'],
                       self.dict_of_values['x_text_information'],
                       self.dict_of_values['y_text_information'] + self.dict_of_values['space_h_text_information'],
                       self.ORANGE)

    def draw(self):
        Img.draw(self.game_over, self.dict_of_values['x_game_over'], self.dict_of_values['y_game_over'])
        self.draw_current_score()
        self.draw_best_score()
        self.draw_medal()
        self.draw_information()
