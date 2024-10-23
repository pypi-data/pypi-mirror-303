from __future__ import annotations

from polars import DataFrame, Series, Object
from typing_extensions import Generic, TypeVar, List, Dict, Callable, Optional

from .ColumnModel import ColumnModel, QModelIndex
from ..core import PersistentIndex

T = TypeVar('T')


class RowModel(ColumnModel, Generic[T]):
    def __init__(self, factory: Callable[..., T],
                 rows: List[Dict[str, object]] = None,
                 reserve_blank_row=False,
                 **kwargs
                 ) -> None:
        self.__class__.factory = factory
        super().__init__(**kwargs)
        if rows:
            self.append(rows, reserve_blank_row=reserve_blank_row)

    def columnCount(self, parent=QModelIndex()) -> int:
        return 1

    def removeRows(self, row: int, count: int, parent=QModelIndex()) -> None:
        """ 移除行 """
        self.beginRemoveRows(parent, row, row + count - 1)
        self.df = self.df[:row].vstack(self.df[row + count:])
        self.endRemoveRows()
        return True

    def data(self, index: QModelIndex, role=ItemDataRole.Display) -> Optional[T]:
        """ 项目数据 """
        if role in (ItemDataRole.Display, ItemDataRole.Edit):
            item = self.df[index.row(), index.column()]
            return getattr(item, 'text', '') if role == ItemDataRole.Display else item
        return super().data(index, role)

    def setData(self, index: QModelIndex, value: object, role=ItemDataRole.Edit) -> bool:
        """ 设置数据 """
        succeed = role in (ItemDataRole.Display, ItemDataRole.Edit)
        if succeed:
            self.df[index.row(), index.column()] = value
            self.dataChanged.emit(index, index, [role])
        return succeed

    def _append_df(self, row: int, data: List[Dict[str, object]], first: int) -> None:
        df = DataFrame(Series([self.factory(**x) for x in data], dtype=Object))
        if row == -1 or self.rowCount() == 0:
            setattr(self, 'df', df if self.df.is_empty() else self.df.vstack(df))
        else:
            self.df = self.df[:first].vstack(df).vstack(self.df[first:])

    def __getitem__(self, index: int | QModelIndex | PersistentIndex) -> Optional[T]:
        if self.df.is_empty():
            return None
        row = index if isinstance(index, int) else index.row()
        return self.df.item(row, 0)

    def factory(self, *args, **kwargs) -> T:
        """ 项目工厂 """
