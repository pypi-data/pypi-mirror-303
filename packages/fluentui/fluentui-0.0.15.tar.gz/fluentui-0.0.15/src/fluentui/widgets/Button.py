from typing import Self, Callable

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QPushButton, QCheckBox, QAbstractButton

from .Widget import WidgetMix

if (__abs_button := object) is None:
    __abs_button = QAbstractButton


class AbsButtonMix(WidgetMix, __abs_button):
    def __init__(self,
                 text: str = '', *,
                 icon: QIcon | str = None,
                 icon_size: int | tuple[int, int] = None,
                 checked=False,
                 checkable: bool = None,
                 auto_exclusive: bool = None,
                 on_toggled: Callable[[bool], None] = None,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        if on_toggled: self.toggled.connect(on_toggled)
        if auto_exclusive is not None: self.setAutoExclusive(auto_exclusive)
        if checkable is not None: self.setCheckable(checkable)

        self.setText(text)
        self.setChecked(checked)

        if icon_size is not None:
            if isinstance(icon_size, int): icon_size = (icon_size, icon_size)
            self.setIconSize(*icon_size)
        if icon: self.setIcon(icon)

    def setIcon(self: Self, icon: QIcon | QPixmap | str) -> None:
        icon = QIcon(icon) if isinstance(icon, str) else icon
        super().setIcon(icon)

    def setIconSize(self, w: int, h: int) -> None:
        super().setIconSize(QSize(w, h))

class Button(AbsButtonMix, QPushButton):
    def __init__(self, text='', *,
                 default: bool = None,
                 auto_default: bool = None,
                 **kwargs
                 ):
        super().__init__(text, **kwargs)
        if default is not None:
            self.setDefault(default)
        if auto_default is not None:
            self.setAutoDefault(auto_default)

    def setIcon(self, icon: str | QIcon) -> None:
        icon = QIcon(icon) if isinstance(icon, str) else icon
        super().setIcon(icon)


class SubtleButton(Button):
    def __init__(self, text='', **kwargs):
        super().__init__(text, **kwargs)
        self.setStyleSheet(
            'SubtleButton {\n'
            '    background: transparent;\n'
            '    border: none;\n'
            '    padding: 5\n'
            '}\n'
            ':hover { background: #f5f5f5 }\n'
            ':pressed { background: #e0e0e0 }'
        )


class CheckBox(AbsButtonMix, QCheckBox):
    ...
