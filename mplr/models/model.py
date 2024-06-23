from PySide6.QtCore import QObject, Signal


class Model(QObject):
    subsonic_changed = Signal(bool)

    @property
    def subsonic(self):
        return self._subsonic

    @subsonic.setter
    def subsonic(self, value):
        self._subsonic = value
        self.subsonic_changed.emit(value)

    def __init__(self):
        super().__init__()
