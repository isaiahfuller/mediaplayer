from PySide6.QtCore import QObject
import mpv
import locale

class Player(QObject):
    def __init__(self, model):
        super().__init__()
        locale.setlocale(locale.LC_NUMERIC, "C")
        self._model = model
        self.mpv = mpv.MPV(video=False)
        self.mpv_init()

    def mpv_init(self):
        self.mpv.terminate()
        self.mpv = mpv.MPV(video=False)
        self.mpv.observe_property("playback-time", self.on_duration_changed)
        self.mpv.observe_property("pause", self.on_pause_changed)
        self.mpv.observe_property("volume", self.on_volume_changed)

    def play_song(self, stream):
        self.mpv_init()
        # self.mpv.play_bytes(stream.content)
        self.mpv.play(stream)

    def play_pause_toggle(self):
        self.mpv.pause = not self.mpv.pause

    def on_duration_changed(self, name, value):
        print(f"Duration changed: {value}")
        if value is not None:
            self._model.player_duration = value

    def on_pause_changed(self, name, value):
        print(f"Pause state changed: {value}")
        if value is not None:
            """"""
            # Handle pause state change

    def on_volume_changed(self, name, value):
        print(f"Volume changed: {value}")
        if value is not None:
            """"""
            # Handle volume change
