from PyQt5.QtWidgets import QHBoxLayout, QLabel, QFrame, QVBoxLayout
from Source import globals

class SettingsInterface:
    def __init__(self, variable):
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

        self.__statistics_box = QHBoxLayout()

        self.__statistics_box.addWidget(QLabel("Time: "))
        self.__statistics_box.addWidget(QLabel(str(globals.number_of_bomb)))


        self.__statistics_box.addWidget(QLabel("Bombs: "))

    def layout(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        self.__layout = QVBoxLayout()
        self.__layout.addLayout(self.__setting_box)
        self.__layout.addLayout(self.__statistics_box)
        #frame.setLayout(self.__layout)
        return self.__layout


