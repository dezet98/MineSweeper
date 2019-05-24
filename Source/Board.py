from Source.Button import Button
from Source import globals
import random


class Board:
    def __init__(self, variable, end_game_function):
        self.variable = variable
        self.__buttons = [[Button(j, i, end_game_function, self.free_others_function, self.free_bombs) for i in range(self.variable['m'])] for j in range(self.variable['n'])]
        self.set_bombs()
        self.set_numbers()
        print("\nCreate Board")

    def get_variable(self):
        self.variable['buttons'] = self.__buttons
        return self.variable

    def set_bombs(self):
        all_index = []
        for i in range(0, self.variable['n']):
            for j in range(0, self.variable['m']):
                all_index.append([i, j])

        self.bombs_index = random.sample(all_index, self.variable['mines'])

        for x, y in self.bombs_index:
            self.__buttons[x][y].set_bomb()

    # this can be in button if we are have a global n and m for example, you will see
    def set_numbers(self):
        self.out_of_range = lambda a, b: 0 <= a < self.variable['n'] and 0 <= b < self.variable['m']

        for i in range(0, self.variable['n']):
            for j in range(0, self.variable['m']):
                number_of = 0
                if self.out_of_range(i-1, j-1) and [i-1, j-1] in self.bombs_index:
                    number_of += 1
                if self.out_of_range(i-1, j) and [i-1, j] in self.bombs_index:
                    number_of += 1
                if self.out_of_range(i-1, j+1) and [i-1, j+1] in self.bombs_index:
                    number_of += 1
                if self.out_of_range(i, j-1) and [i, j-1] in self.bombs_index:
                    number_of += 1
                if self.out_of_range(i, j+1) and [i, j+1] in self.bombs_index:
                     number_of += 1
                if self.out_of_range(i+1, j-1) and [i+1, j-1] in self.bombs_index:
                     number_of += 1
                if self.out_of_range(i+1, j) and [i+1, j] in self.bombs_index:
                    number_of += 1
                if self.out_of_range(i+1, j+1) and [i+1, j+1] in self.bombs_index:
                   number_of += 1
                self.__buttons[i][j].set_neighbours_bomb(number_of)

    def free_others_function(self, i, j):
        self.__buttons[i][j].free()

        if self.out_of_range(i - 1, j - 1):
            if self.__buttons[i - 1][j - 1].check_able_to_free():
                self.__buttons[i - 1][j - 1].free_others_function(i-1, j-1)

        if self.out_of_range(i - 1, j):
            if self.__buttons[i - 1][j].check_able_to_free():
                self.__buttons[i - 1][j].free_others_function(i-1, j)

        if self.out_of_range(i - 1, j + 1):
            if self.__buttons[i - 1][j + 1].check_able_to_free():
                self.__buttons[i - 1][j + 1].free_others_function(i-1, j+1)

        if self.out_of_range(i, j - 1):
            if self.__buttons[i][j - 1].check_able_to_free():
                self.__buttons[i][j - 1].free_others_function(i, j-1)

        if self.out_of_range(i, j + 1):
            if self.__buttons[i][j + 1].check_able_to_free():
                self.__buttons[i][j + 1].free_others_function(i, j+1)

        if self.out_of_range(i + 1, j - 1):
            if self.__buttons[i + 1][j - 1].check_able_to_free():
                self.__buttons[i + 1][j - 1].free_others_function(i+1, j-1)

        if self.out_of_range(i + 1, j):
            if self.__buttons[i + 1][j].check_able_to_free():
                self.__buttons[i + 1][j].free_others_function(i+1, j)

        if self.out_of_range(i + 1, j + 1):
            if self.__buttons[i + 1][j + 1].check_able_to_free():
                self.__buttons[i + 1][j + 1].free_others_function(i+1, j+1)

    def free_bombs(self):
        for i in self.bombs_index:
            self.__buttons[i[0]][i[1]].set_icon('../Images/bomb.jfif', 20, 20)

    def change_bombs_color(self, change):
        if change:
            for x, y in self.bombs_index:
                self.__buttons[x][y].set_color(20)
        else:
            for x, y in self.bombs_index:
                self.__buttons[x][y].set_basic_color()



