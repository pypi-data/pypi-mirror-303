from typing import Union

from PySide6.QtWidgets import QTableView, QTableWidget

from .AbsItemView import AbsItemViewMix


class TableViewMix(AbsItemViewMix):
    Self = Union[QTableView, 'TableViewMix']

    def __init__(self: QTableView, *args,
                 default_row_height=0,  # 默认行高
                 default_col_width: int = None,  # 默认列宽
                 min_row: int = None,  # 最小行高
                 max_row: int = None,  # 最大行高
                 min_col: int = None,  # 最小列宽
                 max_col: int = None,  # 最大列宽
                 word_wrap=True,
                 show_grid=True,
                 auto_scroll=False,
                 hor_header_visible=True,
                 ver_header_visible=True,
                 **kwargs
                 ):
        super().__init__(*args, **kwargs)
        hor_header = self.horizontalHeader()
        ver_header = self.verticalHeader()

        if default_col_width:
            hor_header.setDefaultSectionSize(default_col_width)  # 默认列宽
        if min_col: hor_header.setMinimumSectionSize(min_col)  # 最小列宽
        if max_col: hor_header.setMaximumSectionSize(max_col)  # 最大列宽
        hor_header.setVisible(hor_header_visible)

        ver_header.setDefaultSectionSize(default_row_height)  # 默认行高
        if min_row: ver_header.setMinimumSectionSize(min_row)  # 最小行高
        if max_row: ver_header.setMaximumSectionSize(max_row)  # 最大行高
        ver_header.setVisible(ver_header_visible)

        self.setShowGrid(show_grid)
        self.setWordWrap(word_wrap)
        self.setAutoScroll(auto_scroll)


class TableView(TableViewMix, QTableView):
    ...


class TableWidget(TableViewMix, QTableWidget):
    def __init__(self, rows=0, columns=0, **kwargs):
        super().__init__(**kwargs)
        self.setRowCount(rows)
        self.setColumnCount(columns)
