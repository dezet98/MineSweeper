from PyQt5.QtWidgets import QAction, qApp


class Menu:
    def __init__(self, window):
        self.window = window
        self.menu_bar = window.menuBar()
        self.status_bar = window.statusBar()
        self.file()
        self.view()

    def file(self):
        file_menu = self.menu_bar.addMenu('File')
        exit_action = QAction('Exit', self.window)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit program without save')
        exit_action.triggered.connect(qApp.quit)
        file_menu.addAction(exit_action)

    def view(self):
        view_menu = self.menu_bar.addMenu('View')
        dark_action = QAction('Set black view', self.window)
        dark_action.setShortcut('Ctrl+B')
        dark_action.setStatusTip("Change a style on dark")
        # stanowczo poprzez zmienne globalne to dorobisz!!!! self.window.setStyleSheet("background-color: black;")
        view_menu.addAction(dark_action)