import uuid
from PySide6.QtCore import QSettings, QObject
import libopensonic.connection
import keyring


class Subsonic(QObject):
    def __init__(self):
        """
        Initializes the music player settings and server connections.

        This method reads the server configurations from QSettings and attempts to
        establish connections to each server. If a server responds to a ping, it is
        added to the list of active servers.

        Attributes:
            servers (list): A list to store active server configurations.
        """
        super().__init__()
        settings = QSettings("Isaiah Fuller", "musicplayer")
        self.servers = []
        size = settings.beginReadArray("servers")
        for i in range(0, size):
            settings.setArrayIndex(i)
            uuid = settings.value("uuid")
            url = settings.value("url")
            port = settings.value("port")
            uname = settings.value("uname")
            pword = keyring.get_password(str(uuid), uname)
            new_server = libopensonic.connection.Connection(
                baseUrl=url, username=uname, password=pword, port=port
            )
            ping = new_server.ping()
            if ping is True:
                self.servers.append(
                    {
                        "uuid": str(uuid),
                        "url": url,
                        "port": int(port),
                        "username": uname,
                        "password": pword,
                    }
                )
        settings.endArray()

    def setLoginInformation(self, address, username, password, port=4533):
        self.connection = libopensonic.connection.Connection(
            baseUrl=address, username=username, password=password, port=port
        )

    def addNewServer(self, address, username, password, port):
        """
        Adds a new server to the list of servers and saves the configuration.

        Parameters:
        address (str): The address of the new server.
        username (str): The username for the new server.
        password (str): The password for the new server.
        port (int): The port number for the new server.

        Returns:
        None
        """
        settings = QSettings("Isaiah Fuller", "musicplayer")
        settings.beginWriteArray("servers")
        for i in range(0, len(self.servers)):
            settings.setArrayIndex(i)
            settings.setValue("uuid", self.servers[i].uuid)
            settings.setValue("url", self.servers[i].url)
            settings.setValue("port", self.servers[i].port)
            settings.setValue("uname", self.servers[i].uname)
            keyring.set_password(
                self.servers[i].uuid, self.servers[i].uname, self.servers[i].pword
            )
        settings.setArrayIndex(len(self.servers))
        new_uuid = uuid.uuid4()
        settings.setValue("uuid", new_uuid)
        settings.setValue("url", address)
        settings.setValue("port", port)
        settings.setValue("uname", username)
        keyring.set_password(str(new_uuid), username=username, password=password)
        settings.endArray()

    def getStream(self, song):
        if song["suffix"] == "m4a":
            return self.connection.stream(sid=song["id"], tformat="mp3")
        return self.connection.stream(sid=song["id"])

    def getSong(self, id):
        song = self.connection.getSong(id).to_dict()
        return song

    def getAllAlbums(self):
        """
        Retrieves all albums from the connection in an alphabetical order by name.

        This method fetches albums in batches of 500 until no more albums are available.
        Each album is converted to a dictionary and added to the all_albums list.

        Returns:
            list: A list of dictionaries, each representing an album.
        """
        all_albums = []
        i = 0
        while True:
            res = self.connection.getAlbumList2(
                ltype="alphabeticalByName", size=500, offset=500 * i
            )
            for album in res:
                all_albums.append(album.to_dict())
            i += 1
            if len(res) < 500:
                break

        return all_albums

    def getAllSongs(self):
        """
        Retrieves all songs from the connection in batches of 500 until no more songs are found.

        Returns:
            list: A list of dictionaries, each representing a song.
        """
        offset = 0
        songs = []
        while True:
            res = self.connection.search3(
                "",
                artistCount=0,
                artistOffset=0,
                albumCount=0,
                albumOffset=0,
                songCount=500,
                songOffset=offset,
            )
            for song in res["songs"]:
                songs.append(song.to_dict())
            if res["songs"] is None or len(res["songs"]) < 500:
                break
            offset += 500
        return songs

    def getGenres(self):
        """
        Retrieves a list of genres from the database connection, formatted as
        a list of dictionaries including the numbers of songs and albums tagged with
        the genre

        Returns:
            list: A list of genres retrieved from the database.
        """
        res = self.connection.getGenres()
        return res["genres"]

    def getAllArtists(self):
        """
        Retrieves all artists from the database.

        This method fetches artists grouped by their starting letter from the database,
        then flattens the list and converts each artist to a dictionary format.

        Returns:
            list: A list of dictionaries, each representing an artist.
        """
        res = self.connection.getArtists()
        artists = []
        for letter in res:
            for artist in letter.artists:
                artists.append(artist.to_dict())
        return artists
