from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QTreeWidgetItem
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from mplr.views.mainwindow_ui import Ui_MainWindow
from mplr.util.timeformat import time_format
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

        self._ui.songs_display.itemDoubleClicked.connect(
            self._main_controller.play_song
        )
        self._ui.player_button_pause.clicked.connect(self._main_controller.player_pause)

        self._model.genres_changed.connect(self.load_genre_list)
        self._model.albums_changed.connect(self.load_album_list)
        self._model.artists_changed.connect(self.load_artist_list)
        self._model.songs_changed.connect(self.load_songs)

        self._model.current_song_changed.connect(self.set_current_song_display)
        self._model.player_duration_changed.connect(self.set_current_song_duration)

    @Slot(dict)
    def set_current_song_display(self, song):
        print(song)
        slider = self._ui.player_position_slider
        label = self._ui.player_position_song_length
        slider.setValue(0)
        slider.setMaximum(song["duration"])
        label.setText(time_format(song["duration"]))

        self._ui.player_label_title.setText(song["title"])
        self._ui.player_label_artist.setText(song["artist"])

        data = self._model.subsonic.connection.getCoverArt(song["coverId"], size="100")
        pixmap = QPixmap()
        pixmap.loadFromData(data.content)
        self._ui.player_label_art.setPixmap(pixmap)

    @Slot(float)
    def set_current_song_duration(self, duration):
        label = self._ui.player_position_current
        slider = self._ui.player_position_slider
        label.setText(time_format(duration))
        slider.setValue(int(duration))

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

    @Slot(list)
    def load_songs(self, value):
        print("Setting songs...")
        # keys: title, track, artist, album
        for song in value:
            new_item = QTreeWidgetItem()
            item_text = [
                song["title"],
                song["track"],
                song["artist"],
                song["album"],
                song["id"],
            ]
            for i in range(0, len(item_text)):
                new_item.setText(i, str(item_text[i]))
            self._ui.songs_display.addTopLevelItem(new_item)
        for i in range(0, len(value)):
            self._ui.songs_display.resizeColumnToContents(i)
        self._ui.songs_display.hideColumn(len(item_text) - 1)
        self._ui.songs_display.repaint()
