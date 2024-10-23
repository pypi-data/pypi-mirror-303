from typing import Callable

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTextEdit, QTextBrowser

from .ScrollArea import AbsScrollAreaMix


class TextEditMix(AbsScrollAreaMix):
    def __init__(self: QTextEdit,
                 text='', *,
                 read_only=False,
                 undo_redo_enabled=True,
                 document_margin=4,
                 accept_rich_text=True,
                 on_text_change: Callable[[], None] = None,
                 self_align: Qt.AlignmentFlag = None,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        if on_text_change: self.textChanged.connect(on_text_change)

        self.setText(text)
        self.setReadOnly(read_only)
        self.setAcceptRichText(accept_rich_text)
        self.setUndoRedoEnabled(undo_redo_enabled)
        self.document().setDocumentMargin(document_margin)
        if self_align is not None: self.setAlignment(self_align)

    def adjustFixedHeight(self: QTextEdit, width=0) -> None:
        if (d := self.document()) and width > 0:
            d.setTextWidth(width)
            d.setTextWidth(idea_width := int(d.idealWidth()))
            self.setFixedSize(idea_width, d.size().toSize().height())
        else:
            d.setTextWidth(d.idealWidth())
            self.setFixedHeight(d.size().toSize().height())


class TextEdit(TextEditMix, QTextEdit):
    ...


class TextBrowser(TextEditMix, QTextBrowser):
    def __init__(self, text='', *,
                 open_links=True,
                 open_external_links=False,
                 on_anchor_clicked: Callable[[str], None] = None,
                 **kwargs
                 ):
        super().__init__(text, **kwargs)
        if on_anchor_clicked: self.anchorClicked.connect(on_anchor_clicked)

        self.setOpenLinks(open_links)
        self.setOpenExternalLinks(open_external_links)
