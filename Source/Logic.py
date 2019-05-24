from PyQt5.QtWidgets import QLineEdit, QPushButton, QWidget, QMessageBox
from PyQt5.QtCore import Qt, QThread, QCoreApplication
from Source.Interface import Interface
from Source import Exceptions
from Source.Board import Board
from Source import globals
import sys, time

class Logic:
    def __init__(self, central_widget):
        self.create_variables()
        self.interface = Interface(self.get_variable(), central_widget)
        self.check_ok_button()

    def create_variables(self):
        self.__n = QLineEdit()
        # self.__n.setMaximumSize(40, 25)
        self.__n.setText("5")
        self.__m = QLineEdit()
        # self.__m.setMaximumSize(40, 25)
        self.__m.setText("7")
        self.__mines = QLineEdit()
        # self.__mines.setMaximumSize(40, 25)
        self.__mines.setText("7")
        self.__ok_button = QPushButton("Start Game")
        self.__ok_button.setShortcut(Qt.Key_Return)
        self.first_game = 0

    def get_variable(self):
        return {'n': self.__n, 'm': self.__m, 'mines': self.__mines, 'ok_button': self.__ok_button}

    def get_board_variable(self):
        return {'n': int(self.__n.text()), 'm': int(self.__m.text()), 'mines': int(self.__mines.text())}

    def check_ok_button(self):
        self.__ok_button.clicked.connect(self.clicked_ok_button)

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
            if self.first_game is 0:
                self.first_game = 1
            else:
                self.interface.clear_board_layout(self.interface.get_board_layout())
            globals.game_over = False
            globals.number_of_no_bomb = int(self.__n.text()) * int(self.__m.text()) - int(self.__mines.text())
            globals.number_of_bomb = int(self.__mines.text())
            self.create_board(self.interface.end_game)
            self.interface.create_board_layout(self.get_board())

            #self.using_q_thread()

    def create_board(self, end_game_function):
        self.__board = Board(self.get_board_variable(), end_game_function)

    def get_board(self):
        return self.__board

    def change_bombs_color(self, change):
        self.get_board().change_bombs_color(change)  # bring a function in Board where bombs fields will be dark

    '''  def using_q_thread(self):
        thread = self.AThread()
        thread.finished.connect(globals.app.exit)
        thread.start()

    class AThread(QThread):

        def run(self):
            count = 0
            while count < 5:
                time.sleep(1)
                print("A Increasing")
                count += 1
                '''