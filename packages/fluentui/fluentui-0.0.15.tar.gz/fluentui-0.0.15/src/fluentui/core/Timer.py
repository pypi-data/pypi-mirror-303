from typing import Callable

from PySide6.QtCore import QTimer


class Timer(QTimer):
    def __init__(self, interval=0, *, single_shot=False, timeout: Callable = None, parent=None):
        super().__init__(parent)
        self.setSingleShot(single_shot)
        self.setInterval(interval)
        if timeout is not None: self.timeout.connect(timeout)
