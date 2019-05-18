from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QSize
from Source import globals


class Button(QPushButton):
    def __init__(self, x, y, end_game_function, free_others_function):
        super().__init__()
        self.x = x
        self.y = y
        self.bomb = False
        self.flag = False
        self.question_mark = False
        self.neighbours_bomb = 0
        self.status_of_deactivate = False
        self.end_game_function = end_game_function
        self.status_of_defeat = False
        self.free_others_function = free_others_function
        self.setMaximumSize(35, 35)
        #self.setIcon(QtGui.QIcon('../Images/WindowMainIcon.png'))
        self.setIconSize(QSize(35, 35))

    def mousePressEvent(self, mouse_event):
        if mouse_event.button() == Qt.LeftButton and not globals.game_over:
            if not self.status_of_deactivate:
                self.mouse_left_click()
            print("mouse left click on button[", self.x, '][', self.y, ']')
        elif mouse_event.button() == Qt.RightButton and not globals.game_over:
            if not self.status_of_deactivate:
                self.mouse_right_click()
            print("mouse right click on button[", self.x, '][', self.y, ']')

    def mouse_left_click(self):
        if self.flag or self.question_mark:
            pass
        elif self.bomb:
            self.setText("b")
            self.status_of_deactivate = True
            globals.game_over = True
            self.end_game_function(0)
        elif self.neighbours_bomb != 0:
            self.free()
        else:
            self.free_others_function(self.x, self.y)

    # maybe better idea it will be do me own signal for change flag!!!!(its true)
    def mouse_right_click(self):
        if not self.flag and not self.question_mark:
            self.flag = True
            self.setText('F')
        elif self.flag:
            self.flag = False
            self.question_mark = True
            globals.number_of_no_bomb = globals.number_of_no_bomb + 1
            self.setText('?')
        else:
            self.question_mark = False
            globals.number_of_no_bomb = globals.number_of_no_bomb - 1
            self.setText('')
            self.check_win()

    def set_bomb(self):
        self.bomb = True

    def set_neighbours_bomb(self, number):
        self.neighbours_bomb = number

    def get_bomb(self):
        return self.bomb

    def free(self):
        self.setText(str(self.neighbours_bomb))
        self.status_of_deactivate = True
        globals.number_of_no_bomb = globals.number_of_no_bomb - 1
        self.check_win()

    def check_able_to_free(self):
        if self.bomb or self.neighbours_bomb != 0 or self.status_of_deactivate:
            return False
        else:
            return True

    def check_win(self):
        if globals.number_of_no_bomb == 0:
            self.end_game_function(1)