from typing import List, Tuple, Callable

from PySide6.QtWidgets import QTabWidget, QWidget

from .Widget import WidgetMix


class TabWidget(WidgetMix, QTabWidget):
    def __init__(self, *,
                 tab: List[Tuple[str, QWidget]] = None,
                 position=QTabWidget.TabPosition.North,
                 on_current: Callable[[int], None] = None,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        if on_current: self.currentChanged.connect(on_current)

        self.setTabPosition(position)
        for x in tab or []: self.addTab(x[1], x[0], )
