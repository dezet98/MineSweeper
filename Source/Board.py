from Source.Button import Button
import random


class Board:
    def __init__(self, variable, signals):
        self.variable = variable
        self.__buttons = [[Button(x, y, self.free_others_function, self.free_bombs, signals) for y in range(self.variable['m'])] for x in range(self.variable['n'])]
        self.out_of_range = lambda a, b: 0 <= a < self.variable['n'] and 0 <= b < self.variable['m']  # this check range
        self.bombs_index = []
        self.set_bombs()
        self.set_numbers()
        print("\nCreate Board")
        signals.reconnect(signals.cloud_bombs, self.cloud_bombs())
        signals.reconnect(signals.uncloud_bombs, self.uncloud_bombs())
        signals.cloud_bombs.connect(self.cloud_bombs)
        signals.uncloud_bombs.connect(self.uncloud_bombs)

    def get_variable(self):
        self.variable['buttons'] = self.__buttons
        return self.variable

    def set_bombs(self):
        all_index = [[x, y] for x in range(0, self.variable['n']) for y in range(0, self.variable['m'])]
        self.bombs_index = random.sample(all_index, self.variable['mines'])
        for x, y in self.bombs_index:
            self.__buttons[x][y].set_bomb()

    @staticmethod
    def index_gen(i, j):
        # index are order as a clock, we start in 'top left' end finish in 'middle left':
        index = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j + 1], [i + 1, j + 1], [i + 1, j], [i + 1, j - 1],
                 [i, j - 1]]
        for i, j in index:
            yield i, j

    def set_numbers(self):
        for i in range(0, self.variable['n']):
            for j in range(0, self.variable['m']):
                number_of = 0
                for x, y in self.index_gen(i, j):
                    if self.out_of_range(x, y) and [x, y] in self.bombs_index:
                        number_of += 1
                self.__buttons[i][j].set_number(number_of)

    def free_others_function(self, i, j):
        self.__buttons[i][j].free()
        for x, y in self.index_gen(i, j):
            if self.out_of_range(x, y):
                if self.__buttons[x][y].check_able_to_free() == 1:
                    self.__buttons[x][y].free_others_function(x, y)
                elif self.__buttons[x][y].check_able_to_free() == 0:
                    self.__buttons[x][y].free()

    def free_bombs(self):
        for x, y in self.bombs_index:
            self.__buttons[x][y].set_icon('../Images/bomb.png', 20, 20)
            self.__buttons[x][y].set_color(100)

    def cloud_bombs(self):
        for x, y in self.bombs_index:
            self.__buttons[x][y].set_color(100)

    def uncloud_bombs(self):
        for x, y in self.bombs_index:
            self.__buttons[x][y].set_basic_color()






