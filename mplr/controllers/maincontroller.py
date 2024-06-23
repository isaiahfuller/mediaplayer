from PySide6.QtCore import QObject, Slot
from mplr.views.subsonic_login import SubsonicLogin
from mplr.controllers.subsonic_login_controller import SubsonicLoginController
from mplr.models.subsonic_login_model import SubsonicLoginModel
from threading import Thread


class MainController(QObject):
    def __init__(self, model) -> None:
        super().__init__()
        self._model = model

    @Slot(bool)
    def server_connection(self):
        subsonic_login_model = SubsonicLoginModel(self._model.subsonic)
        subsonic_login_controller = SubsonicLoginController(subsonic_login_model)
        self.dialog = SubsonicLogin(subsonic_login_model, subsonic_login_controller)
        self.dialog.show()
        self.dialog.accepted.connect(self.connection)

    def connection(self):
        print("connecting")
        self.dialog = None
        self.refresh()

    def refresh(self):
        print("get lists")
        # t = Thread(target=self.get_all_songs)
        t = Thread(target=self.get_all_artists)
        t.daemon = True
        t.start()

    def get_all_songs(self):
        songs = self._model.subsonic.getAllSongs()
        return songs

    def get_all_artists(self):
        artists = self._model.subsonic.getAllArtists()
        print(artists)
        print(len(artists))
        return artists
