from __future__ import annotations

from PySide6.QtCore import QAbstractItemModel, QModelIndex

from .PersistentIndex import PersistentIndex


class AbsItemModelMix:
    def index(self, row: int | QModelIndex, column: int = None, parent=QModelIndex()) -> QModelIndex:
        if isinstance(row, QModelIndex):
            column = row.column() if column is None else column
            row = row.row()
        return super().index(row, 0 if column is None else column, parent)

    def hasIndex(self, row: int, column=0, parent=QModelIndex()) -> bool:
        return super().hasIndex(row, column, parent)

    def createPersistentIndex(self, row: int, column=0, obj=None) -> PersistentIndex:
        return PersistentIndex(self.createIndex(row, column, obj))

    def createIndex(self, row: int, column=0, obj=None) -> QModelIndex:
        return super().createIndex(row, column, obj)


class AbsItemModel(AbsItemModelMix, QAbstractItemModel):
    ...
