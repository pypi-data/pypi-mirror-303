from __future__ import annotations

from PySide6.QtCore import QAbstractTableModel, QObject, QModelIndex, Qt, QPersistentModelIndex
from polars import DataFrame

from .ColumnItem import ColumnItem
from ..core.AbsItemModel import AbsItemModelMix
from ..namespce import ItemDataRole


class ColumnModel(AbsItemModelMix, QAbstractTableModel):
    def __init__(self,
                 parent: QObject = None, *,
                 header: dict[str, type] = None,
                 ):
        super().__init__(parent=parent)
        self.df = DataFrame(schema=header)

    def rowCount(self, parent=QModelIndex()) -> int:
        """ 行数 """
        return self.df.height

    def columnCount(self, parent=QModelIndex()) -> int:
        """ 列数 """
        return self.df.width

    def headerData(self, section: int, axis: int, role=ItemDataRole.Display) -> object:
        """ 头数据 """
        if role == ItemDataRole.Display:
            return self.df.columns[section]
        return super().headerData(section, Qt.Orientation(axis), role)

    def removeRows(self, row: int, count: int, parent=QModelIndex()) -> None:
        """ 移除行 """
        self.beginRemoveRows(parent, row, row + count - 1)
        self.df = self.df[:row].extend(self.df[row + count:])
        self.endRemoveRows()
        return True

    def data(self, index: QModelIndex, role=ItemDataRole.Display) -> object:
        """ 项目数据 """
        if role in (ItemDataRole.Display, ItemDataRole.Edit):
            item: ColumnItem = self.df[index.row(), index.column()]
            return item.value
        return None

    def setData(self, index: QModelIndex, value: object, role=ItemDataRole.Edit) -> bool:
        """ 设置数据 """
        if role in (ItemDataRole.Display, ItemDataRole.Edit):
            self.df[index.row(), index.column()] = value
            self.dataChanged.emit(index, index, [role])
            return True
        return False

    def append(self, data: dict | list[dict] = None, row=-1, reserve_blank_row=False) -> None:
        """ 添加行 """
        reserve_blank_row = reserve_blank_row or data is None
        data = data or []
        data = data if isinstance(data, list) else [data]

        if reserve_blank_row:  # 追加空行
            if not data:
                type_dict = self.df.item(0, 0).__class__.__annotations__
            else:
                type_dict = {k: type(v) for k, v in data[0].items()}
            data.append({k: v() for k, v in type_dict.items()})

        first = row if row >= 0 else self.rowCount()
        last = first + len(data) - 1

        self.beginInsertRows(QModelIndex(), first, last)
        self._append_df(row, data, first)
        self.endInsertRows()

    def _append_df(self, row: int, data: list[dict[str, object]], first: int) -> None:
        df = DataFrame(
            {key: ColumnItem(value) for key, value in x.items()}
            for x in data
        )
        if row == -1:
            setattr(self, 'df', df) if self.df.is_empty() else self.df.extend(df)
        else:
            self.df = self.df[:first].extend([df, self.df[first:]])

    def __getattr__(self, index: int | QModelIndex | QPersistentModelIndex) -> dict[str, object]:
        row = index if isinstance(index, int) else index.row()
        return self.df.row(row, named=True)
