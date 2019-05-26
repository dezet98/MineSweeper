from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtGui
from Source.Logic import Logic
from Source.Menu import Menu
from Source import globals
from Source.Signals import Signals

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = Menu(self)
        self.central_widget = QWidget()
        self.properties()
        self.setCentralWidget(self.central_widget)
        self.show()

    def properties(self):
        self.setWindowTitle('Saper')
        self.setWindowIcon(QtGui.QIcon('../Images/WindowMainIcon.png'))
        self.resize(540, 440)
        #self.setStyleSheet('background-image: url(../Images/WindowMainIcon.png);')
        self.signals = Signals()
        self.game = Logic(self.central_widget, self.signals)

    def closeEvent(self, event):  # if we close Window 'event' is generated( QWidget.closeEvent(self, QCloseEvent) )
        answer = QMessageBox.question(self, "Message", "Do you really close the program?")
        if answer == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_X:
            globals.xyzzy = 1
        elif e.key() == Qt.Key_Y and globals.xyzzy == 1:
            globals.xyzzy += 1
        elif e.key() == Qt.Key_Z and (globals.xyzzy == 2 or globals.xyzzy == 3):
            globals.xyzzy += 1
        elif e.key() == Qt.Key_Y and (globals.xyzzy == 4):
            self.game.change_bombs_color(True)  # bombs fields change color(with False as a arg color return to basic)
        elif e.key() == Qt.Key_R:
            self.game.change_bombs_color(False)
        else:
            globals.xyzzy = 0


if __name__ == '__main__':
    globals.initialize()
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
