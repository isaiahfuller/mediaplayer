import uuid
from PySide6.QtCore import QSettings
import libopensonic.connection
import keyring


class Subsonic:
    def __init__(self):
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
            print(f"Ping: {ping}")
            if ping is True:
                self.servers.append(
                    {
                        "uuid": uuid,
                        "url": url,
                        "port": port,
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

    def getAllAlbums(self):
        albums = self.connection.getAlbumList2(ltype="alphabeticalByName")
        for album in albums:
            print(album.to_dict())
