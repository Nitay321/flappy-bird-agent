import pickle


class Agent:
    def __init__(self):
        self.discount_factor = 1
        self.learning_rate = 0.7

        self.q_table = None
        self.action = None

        self.name = None

    def load_q_table(self):
        try:
            with open('brain/' + self.name + '.pickle', 'rb') as file:
                self.q_table = pickle.load(file)
        except:
            self.q_table = {}


    def save_q_table(self):
        with open('brain/' + self.name + '.pickle', 'wb') as file:
            pickle.dump(self.q_table, file, -1)

    def check_state(self, state):
        try:
            self.q_table[state]
        except KeyError:
            self.q_table[state] = [0, 0]

    def max_value(self, state):
        if self.q_table[state][0] < self.q_table[state][1]:
            return self.q_table[state][1]
        return self.q_table[state][0]

    def max_arg(self, state):
        if self.q_table[state][0] < self.q_table[state][1]:
            return 1
        return 0

    def the_chosen_action(self, state):
        self.action = self.max_arg(state)

    def update_value(self, state, next_state, current_reward):

        old_value = self.q_table[state][self.action]

        self.check_state(next_state)

        next_max_value = self.max_value(next_state)
        value = (1 - self.learning_rate) * old_value + self.learning_rate * (
                current_reward + self.discount_factor * next_max_value)

        self.q_table[state][self.action] = value
