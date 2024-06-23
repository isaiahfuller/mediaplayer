from PySide6.QtCore import QObject, Signal


class SubsonicLoginModel(QObject):
    """
    A model class for handling Subsonic login details and emitting signals when properties change.
    """

    url_changed = Signal(str)
    port_changed = Signal(int)
    uname_changed = Signal(str)
    pword_changed = Signal(str)
    server_id_changed = Signal(int)

    _uname = ""
    _pword = ""
    _url = ""
    _port = 4533
    _server_id = 0

    def __init__(self, subsonic):
        """
        Initialize the SubsonicLoginModel with a subsonic instance.

        :param subsonic: An instance of the Subsonic class.
        """
        super().__init__()
        self._subsonic = subsonic

    @property
    def url(self):
        """
        Get the URL of the Subsonic server.

        :return: The URL as a string.
        """
        return self._url

    @url.setter
    def url(self, value):
        """
        Set the URL of the Subsonic server and emit the url_changed signal.

        :param value: The new URL as a string.
        """
        self._url = value
        self.url_changed.emit(value)

    @property
    def uname(self):
        """
        Get the username for Subsonic login.

        :return: The username as a string.
        """
        return self._uname

    @uname.setter
    def uname(self, value):
        """
        Set the username for Subsonic login and emit the uname_changed signal.

        :param value: The new username as a string.
        """
        self._uname = value
        self.uname_changed.emit(value)

    @property
    def pword(self):
        """
        Get the password for Subsonic login.

        :return: The password as a string.
        """
        return self._pword

    @pword.setter
    def pword(self, value):
        """
        Set the password for Subsonic login and emit the pword_changed signal.

        :param value: The new password as a string.
        """
        self._pword = value
        self.pword_changed.emit(value)

    @property
    def port(self):
        """
        Get the port number for the Subsonic server.

        :return: The port number as an integer.
        """
        return self._port

    @port.setter
    def port(self, value):
        """
        Set the port number for the Subsonic server and emit the port_changed signal.

        :param value: The new port number as an integer.
        """
        self._port = value
        self.port_changed.emit(value)

    @property
    def server_id(self):
        """
        Get the server ID for the Subsonic server.

        :return: The server ID as an integer.
        """
        return self._server_id

    @server_id.setter
    def server_id(self, value):
        """
        Set the server ID for the Subsonic server and emit the server_id_changed signal.

        :param value: The new server ID as an integer.
        """
        self._server_id = value
        self.server_id_changed.emit(value)

    @property
    def subsonic(self):
        """
        Get the Subsonic instance.

        :return: The Subsonic instance.
        """
        return self._subsonic

    @subsonic.setter
    def subsonic(self, value):
        """
        Set the Subsonic instance.

        :param value: The new Subsonic instance.
        """
        self._subsonic = value

    @property
    def server_list(self):
        """
        Get the list of servers.

        :return: The list of servers.
        """
        return self._server_list

    @server_list.setter
    def server_list(self, value):
        """
        Set the list of servers.

        :param value: The new list of servers.
        """
        self._server_list = value
