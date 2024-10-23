from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QGradient, QColor, QBrush


class StdItem(QStandardItem):
    def __init__(self, data=None,
                 children: list['StdItem'] = None, *,
                 rows: int = None,
                 columns=1,
                 text_align: Qt.AlignmentFlag = None,
                 flags: Qt.ItemFlags = None,
                 enabled=True,
                 background: str | QBrush | QColor | Qt.GlobalColor | QGradient = None,
                 foreground: str | QBrush | QColor | Qt.GlobalColor | QGradient = None,
                 ):
        if rows is not None:
            super().__init__(rows, columns=columns)
        else:
            super().__init__()

        self.setEnabled(enabled)
        if background and isinstance(background, str):
            background = QColor(background)
        if foreground and isinstance(foreground, str):
            foreground = QColor(foreground)

        if flags is not None: self.setFlags(flags)
        if data: self.setData(data, Qt.DisplayRole)
        if text_align is not None: self.setTextAlignment(text_align)

        if foreground is not None: self.setForeground(foreground)
        if background is not None: self.setBackground(background)

        for x in children or []:
            self.appendRow(x)

    def setTextAlignment(self, align: Qt.AlignmentFlag) -> None:
        super().setTextAlignment(Qt.AlignmentFlag(align))

    def setForeground(self, brush: str | QBrush | QColor | Qt.GlobalColor | QGradient):
        brush = QColor(brush) if isinstance(brush, str) else brush
        super().setForeground(brush)

    def setBackground(self, brush: str | QBrush | QColor | Qt.GlobalColor | QGradient):
        brush = QColor(brush) if isinstance(brush, str) else brush
        super().setBackground(brush)
