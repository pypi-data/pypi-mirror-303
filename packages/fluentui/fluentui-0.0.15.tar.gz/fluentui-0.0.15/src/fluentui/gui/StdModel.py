from __future__ import annotations

from typing import Iterable

from PySide6.QtCore import QObject, Qt, QModelIndex
from PySide6.QtGui import QStandardItemModel

from ..core.AbsItemModel import AbsItemModelMix
from ..gui import StdItem


class StdModel(AbsItemModelMix, QStandardItemModel):
    def __init__(self,
                 parent: QObject = None,
                 rows: int = None,
                 columns: int = None,
                 default_role: dict[Qt.ItemDataRole, object] = None,
                 items: Iterable[StdItem] = None
                 ):
        if rows is not None and columns is not None:
            super().__init__(rows, columns, parent)
        else:
            super().__init__(parent)
        self.appendRow(items or [])
        self.default_role = default_role or {}

    def appendRow(self, items: StdItem | Iterable[StdItem]) -> None:
        for x in items if isinstance(items, Iterable) else [items]:
            super().appendRow(x)

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole) -> object:
        data = super().data(index, role)
        if role == Qt.ItemDataRole.TextAlignmentRole and not data:
            return self.default_role.get(role, None)
        return data
