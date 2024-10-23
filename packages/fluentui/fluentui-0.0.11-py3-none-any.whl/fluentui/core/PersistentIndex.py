from PySide6.QtCore import QPersistentModelIndex, Qt, QModelIndex
from typing_extensions import TypeVar, Generic

T = TypeVar('T')


class PersistentIndex(QPersistentModelIndex, Generic[T]):
    def setData(self, value: object, role=Qt.ItemDataRole.EditRole) -> bool:
        if not (m := self.model()):
            return False
        return m.setData(self.index(), value, role)

    def siblingAtColumn(self, column: int) -> QModelIndex:
        return self.sibling(self.row(), column)

    def siblingAtRow(self, row: int) -> QModelIndex:
        return self.sibling(row, self.column())

    def index(self) -> QModelIndex:
        return QModelIndex(self)

    def data(self, role=Qt.ItemDataRole.DisplayRole) -> T:
        return super().data(role)
