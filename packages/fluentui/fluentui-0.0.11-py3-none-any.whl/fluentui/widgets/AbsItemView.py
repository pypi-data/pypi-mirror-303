from __future__ import annotations

from enum import Flag, Enum

from PySide6.QtCore import QModelIndex, Signal, QAbstractItemModel, QSize, QLocale
from PySide6.QtWidgets import QAbstractItemView, QTableWidget, QWidget, QStyleOptionViewItem
from typing_extensions import Optional, Callable, Self

from .ItemDelegate import ItemDelegate
from .ScrollArea import ScrollAreaMix
from ..core import PersistentIndex, AbsItemModel
from ..gui import StdModel


class AbsItemView(ScrollAreaMix, QAbstractItemView):
    class EditTrigger(Flag):
        No = 0
        CurrentChanged = 1
        DoubleClicked = 2
        Clicked = 4
        EditKey = 8
        AnyKey = 16
        All = 30

    class ScrollMode(Enum):
        PerItem = 0
        PerPixel = 1

    class SelectionBehavior(Enum):
        Items = 0
        Rows = 1
        Columns = 2

    class SelectionMode(Enum):
        No = 0
        Single = 1
        Multi = 2
        Extended = 3
        Contiguous = 4

    class ScrollHint(Enum):
        Visible = 0
        Top = 1
        Bottom = 2
        Center = 3


class AbsItemViewMix(ScrollAreaMix):
    on_rows_inserted = Signal(QModelIndex, int, int)
    on_row_changed = Signal(QModelIndex, QModelIndex)

    def __init__(self: QAbstractItemView | Self, *,
                 model: QAbstractItemModel = None,
                 auto_scroll=False,
                 auto_scroll_margin=16,
                 edit_triggers=AbsItemView.EditTrigger.No,
                 selection_behavior=AbsItemView.SelectionBehavior.Rows,
                 selection_mode=AbsItemView.SelectionMode.Single,
                 hor_scroll_mode=AbsItemView.ScrollMode.PerPixel,
                 ver_scroll_mode=AbsItemView.ScrollMode.PerPixel,
                 hor_single_step: int = None,  # 滚动速度，通常对应于用户按下 [箭头键]
                 ver_single_step: int = None,
                 delegate: ItemDelegate = None,
                 on_cell_clicked: Callable[[QModelIndex], None] = None,
                 on_double_clicked: Callable[[QModelIndex], None] = None,
                 on_rows_inserted: Callable[[QModelIndex, int, int], None] = None,
                 on_row_changed: Callable[[QModelIndex, QModelIndex], None] = None,
                 **kwargs
                 ):
        super().__init__(**kwargs)

        if on_double_clicked: self.doubleClicked.connect(on_double_clicked)
        if on_rows_inserted: self.on_rows_inserted.connect(on_rows_inserted)
        if on_row_changed: self.on_row_changed.connect(on_row_changed)
        if on_cell_clicked:
            if isinstance(self, QTableWidget):
                self.cellClicked.connect(on_cell_clicked)
            else:
                self.clicked.connect(on_cell_clicked)

        self.setAutoScroll(auto_scroll)
        self.setAutoScrollMargin(auto_scroll_margin if auto_scroll else 0)
        self.setEditTriggers(edit_triggers)
        self.setHorizontalScrollMode(hor_scroll_mode)
        self.setVerticalScrollMode(ver_scroll_mode)
        self.setSelectionBehavior(selection_behavior)
        self.setSelectionMode(selection_mode)

        if hor_single_step is not None:
            self.horizontalScrollBar().setSingleStep(hor_single_step)
        if ver_single_step is not None:
            self.verticalScrollBar().setSingleStep(ver_single_step)

        if not isinstance(self, QTableWidget):
            self.setModel(model or StdModel())
        elif model is not None:
            self.setModel(model)

        if delegate:
            if not delegate.parent():
                delegate.setParent(self)
            self.setItemDelegate(delegate)

    def currentChanged(self, current: QModelIndex, previous: QModelIndex) -> None:
        self.super().currentChanged(current, previous)
        if current.parent() != previous.parent() or current.row() != previous.row():
            self.currentRowChanged(current, previous)

    def currentRowChanged(self, current: QModelIndex, previous: QModelIndex) -> None:
        self.on_row_changed.emit(current, previous)

    def rowsInserted(self, parent: QModelIndex, start: int, end: int):
        super().rowsInserted(parent, start, end)
        self.on_rows_inserted.emit(parent, start, end)

    def setCurrentIndex(self, index: QModelIndex, clicked=False) -> None:
        self.super().setCurrentIndex(index)
        if clicked: self.clicked.emit(index)

    def openPersistentEditor(self, index: QModelIndex, col=-1) -> None:
        """ openPersistentEditor(index=currentIndex(), col: int = None) """
        index = index or self.currentIndex()
        index = index if col == -1 else index.siblingAtColumn(col)
        if not self.isPersistentEditorOpen(index):
            self.super().openPersistentEditor(index)

    def setEditTriggers(self, triggers: AbsItemView.EditTrigger) -> None:
        self.super().setEditTriggers(QAbstractItemView.EditTrigger(triggers.value))

    def setHorizontalScrollMode(self, mode: AbsItemView.ScrollMode) -> None:
        self.super().setHorizontalScrollMode(QAbstractItemView.ScrollMode(mode.value))

    def setVerticalScrollMode(self, mode: AbsItemView.ScrollMode) -> None:
        self.super().setVerticalScrollMode(QAbstractItemView.ScrollMode(mode.value))

    def setSelectionBehavior(self, behavior: AbsItemView.SelectionBehavior) -> None:
        self.super().setSelectionBehavior(QAbstractItemView.SelectionBehavior(behavior.value))

    def setSelectionMode(self, mode: AbsItemView.SelectionMode) -> None:
        self.super().setSelectionMode(QAbstractItemView.SelectionMode(mode.value))

    def scrollTo(self, index: QModelIndex | PersistentIndex, hint=AbsItemView.ScrollHint.Visible):
        index = index if isinstance(index, QModelIndex) else index.index()
        hint = hint if isinstance(hint, int) else hint.value
        super().scrollTo(index, QAbstractItemView.ScrollHint(hint))

    # ---- Delegate Func ----
    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
        """ 创建编辑器 """
        if d := self.itemDelegate():
            return d.super().createEditor(parent, option, index)
        return None

    def updateEditorGeometry(self, editor: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        """ 更新编辑器 """
        if d := self.itemDelegate():
            d.super().updateEditorGeometry(editor, option, index)
        return None

    def setEditorData(self, editor: QWidget, index: QModelIndex) -> None:
        """ 设置编辑器数据 """
        if d := self.itemDelegate():
            d.super().setEditorData(editor, index)
        return None

    def setModelData(self, editor: QWidget, model: AbsItemModel, index: QModelIndex) -> None:
        """ 设置模型数据 """

    def itemSizeHint(self, option: QStyleOptionViewItem, index: QModelIndex) -> QSize:
        """ 项目大小提示 """
        if d := self.itemDelegate():
            return d.super().sizeHint(option, index)
        return None

    def displayText(self, value: object, locale: QLocale) -> str:
        """ 项目文本 """
        if d := self.itemDelegate():
            return d.super().displayText(value, locale)
        return None

    def itemDelegate(self) -> Optional[ItemDelegate]:
        # noinspection PyUnresolvedReferences
        return super().itemDelegate()
