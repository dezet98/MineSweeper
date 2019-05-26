from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore


class Signals(QObject):
    cloud_bombs = QtCore.pyqtSignal()
    uncloud_bombs = QtCore.pyqtSignal()
    bombs_display = QtCore.pyqtSignal()
    time_display = QtCore.pyqtSignal()
    loose = QtCore.pyqtSignal()
    win = QtCore.pyqtSignal()
    set_bomb = QtCore.pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

    def reconnect(self, signal, signal_call):
        while True:
            try:
                if signal_call is not None:
                    signal.disconnect(signal_call)
                else:
                    signal.disconnect()
            except TypeError:
                break
