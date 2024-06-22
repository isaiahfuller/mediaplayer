from PySide6.QtCore import QObject, Signal


class Model(QObject):
    subsonic_changed = Signal(bool)
    list_artists_changed = Signal(list)
    list_albums_changed = Signal(list)
    list_genres_changed = Signal(list)

    @property
    def subsonic(self):
        return self._subsonic

    @subsonic.setter
    def subsonic(self, value):
        self._subsonic = value
        self.subsonic_changed.emit(value)

    @property
    def list_artists(self):
        return self._list_artists

    @list_artists.setter
    def list_artists(self, value):
        self._list_artists = value
        self.list_artists_changed.emit(value)

    @property
    def list_albums(self):
        return self._list_albums

    @list_albums.setter
    def list_albums(self, value):
        self._list_albums = value
        self.list_albums_changed.emit(value)

    @property
    def list_genres(self):
        return self._list_genres

    @list_genres.setter
    def list_genres(self, value):
        print("list genres changed")
        self._list_genres = value
        self.list_genres_changed.emit(value)

    def __init__(self):
        super().__init__()
