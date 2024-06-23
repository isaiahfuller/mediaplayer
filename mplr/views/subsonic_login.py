from PySide6.QtWidgets import QDialog
from mplr.views.subsonic_login_ui import Ui_SubsonicLogin


class SubsonicLogin(QDialog):
    def __init__(self, model, controller):
        super().__init__()
        self._model = model
        self._controller = controller
        self.setModal(True)
        self._ui = Ui_SubsonicLogin()
        self._ui.setupUi(self)

        self._ui.subsonic_url.textChanged.connect(self._controller.url)
        self._ui.subsonic_port.valueChanged.connect(self._controller.port)
        self._ui.subsonic_user.textChanged.connect(self._controller.uname)
        self._ui.subsonic_password.textChanged.connect(self._controller.pword)
        self._ui.subsonic_servers.currentIndexChanged.connect(
            self._controller.server_id
        )

        self._model.url_changed.connect(self._ui.subsonic_url.setText)
        self._model.uname_changed.connect(self._ui.subsonic_user.setText)
        self._model.pword_changed.connect(self._ui.subsonic_password.setText)
        self._model.port_changed.connect(self._ui.subsonic_port.setValue)

        for server in self._model.subsonic.servers:
            self._ui.subsonic_servers.addItem(str(server["uuid"]))
        if len(self._model.subsonic.servers) > 0:
            server = self._model.subsonic.servers[0]
            self._ui.subsonic_servers.setCurrentIndex(0)
            self._ui.subsonic_url.setText(server["url"])
            self._ui.subsonic_user.setText(server["username"])
            self._ui.subsonic_password.setText(server["password"])
            self._ui.subsonic_port.setValue(int(server["port"]))
        self._ui.subsonic_servers.addItem("New server...")
        self._ui.buttonBox.clicked.connect(self._controller.handle_click)
