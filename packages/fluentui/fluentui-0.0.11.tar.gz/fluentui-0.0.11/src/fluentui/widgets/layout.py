from PySide6.QtCore import Qt
from PySide6.QtWidgets import QBoxLayout, QLayout, QWidget, QGridLayout

from ..core import Margins


class Spacing(int): ...


class Stretch(int): ...


class Layout:
    def __init__(self, *args,
                 parent=None,
                 spacing=0,
                 margin='0',
                 row_span=1,
                 column_span=1,
                 self_align=Qt.AlignmentFlag(0),
                 **kwargs):
        super().__init__(parent=parent, *args, **kwargs)
        self.row_span = row_span
        self.column_span = column_span
        self.self_align = self_align
        if isinstance(self, QLayout):
            self.setSpacing(spacing)
            self.setContentsMargins(Margins(margin))


class BoxLayout(Layout, QBoxLayout):
    def __init__(self, dir_: QBoxLayout.Direction,
                 body: QLayout | QWidget | Stretch | Spacing | list = None,
                 **kwargs):
        super().__init__(dir_, **kwargs)
        if body is not None:
            for x in body if isinstance(body, list) else [body]:
                self.addWidget(x)

    def addWidget(self,
                  item: QLayout | QWidget | Stretch | Spacing | list,
                  alignment=Qt.AlignmentFlag(0)) -> None:
        if isinstance(item, QLayout):
            return self.addLayout(item)
        if isinstance(item, Stretch):
            return self.addStretch(item)
        if isinstance(item, Spacing):
            return self.addSpacing(item)

        if isinstance(item, Layout):
            alignment = item.self_align
        super().addWidget(item, alignment=alignment)


class Row(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(QBoxLayout.Direction.LeftToRight, **kwargs)


class Column(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(QBoxLayout.Direction.TopToBottom, **kwargs)


class Grid(Layout, QGridLayout):
    def __init__(self, body: list[QWidget | QLayout] = None, **kwargs):
        super().__init__(**kwargs)
        for row, x in enumerate(body):
            if isinstance(x, list):
                for column, y in enumerate(x):
                    self.addWidget(y, row, column)
                continue
            self.addWidget(x, row, 0)

    def addWidget(self, w: QWidget | QLayout,
                  row: int, column=0,
                  row_span=1, column_span=1,
                  alignment=Qt.AlignmentFlag(0)):
        if isinstance(w, Layout):
            row_span, column_span = w.row_span, w.column_span

        if isinstance(w, QWidget):
            super().addWidget(w, row, column, row_span, column_span, alignment)
            return
        self.addLayout(w, row, column, row_span, column_span, alignment)
