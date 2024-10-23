from __future__ import annotations

from PySide6.QtCore import QAbstractItemModel
from PySide6.QtWidgets import QComboBox

from .Widget import WidgetMix
from .. import AssetPath


class ComboBox(WidgetMix, QComboBox):
    def __init__(self, *,
                 max_visible=10,
                 items: list[str | dict | tuple] = None,
                 model: QAbstractItemModel = None,
                 editable=False,
                 select: int | str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.setStyleSheet(
            ":item { height: 32px; }\n"
            "::drop-down { border: 0; width: 24px }\n"
            "::down-arrow {\n"
            f"   image: url({AssetPath}/images/light_chevron_down.png);\n"
            "    width: 12; right: 6\n"
            "}"
        )
        self.setEditable(editable)
        self.setMaxVisibleItems(max_visible)

        if model is not None:
            self.setModel(model)
        elif items:
            if isinstance(items[0], str):
                self.addItems(items)
            else:
                self.setItems(items)

        if isinstance(select, int):
            self.setCurrentIndex(select)
        elif isinstance(select, str):
            self.setCurrentText(select)

    def setItems(self, items: list[dict]) -> None:
        self.clear()
        for x in items:
            if not isinstance(x, tuple):  # dict
                x = tuple(x.items())[0]
            self.addItem(x[1], x[0])

    def selectText(self, text: str) -> int:
        if (index := self.findText(text)) >= 0:
            self.setCurrentIndex(index)
        return index

    def selectEditText(self, text: str) -> int:
        if (index := self.findText(text)) >= 0:
            self.setCurrentIndex(index)
        if index == -1:
            self.setEditText(text.strip())
        return index

    def selectData(self, data: object) -> int:
        if (index := self.findData(data)) >= 0:
            self.setCurrentIndex(index)
        return index
