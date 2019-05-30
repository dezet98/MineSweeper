from PyQt5.QtWidgets import QHBoxLayout, QLabel, QFrame, QVBoxLayout, QLCDNumber
from PyQt5.QtGui import QPixmap
from Source import globals


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

        self.time_display = QLCDNumber()
        self.time_display.setFrameShape(QFrame.NoFrame)
        self.time_display.setMaximumSize(80, 60)
        self.time_display.setMinimumSize(80, 60)
        self.bombs_display = QLCDNumber()
        self.bombs_display.setMaximumSize(80, 40)
        self.bombs_display.setMinimumSize(80, 40)
        self.bombs_display.setFrameShape(QFrame.NoFrame)
        self.signals.update_time_display.connect(self.update_time)
        self.signals.update_bombs_display.connect(self.update_bombs)

        self.__statistics_box.addWidget(self.time_display)
        self.__statistics_box.addWidget(self.bombs_display)

    def update_time(self):
        self.time_display.display(globals.time)

    def update_bombs(self):
        self.bombs_display.display(globals.number_of_bomb)

    def layout(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        self.__layout = QVBoxLayout()
        self.__layout.addLayout(self.__setting_box)
        self.__layout.addLayout(self.__statistics_box)
        self.__layout.addStretch(1)
        self.__layout.setSpacing(10)
        frame.setLayout(self.__layout)
        frame.setMaximumSize(560, 126)

        layout = QVBoxLayout()
        layout.addWidget(frame)

        return layout



