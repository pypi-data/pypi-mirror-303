from typing import Callable

from PySide6.QtCore import QModelIndex, QAbstractItemModel, QItemSelectionModel
from PySide6.QtWidgets import QAbstractItemView, QAbstractItemDelegate

from .ScrollArea import AbsScrollAreaMix

if (__abs_item_view := object) is not None:
    __abs_item_view = QAbstractItemView


class AbsItemViewMix(AbsScrollAreaMix, __abs_item_view):
    def __init__(self, *,
                 model: QAbstractItemModel = None,
                 auto_scroll=False,
                 auto_scroll_margin=16,
                 edit_triggers=QAbstractItemView.EditTrigger.NoEditTriggers,
                 selection_behavior=QAbstractItemView.SelectionBehavior.SelectRows,
                 selection_mode=QAbstractItemView.SelectionMode.SingleSelection,
                 hor_scroll_mode=QAbstractItemView.ScrollMode.ScrollPerPixel,
                 ver_scroll_mode=QAbstractItemView.ScrollMode.ScrollPerPixel,
                 hor_single_step: int = None,  # 滚动速度，通常对应于用户按下 [箭头键]
                 ver_single_step: int = None,
                 selection_model: QItemSelectionModel = None,
                 delegate: QAbstractItemDelegate = None,
                 cell_clicked: Callable[[QModelIndex], None] = None,
                 double_clicked: Callable[[QModelIndex], None] = None,
                 row_changed: Callable[[QModelIndex, QModelIndex], None] = None,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        if cell_clicked: self.clicked.connect(cell_clicked)
        if double_clicked: self.doubleClicked.connect(double_clicked)

        self.setAutoScroll(auto_scroll)
        self.setEditTriggers(edit_triggers)
        self.setAutoScrollMargin(auto_scroll_margin if auto_scroll else 0)
        self.setHorizontalScrollMode(hor_scroll_mode)
        self.setVerticalScrollMode(ver_scroll_mode)
        self.setSelectionBehavior(selection_behavior)
        self.setSelectionMode(selection_mode)

        if hor_single_step is not None: self.horizontalScrollBar().setSingleStep(hor_single_step)
        if ver_single_step is not None: self.verticalScrollBar().setSingleStep(ver_single_step)
        if selection_model is not None: self.setSelectionModel(selection_model)
        if model is not None: self.setModel(model)
        if row_changed: self.selectionModel().currentRowChanged.connect(row_changed)
        if delegate: self.setItemDelegate(delegate)
