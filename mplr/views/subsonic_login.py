from PySide6.QtWidgets import QDialog
from mplr.views.subsonic_login_ui import Ui_SubsonicLogin
from mplr.connection.subsonic import Subsonic


class SubsonicLogin(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self._ui = Ui_SubsonicLogin()
        self._ui.setupUi(self)
        self.subsonic = Subsonic()
        for server in self.subsonic.servers:
            self._ui.subsonic_servers.addItem(str(server["uuid"]))
        if len(self.subsonic.servers) > 0:
            server = self.subsonic.servers[0]
            self._ui.subsonic_servers.setCurrentIndex(0)
            self._ui.subsonic_url.setText(server["url"])
            self._ui.subsonic_user.setText(server["username"])
            self._ui.subsonic_password.setText(server["password"])
            self._ui.subsonic_port.setValue(int(server["port"]))
        self._ui.subsonic_servers.addItem("New server...")
        self._ui.buttonBox.clicked.connect(self.handle_click)

    def handle_click(self):
        print("nui")
        self.uname = self._ui.subsonic_user.text()
        self.pword = self._ui.subsonic_password.text()
        self.url = self._ui.subsonic_url.text()
        self.port = self._ui.subsonic_port.text()
        self.subsonic.setLoginInformation(
            username=self.uname,
            password=self.pword,
            address=self.url,
            port=self.port,
        )
        if self._ui.subsonic_servers.currentText() == "New server...":
            self.subsonic.addNewServer(
                username=self.uname,
                password=self.pword,
                address=self.url,
                port=self.port,
            )
