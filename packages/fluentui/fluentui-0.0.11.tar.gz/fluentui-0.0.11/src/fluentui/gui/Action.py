from typing import Callable

from PySide6.QtGui import QAction, QIcon, QPixmap

from ..core.Object import ObjectMix


class Action(ObjectMix, QAction):
    def __init__(self, text='',
                 icon: QIcon | QPixmap = None,
                 triggered: Callable[[bool], None] = None,
                 **kwargs):
        super().__init__(text, **kwargs)
        if icon is not None: self.setIcon(icon)
        if triggered: self.triggered.connect(triggered)
