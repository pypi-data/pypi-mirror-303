from typing import List, Callable

from PySide6.QtWidgets import QTabBar

from .Widget import WidgetMix


class TabBar(WidgetMix, QTabBar):
    def __init__(self,
                 tabs: List[str] = None,
                 on_current: Callable[[int], None] = None,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        if on_current: self.currentChanged.connect(on_current)
        for x in tabs or []: self.addTab(x)
