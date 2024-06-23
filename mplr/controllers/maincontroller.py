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
        genres_thread = Thread(target=self.get_genres, daemon=True)
        artists_thread = Thread(target=self.get_all_artists, daemon=True)
        songs_thread = Thread(target=self.get_all_songs, daemon=True)
        albums_thread = Thread(target=self.get_all_albums, daemon=True)
        genres_thread.start()
        artists_thread.start()
        songs_thread.start()
        albums_thread.start()

    def get_all_songs(self):
        print("Getting songs...")
        songs = self._model.subsonic.getAllSongs()
        self._model.songs = songs
        return songs

    def get_all_artists(self):
        print("Getting artists...")
        artists = self._model.subsonic.getAllArtists()
        self._model.artists = artists
        return artists

    def get_genres(self):
        print("Getting genres...")
        genres = sorted(
            self._model.subsonic.getGenres()["genre"], key=lambda x: x["value"].lower()
        )
        self._model.genres = genres
        return genres

    def get_all_albums(self):
        print("Gerring albums...")
        albums = self._model.subsonic.getAllAlbums()
        self._model.albums = albums
        return albums
