import os

os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]
import libopensonic  # noqa: E402
import libopensonic.connection  # noqa: E402
import sys  # noqa: E402
from getpass import getpass  # noqa: E402
from PySide6.QtWidgets import QApplication  # noqa: E402
from mplr.views.mainwindow import MainView
from mplr.controllers.maincontroller import MainController
from mplr.models.model import Model


class Test(QApplication):
    def __init__(self, conn):
        super().__init__()
        self.model = Model()
        self.main_controller = MainController(model=self.model)
        self.main_view = MainView(
            model=self.model, main_controller=self.main_controller, conn=conn
        )
        self.main_view.show()


if __name__ == "__main__":
    server_address = input("server addr ")
    port = input("server port ")
    uname = input("server uname ")
    pword = getpass("server pword ")
    conn = libopensonic.connection.Connection(
        baseUrl=server_address,
        username=uname,
        password=pword,
        port=port,
    )
    app = Test(conn=conn)
    sys.exit(app.exec_())
