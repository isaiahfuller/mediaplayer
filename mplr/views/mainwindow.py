from PySide6.QtWidgets import QMainWindow
from mplr.views.mainwindow_ui import Ui_MainWindow
import mpv
import locale


class MainView(QMainWindow):
    def __init__(self, model, main_controller, conn):
        super().__init__()
        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        songs = conn.getRandomSongs(size=2)
        song = songs[0].to_dict()
        print(song)
        # app = QApplication(sys.argv)
        locale.setlocale(locale.LC_NUMERIC, "C")
        song = conn.stream(song["id"])
        # print(song.content)
        player = mpv.MPV(
            wid=str(int(self._ui.player.winId())),
            log_handler=print,
            loglevel="debug",
        )
        player.play_bytes(song.content)
