from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from Source.Logic import Logic
from Source.Menu import Menu
from Source import globals
from Source.Signals import Signals
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        __menu = Menu(self)
        __central_widget = QWidget()

        self.__signals = Signals()
        self.keys_order = 0  # I need that to notice a keyboard sequences(xyzzy)
        self.__game = Logic(__central_widget, self.__signals)

        self.setCentralWidget(__central_widget)
        self.properties()

    def properties(self):
        self.setWindowTitle('MineSweeper')
        self.setWindowIcon(QtGui.QIcon('../Images/window_icon.jpg'))
        self.resize(540, 440)
        self.show()

    def closeEvent(self, event):  # if we close Window 'event' is generated( QWidget.closeEvent(self, QCloseEvent) )
        answer = QMessageBox.question(self, "Message", "Do you really close the program?")
        if answer == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):     # if user pass in right order 'xyzzy' bomb fields will cloud, 'r' return color
        if e.key() == Qt.Key_X:
            self.keys_order = 1
        elif e.key() == Qt.Key_Y and self.keys_order == 1:
            self.keys_order  += 1
        elif e.key() == Qt.Key_Z and (self.keys_order == 2 or self.keys_order == 3):
            self.keys_order += 1
        elif e.key() == Qt.Key_Y and self.keys_order == 4:
            self.keys_order = 0
            self.__signals.cloud_bombs.emit()
        elif e.key() == Qt.Key_R:
            self.__signals.uncloud_bombs.emit()
        else:
            self.keys_order = 0


if __name__ == '__main__':
    globals.initialize()
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
