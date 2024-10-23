from PySide6.QtWidgets import QListView

from .AbsItemView import AbsItemViewMix
from ..gui import StdModel


class ListView(AbsItemViewMix, QListView):
    def __init__(self, *, uniform_item_sizes=False, spacing=0, **kwargs):
        super().__init__(**kwargs)
        self.setSpacing(spacing)
        self.setUniformItemSizes(uniform_item_sizes)

    # def move_to_previous_row(self):
    #     """ 移动到上一行 """
    #     if (row := self.currentIndex().row()) <= 0:
    #         return
    #
    #     m = self.model()
    #     take_item = m.takeItem(row)  # 要移动的项目  移动到前一项
    #     previous_item = m.takeItem(row - 1, 0)  # 上一个项目
    #
    #     m.setItem(row, previous_item)
    #     m.setItem(row - 1, take_item)
    #     self.setCurrentIndex(take_item.index())
    #
    # def move_to_next_row(self):
    #     """ 移动到下一行 """
    #     m = self.model()
    #     row = self.currentIndex().row()
    #     if -1 == row or row >= m.rowCount() - 1:
    #         return
    #
    #     take_item = m.takeItem(row, 0)  # 要移动的项目
    #     next_item = m.takeItem(row + 1, 0)  # 下一个项目
    #
    #     m.setItem(row, next_item)
    #     m.setItem(row + 1, take_item)
    #     self.setCurrentIndex(take_item.index())

    def model(self) -> StdModel:
        return super().model()
