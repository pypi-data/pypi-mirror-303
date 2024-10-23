from PySide6.QtCore import QPersistentModelIndex, Qt, QModelIndex


class PersistentIndex(QPersistentModelIndex):
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
