from .AbsItemView import AbsItemView
from .Widget import Widget
from ..core import PersistentIndex
from ..gui import ColumnModel
from ..namespce import ItemDataRole


class ItemEditor(Widget):
    def __init__(self, index: PersistentIndex = None, **kwargs):
        super().__init__(**kwargs)
        self.index = index

    def data(self) -> object:
        return self.index.data(ItemDataRole.Edit)

    def model(self) -> ColumnModel:
        return self.index.model()

    def row(self) -> int:
        return self.index.row()

    def column(self) -> int:
        return self.index.column()

    def view(self) -> AbsItemView:
        return super().parent().parent()
