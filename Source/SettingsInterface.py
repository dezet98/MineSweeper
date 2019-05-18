from PyQt5.QtWidgets import QHBoxLayout, QLabel, QFrame


class SettingsInterface:
    def __init__(self, variable):
        self.create_interface(variable)

    def create_interface(self, variable):
        self.__ver_box = QHBoxLayout()

        __writing = QLabel("Settings:")
        self.__ver_box.addWidget(__writing)

        self.__ver_box.addWidget(QLabel('N='))
        self.__ver_box.addWidget(variable['n'])

        self.__ver_box.addWidget(QLabel('M='))
        self.__ver_box.addWidget(variable['m'])

        self.__ver_box.addWidget(QLabel('Mines='))
        self.__ver_box.addWidget(variable['mines'])

        self.__ver_box.addWidget(variable['ok_button'])

    def layout(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        self.__layout = QHBoxLayout()
        self.__layout.addLayout(self.__ver_box)
        #frame.setLayout(self.__layout)
        return self.__layout

