from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
import sys
from PyQt5 import QtGui
from Source.Logic import Logic
from Source.Menu import Menu
from Source import globals


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
        self.resize(500, 400)
        self.game = Logic(self.central_widget)

    def closeEvent(self, event):  # if we close Window 'event' is generated( QWidget.closeEvent(self, QCloseEvent) )
        answer = QMessageBox.question(self, "Message", "Do you really close the program?")
        if answer == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    globals.initialize()
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
