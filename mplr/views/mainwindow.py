from PySide6.QtWidgets import QMainWindow, QListWidgetItem
from PySide6.QtCore import Slot
from mplr.views.mainwindow_ui import Ui_MainWindow
# import locale


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        """
        Initializes the main window of the application.

        Args:
            model: The data model used by the application.
            main_controller: The main controller handling the application's logic.
        """
        super().__init__()
        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # Connect the 'Connect to server' action to the server connection method in the main controller
        self._ui.actionConnect_to_server.triggered.connect(
            self._main_controller.server_connection
        )

        # Connect the model's list_genres_changed signal to the load_genre_list method
        # self._model.list_genres_changed.connect(self.load_genre_list)

        # The following code is commented out and appears to be related to testing or debugging
        # songs = conn.getRandomSongs(size=2)
        # song = songs[0].to_dict()
        # print(song)
        # app = QApplication(sys.argv)
        # locale.setlocale(locale.LC_NUMERIC, "C")
        # song = conn.stream(song["id"])
        # print(song.content)
        # player = mpv.MPV(
        #     wid=str(int(self._ui.mpv_container.winId())),
        #     log_handler=print,
        #     loglevel="debug",
        # )
        # player.play_bytes(song.content)
        # player.set

    @Slot(list)
    def load_genre_list(self, value):
        for genre in sorted(value):
            new_action = QListWidgetItem(genre)
            self._ui.filters_genre.addItem(new_action)
        self._ui.filters_genre.repaint()
