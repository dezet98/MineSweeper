from PyQt5.QtWidgets import QWidget, QMessageBox, QVBoxLayout
from Source.SettingsInterface import SettingsInterface
from Source.BoardInterface import BoardInterface
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QSound
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
import time


class Interface:
    def __init__(self, variable, central_widget, signals):
        self.central_widget = central_widget
        self.variable = variable
        self.signals = signals
        self.main_layout = QVBoxLayout()
        self.create_settings_layout(variable)
        central_widget.setLayout(self.main_layout)

    def create_settings_layout(self, variable):
        self.__settings = SettingsInterface(variable, self.signals)
        self.main_layout.addLayout(self.__settings.layout())

    def get_settings_layout(self):
        return self.__settings

    def create_board_layout(self, board):
        self.__board_layout = BoardInterface(board.get_variable()).layout()
        self.main_layout.addLayout(self.__board_layout)

    def get_board_layout(self):
        return self.__board_layout

    def clear_board_layout(self, layout):

        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_board_layout(item.layout())

    def end_game(self, results):
        __loose_window = QWidget()
        if results:
            __win_statement = QMessageBox.question(__loose_window, "You win!!", "You win!!!\nYour time:", QMessageBox.Ok)
        else:
            video = QVideoWidget()
            video.resize(500, 400)
            video.setWindowTitle("GAME OVER")
            #video.resize(self.central_widget.height(), self.central_widget.width())
            player = QMediaPlayer()
            player.setVideoOutput(video)
            player.setMedia(QMediaContent(QUrl.fromLocalFile("../Images/bum.gif")))
            video.show()
            QSound.play("../Images/bum.wav")
            player.play()

            time.sleep(5.5)
            player.stop()
            video.close()