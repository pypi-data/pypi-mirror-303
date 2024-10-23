from PySide6.QtCore import Qt
from PySide6.QtWidgets import QScrollArea

from .frame import FrameMix


class ScrollAreaMix(FrameMix):
    def __init__(self: QScrollArea, *,
                 hor_scroll_policy=Qt.ScrollBarPolicy.ScrollBarAsNeeded,
                 ver_scroll_policy=Qt.ScrollBarPolicy.ScrollBarAsNeeded,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.setHorizontalScrollBarPolicy(hor_scroll_policy)
        self.setVerticalScrollBarPolicy(ver_scroll_policy)
