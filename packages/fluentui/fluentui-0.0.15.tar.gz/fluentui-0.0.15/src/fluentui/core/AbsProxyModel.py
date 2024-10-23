from PySide6.QtCore import QAbstractProxyModel, QSortFilterProxyModel, QObject

from .AbsItemModel import AbsItemModelMix, AbsItemModel


class AbsProxyModelMix(AbsItemModelMix):
    ...


class AbsProxyModel(AbsProxyModelMix, QAbstractProxyModel):
    ...


class SortFilterProxyModelMix(AbsProxyModelMix):
    def __init__(self, source: AbsItemModel = None, parent: QObject = None):
        super().__init__(parent)
        if source is not None:
            self.setSourceModel(source)


class SortFilterProxyModel(SortFilterProxyModelMix, QSortFilterProxyModel):
    ...
