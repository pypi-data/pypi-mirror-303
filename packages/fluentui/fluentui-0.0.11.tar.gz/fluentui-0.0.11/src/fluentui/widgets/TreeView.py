from PySide6.QtWidgets import QTreeView

from .AbsItemView import AbsItemViewMix


class TreeView(AbsItemViewMix, QTreeView):
    def __init__(self,
                 indentation=20,
                 header_hidden=False,
                 expands_on_double_click=False,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.setIndentation(indentation)
        self.setHeaderHidden(header_hidden)
        self.setExpandsOnDoubleClick(expands_on_double_click)
