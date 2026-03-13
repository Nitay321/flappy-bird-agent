import pickle


def check_value(current_value, default_value):
    if current_value is None:
        return default_value
    return current_value


class InputDict:
    def __init__(self):

        self.dict = None

        self.name = 'input_dict'

    def load_input_dict(self):
        try:
            with open('related_to_menu/' + self.name + '.pickle', 'rb') as file:
                self.dict = pickle.load(file)
        except FileNotFoundError:
            self.dict = {'agent_name': 'brain',
                         'jumping_sound': True,
                         'score_sound': True,
                         'music_sound': True,
                         'death_sound': True,
                         'rotate_bird': False,
                         'number_of_birds': 1,
                         'random_place': False,
                         'x_screen': 480,
                         'y_screen': 600,
                         'mode': 'die'}

    def save_input_dict(self):
        with open('related_to_menu/' + self.name + '.pickle', 'wb') as file:
            pickle.dump(self.dict, file, -1)

    def enter_to_dict(self, key, value):
        last_value = self.dict[key]
        value = check_value(value, last_value)
        self.dict[key] = value
