from PyQt5.QtWidgets import QMessageBox, QWidget


class RangeException(Exception):
    def __init__(self, message):
        self.__message = message

    def get_message(self):
        return self.__message

    def get_statement(self):
        __state_window = QWidget()
        __statement = QMessageBox.question(__state_window, "Message", self.__message, QMessageBox.Ok)
