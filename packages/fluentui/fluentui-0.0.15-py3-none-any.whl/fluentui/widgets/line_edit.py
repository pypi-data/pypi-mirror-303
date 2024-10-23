from typing import Callable

from PySide6.QtWidgets import QLineEdit

from .Widget import WidgetMix


class LineEdit(WidgetMix, QLineEdit):
    def __init__(self, text: str | int = '', *,
                 read_only=False,
                 text_changed: Callable[[str], None] = None,
                 **kwargs
                 ):
        super().__init__(f'{text}', **kwargs)
        if text_changed: self.textChanged.connect(text_changed)
        self.setReadOnly(read_only)

    def setText(self, text: str | int) -> None:
        super().setText(f'{text}')
