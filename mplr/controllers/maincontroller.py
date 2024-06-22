from PySide6.QtCore import QObject, Slot
from mplr.views.subsonic_login import SubsonicLogin
from mplr.connection.subsonic import Subsonic


class MainController(QObject):
    def __init__(self, model) -> None:
        super().__init__()
        self._model = model
        self._model.subsonic_changed.connect(self.get_lists)

    @Slot(bool)
    def server_connection(self):
        self.dialog = SubsonicLogin()
        self.dialog.show()
        self.dialog.accepted.connect(self.connection)

    def connection(self):
        print("connecting")
        subsonic = Subsonic()
        # print(subsonic.connection.ping())
        self.dialog = None
        self._model.subsonic = subsonic

    def get_lists(self):
        print("get lists")
        # subsonic = self._model.subsonic
        # subsonic.getAllAlbums()
        # albums = []
        # artists = []
        # genres = []
        # for artist_idx in subsonic.getArtists():
        #     for artist in artist_idx.artists:
        #         artists.append(artist.to_dict())
        # for album in subsonic.getAlbumList2(ltype="alphabeticalByName"):
        #     albums.append(album.to_dict())
        # for genre in subsonic.getGenres()["genres"]["genre"]:
        #     genres.append(genre["value"])
        # self._model.list_artists = artists
        # self._model.list_albums = albums
        # self._model.list_genres = genres
        # print(albums)
        # print(artists)
        # print(genres)
