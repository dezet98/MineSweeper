from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5 import QtGui
from Source import globals


class Button(QPushButton):
    def __init__(self, x, y, end_game_function, free_others_function, free_bombs, signals):
        super().__init__()
        self.signals = signals
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
        self.free_bombs_function = free_bombs
        self.setMaximumSize(35, 35)
        self.setMinimumSize(35, 35)
        self.set_basic_color()
        self.signal = pyqtSignal()

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
            self.status_of_deactivate = True
            self.free_bombs_function()
            globals.game_over = True
            self.end_game_function(0)
        elif self.neighbours_bomb != 0:
            self.free()
        else:
            self.free_others_function(self.x, self.y)

    # maybe better idea it will be do me own signal for change flag!!!!(its true)
    def mouse_right_click(self):
        self.check_win()
        if not self.flag and not self.question_mark:
            self.flag = True
            globals.number_of_bomb -= 1
            self.signals.signal1.emit()
            self.set_icon('../Images/flag.png', 40, 40)
        elif self.flag:
            self.flag = False
            globals.number_of_bomb += 1
            self.signals.signal1.emit()
            self.question_mark = True
            globals.number_of_no_bomb = globals.number_of_no_bomb + 1
            self.set_icon('../Images/question_mark.png', 20, 20)
        else:
            self.question_mark = False
            globals.number_of_no_bomb = globals.number_of_no_bomb - 1
            self.setIconSize(QSize(35, 35))
            self.set_icon(None)

    def set_bomb(self):
        self.bomb = True

    def set_neighbours_bomb(self, number):
        self.neighbours_bomb = number

    def free(self):
        self.setStyleSheet('font-size: 12px;'
                           'font-family: Arial;color: rgb(255, 255, 255);'
                           'background-color: rgb(38,56,76);')
        #self.setStyleSheet('font-size: 12px;font-family: Arial;color: rgb(0, 0, 0);')
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
            globals.game_over = True
            self.end_game_function(1)

    def set_icon(self, path, x=35, y=35):
        self.setIcon(QtGui.QIcon(path))
        self.setIconSize(QSize(x, y))

    def set_color(self, darker=0):
        self.r = self.r - darker if self.r - darker > 0 else 0
        self.g = self.g - darker if self.g - darker > 0 else 0
        self.b = self.b - darker if self.b - darker > 0 else 0
        self.setStyleSheet('background-color: rgb({}, {}, {});'.format(self.r, self.g, self.b))

    def set_basic_color(self):
        self.r, self.g, self.b = 100, 100, 255
        self.setStyleSheet('background-color: rgb({}, {}, {});'.format(self.r, self.g, self.b))