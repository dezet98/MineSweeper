from PyQt5.QtWidgets import QHBoxLayout, QLabel, QFrame, QVBoxLayout, QLCDNumber
from Source import globals
from Source.Signals import Signals

class SettingsInterface:
    def __init__(self, variable, signals):
        self.signals = signals
        self.create_interface(variable)

    def create_interface(self, variable):
        self.__setting_box = QHBoxLayout()

        self.__setting_box.addWidget(QLabel("Settings:"))
        self.__setting_box.addWidget(QLabel('N='))
        self.__setting_box.addWidget(variable['n'])
        self.__setting_box.addWidget(QLabel('M='))
        self.__setting_box.addWidget(variable['m'])
        self.__setting_box.addWidget(QLabel('Mines='))
        self.__setting_box.addWidget(variable['mines'])
        self.__setting_box.addWidget(variable['ok_button'])
        self.__setting_box.addWidget(variable['pause_button'])
        self.__statistics_box = QHBoxLayout()

        self.__statistics_box.addWidget(QLabel("Time: "))
        self.time_display = QLCDNumber()
        self.__statistics_box.addWidget(self.time_display)
        self.signals.time_display.connect(self.show_time)

        self.__statistics_box.addWidget(QLabel("Bombs: "))
        self.bombs_display = QLCDNumber()
        self.__statistics_box.addWidget(self.bombs_display)
        self.signals.bombs_display.connect(self.set_bombs_display)

    def show_time(self):
        self.time_display.display(globals.time)

    def set_bombs_display(self):
        self.bombs_display.display(globals.number_of_bomb)

    def layout(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        self.__layout = QVBoxLayout()
        self.__layout.addLayout(self.__setting_box)
        self.__layout.addLayout(self.__statistics_box)
        #frame.setLayout(self.__layout)
        return self.__layout



