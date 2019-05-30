from PyQt5.QtWidgets import QAction, qApp
import webbrowser
from Source import globals


class Menu:
    def __init__(self, window, signals):
        self.window = window
        self.signals = signals
        self.menu_bar = window.menuBar()
        self.status_bar = window.statusBar()

        file_menu = self.menu_bar.addMenu('File')
        file_menu.addAction(self.exit())

        options_menu = self.menu_bar.addMenu('Options')
        options_menu.addAction(self.dark())
        options_menu.addAction(self.music())
        options_menu.addAction(self.help())

    def exit(self):
        exit_action = QAction('Exit', self.window)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit program without save')
        exit_action.triggered.connect(qApp.quit)
        return exit_action

    def music(self):
        music_action = QAction('Music', self.window)
        music_action.setCheckable(True)
        music_action.setChecked(True)
        music_action.setShortcut('Ctrl+M')
        music_action.setStatusTip('Turn off Music')

        def checked():
            if not music_action.isChecked():
                globals.music = False
                music_action.setStatusTip('Turn on Music')
                self.signals.stop_music.emit()
            else:
                globals.music = True
                music_action.setStatusTip('Turn off Music')
                self.signals.play_music.emit()

        music_action.triggered.connect(checked)
        return music_action

    def dark(self):
        dark_action = QAction('Set black view', self.window)
        dark_action.setShortcut('Ctrl+B')
        dark_action.setStatusTip("Change a style on dark")
        # stanowczo poprzez zmienne globalne to dorobisz!!!! self.window.setStyleSheet("background-color: black;")
        return dark_action

    def help(self):
        open_webb = QAction('Help', self.window)
        open_webb.setShortcut('Ctrl+H')
        open_webb.setStatusTip('Display a website with rules')

        def web():
            self.signals.pause.emit()
            webbrowser.open("https://en.wikipedia.org/wiki/Minesweeper_(video_game)")

        open_webb.triggered.connect(web)
        return open_webb
