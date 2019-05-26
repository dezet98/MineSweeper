from PyQt5.QtWidgets import QLineEdit, QPushButton, QWidget, QMessageBox
from PyQt5.QtCore import Qt, QThread, QCoreApplication
from Source.Interface import Interface
from Source import Exceptions
from Source.Board import Board
from Source import globals
from PyQt5 import QtCore
import sys, time

class Logic:
    def __init__(self, central_widget, signals):
        self.signals = signals
        self.create_variables()
        self.interface = Interface(self.get_variable(), central_widget, self.signals)
        self.create_board()     # create a default first board
        self.__ok_button.clicked.connect(self.clicked_ok_button)
        self.__pause_button.clicked.connect(self.clicked_pause_button)

    def create_variables(self):
        self.__n = QLineEdit()
        # self.__n.setMaximumSize(40, 25)
        self.__n.setText("8")
        self.__m = QLineEdit()
        # self.__m.setMaximumSize(40, 25)
        self.__m.setText("8")
        self.__mines = QLineEdit()
        # self.__mines.setMaximumSize(40, 25)
        self.__mines.setText("12")
        self.__ok_button = QPushButton("Start Game")
        self.__ok_button.setShortcut(Qt.Key_Return)
        self.__pause_button = QPushButton("Pause")
        self.__pause_button.setShortcut(Qt.Key_P)

    def get_variable(self):
        return {'n': self.__n, 'm': self.__m, 'mines': self.__mines, 'ok_button': self.__ok_button, 'pause_button': self.__pause_button}

    def get_board_variable(self):
        return {'n': int(self.__n.text()), 'm': int(self.__m.text()), 'mines': int(self.__mines.text())}

    def clicked_ok_button(self):
        try:
            n = int(self.__n.text())
            m = int(self.__m.text())
            mines = int(self.__mines.text())

            interval1 = [i for i in range(2, 16)]
            interval2 = [i for i in range(0, n*m+1)]
            if n not in interval1 or m not in interval1 or mines not in interval2:
                raise Exceptions.RangeException("Incorrect range!\nN, M belong to [2, 15] and Mines to [0, N*M]")

        except ValueError:
            print("It's ValueError, user didn't pass 'int'\n")
            __state_window = QWidget()
            __content = "Error: Fill boxes uses natural numbers"
            __statement = QMessageBox.question(__state_window, "Message", __content, QMessageBox.Ok)

        except Exceptions.RangeException as r:
            print(r.get_message())
            r.get_statement()

        else:
            self.interface.clear_board_layout(self.interface.get_board_layout())
            self.create_board()

    def clicked_pause_button(self):
        if globals.game_pause == False:
            globals.game_pause = True
            self.__pause_button.setStyleSheet('background-color: rgb(38,56,76)')
        else:
            globals.game_pause = False
            self.__pause_button.setStyleSheet('background-color: rgb(, , ,)')

    def get_board(self):
        return self.__board

    def change_bombs_color(self, change):
        self.get_board().change_bombs_color(change)  # bring a function in Board where bombs fields will be dark

    def create_board(self):
        self.time()
        globals.game_over = False
        if globals.game_pause:
            self.clicked_pause_button()
        globals.number_of_no_bomb = int(self.__n.text()) * int(self.__m.text()) - int(self.__mines.text())
        globals.number_of_bomb = int(self.__mines.text())
        self.signals.signal1.emit()
        self.__board = Board(self.get_board_variable(), self.interface.end_game, self.signals)
        self.interface.create_board_layout(self.get_board())

    def time(self):
        self.curr_time = QtCore.QTime(00, 00, 00)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.count_time)
        self.timer.start(1000)

    def count_time(self):
        if globals.game_over or globals.game_pause:
            self.timer.stop()
            self.timer.start(1000)
        else:
            globals.time = self.curr_time.toString("hh:mm:ss")
            self.signals.time_signal.emit()
            self.curr_time = self.curr_time.addSecs(1)
