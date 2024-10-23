from typing import Callable

from PySide6.QtCore import Qt, Signal, QMetaMethod
from PySide6.QtGui import QCloseEvent, QKeyEvent, QMouseEvent, QShowEvent
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QLayout

from .layout import Layout
from ..core import ObjectMix
from ..gui import Font

if (__widget := object) is None:
    __widget = QWidget


class WidgetMix(ObjectMix, Layout, __widget):
    on_close = Signal()
    on_key_enter_pressed = Signal()
    on_clicked = Signal(QWidget, QMouseEvent)

    def __init__(
            # a、b、c、d、e、f、g、h、i、j、k、l、m、n、o、p、q、r、s、t、u、v、w、x、y、z
            self, *args,
            attrs: Qt.WidgetAttribute | set[Qt.WidgetAttribute | set[Qt.WidgetAttribute]] = None,
            children: QLayout = None,
            drop_shadow_effect: QGraphicsDropShadowEffect = None,
            font: Font = None,
            key='',
            mouse_tracking: bool = None,
            parent: QWidget = None,
            size: tuple[int, int] | int = None,
            width: int = None,
            height: int = None,
            win_title='',
            win_flags: Qt.WindowType = None,
            closed: Callable = None,
            clicked: Callable[[QWidget], QMouseEvent] = None,
            key_enter_pressed: Callable = None,
            **kwargs
    ):
        self.__is_pressed = False

        super().__init__(parent=parent, *args, **kwargs)
        self.setObjectName(key)
        self.setWindowTitle(win_title)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        if closed: self.on_close.connect(closed)
        if clicked: self.on_clicked.connect(clicked)
        if key_enter_pressed: self.on_key_enter_pressed.connect(key_enter_pressed)

        if font is not None: self.setFont(font)
        if win_flags is not None: self.setWindowFlags(win_flags)
        if mouse_tracking is not None: self.setMouseTracking(mouse_tracking)
        if drop_shadow_effect is not None: self.setGraphicsEffect(drop_shadow_effect)

        if size is not None:
            self._init_size = size if isinstance(size, tuple) else (size, size)
        elif all(x is not None for x in [width, height]):
            self._init_size = (width, height)
        elif width is not None:
            self._init_size = (width, -1)
        elif height is not None:
            self._init_size = (-1, height)

        if attrs is not None:
            for x in attrs if isinstance(attrs, set) else {attrs}:
                if isinstance(x, set):
                    for a in x: self.setAttribute(a, False)
                    continue
                self.setAttribute(x)

        if children is not None:
            self.setLayout(children)

    def showEvent(self, e: QShowEvent) -> None:
        super().showEvent(e)
        if size := getattr(self, '_init_size', None):
            w = self.width() if size[0] == -1 else size[0]
            h = self.height() if size[1] == -1 else size[1]
            if (parent := self.parent()) and parent.layout():
                if self in parent.children():
                    self.setFixedSize(w, h)
            else:
                self.resize(w, h)
            delattr(self, '_init_size')

    def closeEvent(self, e: QCloseEvent) -> None:
        super().closeEvent(e)
        self.on_close.emit()

    def keyPressEvent(self, e: QKeyEvent) -> None:
        super().keyPressEvent(e)
        self.on_key_enter_pressed.emit()

    def mousePressEvent(self, e: QMouseEvent) -> None:
        super().mousePressEvent(e)
        self.__is_pressed = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        super().mouseReleaseEvent(e)
        if self.__is_pressed:
            self.__is_pressed = False
            if self.isSignalConnected(QMetaMethod.fromSignal(self.on_clicked)):
                self.on_clicked.emit(self, e)


class Widget(WidgetMix, QWidget):
    ...
