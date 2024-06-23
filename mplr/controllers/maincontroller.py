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

    @Slot()
    def play_song(self, item, col):
        song = self._model.subsonic.getSong(item.text(4))
        stream = self._model.subsonic.getStream(song)
        self._model.current_song = song
        play_song = Thread(
            target=self._model.player.play_song, args=(stream,), daemon=True
        )
        play_song.start()

    @Slot()
    def player_pause(self):
        self._model.player.play_pause_toggle()

    def connection(self):
        self.dialog = None
        self.refresh()

    def refresh(self):
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
        songs.sort(key=lambda x: x["track"])
        songs.sort(key=lambda x: x["album"])
        songs = sorted(songs, key=lambda x: x["artist"].lower())
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
