from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtCore import QUrl


class Music:
    def __init__(self, playlist, player, signals):
        self.playlist = playlist
        self.player = player
        url = QUrl.fromLocalFile("../Music/main_music.wav")
        self.playlist.addMedia(QMediaContent(url))

        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player.setPlaylist(self.playlist)
        signals.play_music.connect(self.play_music)
        signals.stop_music.connect(self.stop_music)
        signals.add_music.connect(lambda: self.add_music("../Music/bum.wav"))
        signals.delete_music.connect(lambda: self.delete_music(self.playlist.currentIndex()))

    def stop_music(self):
        self.player.stop()

    def play_music(self):
        self.player.play()

    def add_music(self, path):
        url = QUrl.fromLocalFile(path)
        self.playlist.addMedia(QMediaContent(url))
        self.playlist.next()

    def delete_music(self, index):
        self.playlist.removeMedia(index)