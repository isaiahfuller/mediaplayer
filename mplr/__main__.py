import sys
from PySide6.QtWidgets import QApplication
from mplr.views.mainwindow import MainView
from mplr.controllers.maincontroller import MainController
from mplr.models.model import Model
from mplr.connection.subsonic import Subsonic


class MusicPlayer(QApplication):
    def __init__(self):
        super().__init__()
        self.model = Model()
        self.main_controller = MainController(model=self.model)
        self.main_view = MainView(
            model=self.model, main_controller=self.main_controller
        )
        self.model.subsonic = Subsonic()
        self.main_view.show()


if __name__ == "__main__":
    app = MusicPlayer()
    sys.exit(app.exec())
