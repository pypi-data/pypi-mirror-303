from PySide6.QtCore import QModelIndex, QSize, QLocale
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem, QWidget
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .AbsItemView import AbsItemView
from ..core import AbsItemModel


class ItemDelegate(QStyledItemDelegate):
    def __init__(self, parent: 'AbsItemView' = None):
        self._parent = parent
        super().__init__(parent=parent)

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
        """ 创建编辑器 """
        return self._parent.createEditor(parent, option, index)

    def updateEditorGeometry(self, editor: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        """ 更新编辑器 """
        self._parent.updateEditorGeometry(editor, option, index)

    def setEditorData(self, editor: QWidget, index: QModelIndex) -> None:
        """ 设置编辑器数据 """
        # self._parent.setEditorData(editor, index)

    def setModelData(self, editor: QWidget, model: AbsItemModel, index: QModelIndex) -> None:
        """ 设置模型数据 """
        # self._parent.setModelData(editor, model, index)

    def sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex) -> QSize:
        """ 项目大小提示 """
        return self._parent.itemSizeHint(option, index)

    def displayText(self, value: object, locale: QLocale) -> str:
        """ 项目文本 """
        return self._parent.displayText(value, locale)

    def setParent(self, parent: 'AbsItemView') -> None:
        self._parent = parent
        super().setParent(parent)

    def parent(self) -> 'AbsItemView':
        return super().parent()

    def super(self) -> 'ItemDelegate':
        return super()
