import os

os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]
import libopensonic  # noqa: E402
import locale  # noqa: E402
import libopensonic.connection  # noqa: E402
import mpv  # noqa: E402
import sys  # noqa: E402
from getpass import getpass  # noqa: E402
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget  # noqa: E402
from PySide6.QtCore import Qt  # noqa: E402


class Test(QMainWindow):
    def __init__(self, conn, parent=None, song_id=""):
        super().__init__(parent)
        self.container = QWidget(self)
        self.setCentralWidget(self.container)
        self.container.setAttribute(Qt.WA_DontCreateNativeAncestors)
        self.container.setAttribute(Qt.WA_NativeWindow)
        player = mpv.MPV(
            wid=str(int(self.container.winId())),
            log_handler=print,
            loglevel="debug",
        )
        song = conn.stream(song_id)
        print(song.content)
        player.play_bytes(song.content)


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
    songs = conn.getRandomSongs(size=2)
    song = songs[0].to_dict()
    print(song)
    app = QApplication(sys.argv)
    locale.setlocale(locale.LC_NUMERIC, "C")
    win = Test(conn=conn, song_id=song["id"])
    win.show()
    sys.exit(app.exec_())
