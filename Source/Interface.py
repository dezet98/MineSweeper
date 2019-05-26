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
        self.signals.loose.connect(self.loose)
        self.signals.win.connect(self.win)
        self.main_layout = QVBoxLayout()
        self.create_settings_layout(variable)
        central_widget.setLayout(self.main_layout)

    def create_settings_layout(self, variable):
        self.__settings = SettingsInterface(variable, self.signals)
        self.main_layout.addLayout(self.__settings.layout())

    def create_board_layout(self, variable):
        self.__board = BoardInterface(variable)
        self.__board_layout = self.__board.layout()
        self.main_layout.addLayout(self.__board_layout)

    def get_board_layout(self):
        return self.__board_layout

    def clear_board_layout(self, layout):
        #layout = self.get_board_layout()
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_board_layout(item.layout())

    def win(self):
         __win_statement = QMessageBox.question(QMessageBox(), "You win!!", "You win!!!\nYour time:", QMessageBox.Ok)

    def loose(self):
        video = QVideoWidget()
        video.resize(500, 400)
        video.setWindowTitle("GAME OVER")
        # video.resize(self.central_widget.height(), self.central_widget.width())
        player = QMediaPlayer()
        player.setVideoOutput(video)
        player.setMedia(QMediaContent(QUrl.fromLocalFile("../Video/bum.gif")))
        video.show()
        QSound.play("../Music/bum.wav")
        player.play()

        time.sleep(5.5)
        player.stop()
        video.close()
