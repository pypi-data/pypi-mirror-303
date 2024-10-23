from typing import Callable

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSystemTrayIcon, QMenu


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self,
                 menu: QMenu = None,
                 icon='',
                 tooltip='',
                 on_activated: Callable = None,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        if on_activated: self.activated.connect(on_activated)

        self.setIcon(QIcon(icon))
        self.setToolTip(tooltip)
        if menu:
            self.setContextMenu(menu)

        self.show()
