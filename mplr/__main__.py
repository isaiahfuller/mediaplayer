import sys
from PySide6.QtWidgets import QApplication
from mplr.views.mainwindow import MainView
from mplr.controllers.maincontroller import MainController
from mplr.models.model import Model
# from getpass import getpass


class Test(QApplication):
    def __init__(self):
        super().__init__()
        self.model = Model()
        self.main_controller = MainController(model=self.model)
        self.main_view = MainView(
            model=self.model, main_controller=self.main_controller
        )
        self.main_view.show()


if __name__ == "__main__":
    # server_address = input("server addr ")
    # port = input("server port ")
    # uname = input("server uname ")
    # pword = getpass("server pword ")
    # conn = libopensonic.connection.Connection(
    #     baseUrl=server_address,
    #     username=uname,
    #     password=pword,
    #     port=port,
    # )
    app = Test()
    sys.exit(app.exec())
