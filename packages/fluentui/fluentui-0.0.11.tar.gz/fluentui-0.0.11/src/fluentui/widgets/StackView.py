from typing import List

from PySide6.QtWidgets import QStackedWidget, QWidget

from .Widget import WidgetMix


class StackView(WidgetMix, QStackedWidget):
    def __init__(self, stack: List[QWidget] = None, **kwargs):
        super().__init__(**kwargs)
        for x in stack or []: self.addWidget(x)
