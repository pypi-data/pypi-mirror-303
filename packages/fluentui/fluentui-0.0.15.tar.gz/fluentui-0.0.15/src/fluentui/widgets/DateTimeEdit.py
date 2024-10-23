from __future__ import annotations

from PySide6.QtCore import QDate, QDateTime, QTime, QTimer
from PySide6.QtWidgets import QDateTimeEdit

from .Widget import WidgetMix


class DateTimeEdit(WidgetMix, QDateTimeEdit):
    def __init__(self, t: QDate | QDateTime | str = '', *,
                 calendar_popup=False,
                 display_format='yyyy-MM-dd HH:mm:ss',
                 **kwargs
                 ):
        if isinstance(t, str):
            t = QDateTime.fromString(t, display_format)
        elif isinstance(t, QDate):
            t = QDateTime(t, QTime())

        super().__init__(t or QDateTime(), **kwargs)
        self.setCalendarPopup(calendar_popup)

        if display_format:
            self.setDisplayFormat(display_format)

    def setDate(self, date: QDate | str) -> None:
        date = QDate.fromString(date) if isinstance(date, str) else date
        super().setDate(date)

    def setSelectedSection(self, section: QDateTimeEdit.Section) -> None:
        self.setFocus()
        QTimer.singleShot(0, lambda: self.super().setSelectedSection(section))
