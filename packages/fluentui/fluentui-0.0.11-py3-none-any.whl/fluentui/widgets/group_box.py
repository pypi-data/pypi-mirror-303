from PySide6.QtWidgets import QGroupBox

from .Widget import WidgetMix


class GroupBox(WidgetMix, QGroupBox):
    def __init__(self, title='', **kwargs):
        super().__init__(title, **kwargs)
