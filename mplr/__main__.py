import sys
import locale
from PySide6.QtWidgets import QApplication
from views.mainwindow import MainView
from controllers.maincontroller import MainController
from models.model import Model
from connection.subsonic import Subsonic
from connection.player import Player


class MusicPlayer(QApplication):
    def __init__(self):
        super().__init__()
        self.model = Model()
        self.main_controller = MainController(model=self.model)
        self.main_view = MainView(
            model=self.model, main_controller=self.main_controller
        )
        self.model.subsonic = Subsonic()
        self.model.player = Player(self.model)
        self.main_view.show()


if __name__ == "__main__":
    app = MusicPlayer()
    locale.setlocale(locale.LC_NUMERIC, "C")
    sys.exit(app.exec())
