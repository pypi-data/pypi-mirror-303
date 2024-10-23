from PySide6.QtCore import Qt
from PySide6.QtWidgets import QScrollArea, QAbstractScrollArea

from .frame import FrameMix

if (__abs_scroll_area := object) is None:
    __abs_scroll_area = QAbstractScrollArea


class AbsScrollAreaMix(FrameMix, __abs_scroll_area):
    def __init__(self, *,
                 hor_scroll_bar_policy=Qt.ScrollBarPolicy.ScrollBarAsNeeded,
                 ver_scroll_bar_policy=Qt.ScrollBarPolicy.ScrollBarAsNeeded,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.setHorizontalScrollBarPolicy(hor_scroll_bar_policy)
        self.setVerticalScrollBarPolicy(ver_scroll_bar_policy)


class ScrollArea(AbsScrollAreaMix, QScrollArea):
    ...
