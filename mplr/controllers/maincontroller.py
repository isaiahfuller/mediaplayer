from PySide6.QtCore import QObject


class MainController(QObject):
    def __init__(self, model) -> None:
        super().__init__()
        self._model = model
