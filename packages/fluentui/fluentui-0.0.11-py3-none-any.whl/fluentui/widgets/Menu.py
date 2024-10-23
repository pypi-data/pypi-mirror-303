from typing import Union, Iterable

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu

from .Widget import WidgetMix


class Menu(WidgetMix, QMenu):
    def __init__(self, title='', *,
                 actions: Union[QAction, Iterable[QAction]] = None,
                 **kwargs
                 ):
        super().__init__(title, **kwargs)
        self.addActions(actions or [])

    def addActions(self, a: Union[QAction, Iterable[QAction]]) -> None:
        for x in a if isinstance(a, Iterable) else [a]:
            if not self.parent():
                x.setParent(self)
            self.addAction(x)
