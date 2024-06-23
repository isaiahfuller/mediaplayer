from PySide6.QtCore import QObject, Signal


class Model(QObject):
    subsonic_changed = Signal(bool)
    songs_changed = Signal(list)
    artists_changed = Signal(list)
    albums_changed = Signal(list)
    genres_changed = Signal(list)

    @property
    def subsonic(self):
        return self._subsonic

    @subsonic.setter
    def subsonic(self, value):
        self._subsonic = value
        self.subsonic_changed.emit(value)

    @property
    def songs(self):
        return self._songs

    @songs.setter
    def songs(self, value):
        self._songs = value
        self.songs_changed.emit(value)

    @property
    def artists(self):
        return self._artists

    @artists.setter
    def artists(self, value):
        self._artists = value
        self.artists_changed.emit(value)

    @property
    def albums(self):
        return self._albums

    @albums.setter
    def albums(self, value):
        self._albums = value
        self.albums_changed.emit(value)

    @property
    def genres(self):
        return self._genres

    @genres.setter
    def genres(self, value):
        self._genres = value
        self.genres_changed.emit(value)

    def __init__(self):
        super().__init__()
