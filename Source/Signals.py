from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore


class Signals(QObject):
    signal1 = QtCore.pyqtSignal()
    time_signal = QtCore.pyqtSignal()
    def __init__(self):
        QObject.__init__(self)

