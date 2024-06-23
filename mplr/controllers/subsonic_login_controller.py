from PySide6.QtCore import QObject, Slot


class SubsonicLoginController(QObject):
    """
    Controller class for handling Subsonic login operations.

    Attributes:
        _model: The model object containing login information and server details.
    """

    def __init__(self, model):
        """
        Initializes the SubsonicLoginController with the given model.

        Args:
            model: The model object containing login information and server details.
        """
        super().__init__()
        self._model = model

    @Slot(str)
    def url(self, value):
        """
        Slot to set the URL in the model.

        Args:
            value (str): The URL to be set.
        """
        self._model.url = value

    @Slot(int)
    def port(self, value):
        """
        Slot to set the port in the model.

        Args:
            value (int): The port number to be set.
        """
        self._model.port = value

    @Slot(str)
    def uname(self, value):
        """
        Slot to set the username in the model.

        Args:
            value (str): The username to be set.
        """
        self._model.uname = value

    @Slot(str)
    def pword(self, value):
        """
        Slot to set the password in the model.

        Args:
            value (str): The password to be set.
        """
        self._model.pword = value

    @Slot(str)
    def server_id(self, value):
        """
        Slot to set the server ID in the model and update login information accordingly.

        Args:
            value (str): The server ID to be set.
        """
        self._model.server_id = value
        if value >= len(self._model.subsonic.servers):
            self._model.uname = ""
            self._model.pword = ""
            self._model.url = "http://127.0.0.1"
            self._model.port = 4533
        else:
            server = self._model.subsonic.servers[value]
            self._model.uname = server["username"]
            self._model.pword = server["password"]
            self._model.url = server["url"]
            self._model.port = server["port"]

    def handle_click(self):
        """
        Handles the click event to set login information and add a new server if necessary.
        """
        self._model.subsonic.setLoginInformation(
            username=self._model.uname,
            password=self._model.pword,
            address=self._model.url,
            port=self._model.port,
        )
        if self._model.server_id >= len(self._model.subsonic.servers):
            self._model.subsonic.addNewServer(
                username=self._model.uname,
                password=self._model.pword,
                address=self._model.url,
                port=self._model.port,
            )
