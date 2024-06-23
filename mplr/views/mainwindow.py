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

        self._ui.actionConnect_to_server.triggered.connect(
            self._main_controller.server_connection
        )

        self._model.genres_changed.connect(self.load_genre_list)
        self._model.albums_changed.connect(self.load_album_list)
        self._model.artists_changed.connect(self.load_artist_list)

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
        print("Setting genre list...")
        for genre in value:
            new_action = QListWidgetItem(genre["value"])
            self._ui.filters_genre.addItem(new_action)
        self._ui.filters_genre.repaint()

    @Slot(list)
    def load_artist_list(self, value):
        print("Setting artist list...")
        for artist in value:
            new_action = QListWidgetItem(artist["name"])
            self._ui.filters_artists.addItem(new_action)
        self._ui.filters_artists.repaint()

    @Slot(list)
    def load_album_list(self, value):
        print("Setting album list...")
        for album in value:
            new_action = QListWidgetItem(album["name"])
            self._ui.filters_albums.addItem(new_action)
        self._ui.filters_albums.repaint()
