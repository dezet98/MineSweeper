import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QShortcut, QLabel, QApplication, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtGui
from Images import *

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.label = QLabel("Try Ctrl+O", self)
        self.shortcut = QShortcut(QKeySequence(Qt.Key_Enter + Qt.Key_0), self)
        self.shortcut.activated.connect(self.on_open)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        #self.button = QPushButton("")
        #self.layout.addWidget(self.button)
        #self.button.setIcon(QtGui.QIcon('..\Images\WindowMainIcon.png'))

        self.setLayout(self.layout)
        self.resize(150, 100)
        self.show()

    @pyqtSlot()
    def on_open(self):
        print("Opening!")
       # self.short = QShortcut(QKeySequence("O"), self)
        #self.short.activated.connect(self.dz)
        print("why")

    @pyqtSlot()
    def dz(self):
        print("Op!")


app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())