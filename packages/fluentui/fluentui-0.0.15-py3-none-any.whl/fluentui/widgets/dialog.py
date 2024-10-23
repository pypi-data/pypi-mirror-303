from typing import Callable

from PySide6.QtWidgets import QDialog

from .Widget import WidgetMix


class Dialog(WidgetMix, QDialog):
    def __init__(self, *,
                 accepted: Callable[[], None] = None,
                 rejected: Callable[[], None] = None,
                 finished: Callable[[int], None] = None,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        if accepted: self.accepted.connect(accepted)
        if rejected: self.rejected.connect(rejected)
        if finished: self.finished.connect(finished)
