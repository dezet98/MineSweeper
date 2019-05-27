import sys

from PyQt5 import QtCore
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
import time
from PyQt5 import  QtMultimediaWidgets


app = QApplication(sys.argv)


playlist = QMediaPlaylist()
url = QUrl.fromLocalFile("../Video/bum.mp4")
playlist.addMedia(QMediaContent(url))
#playlist.setCurrentIndex(0)


player = QMediaPlayer()
player.setPlaylist(playlist)

videoWidget = QtMultimediaWidgets.QVideoWidget()
player.setVideoOutput(videoWidget)
videoWidget.show()
player.play()

sys.exit(app.exec_())






