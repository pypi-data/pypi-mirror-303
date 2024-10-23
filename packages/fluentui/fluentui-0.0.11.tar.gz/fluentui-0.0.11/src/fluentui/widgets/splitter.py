from typing import List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QSplitter

from .frame import FrameMix


class Splitter(FrameMix, QSplitter):
    def __init__(self, *, split: List[QWidget] = None,
                 sizes: List[int] = None,
                 handle_width=5,
                 children_collapsible=True,
                 orientation=Qt.Orientation.Horizontal,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.setOrientation(orientation)
        self.setHandleWidth(handle_width)
        self.setChildrenCollapsible(children_collapsible)

        if sizes is not None: self.setSizes(sizes or [])
        for x in split or []: self.addWidget(x)
