from PySide6.QtWidgets import QFrame

from .Widget import WidgetMix

if (__frame := object) is None:
    __frame = QFrame


class FrameMix(WidgetMix, __frame):
    def __init__(self, frame_shape: QFrame.Shape = None, **kwargs):
        super().__init__(**kwargs)
        if frame_shape is not None:
            self.setFrameShape(frame_shape)


class Frame(FrameMix, QFrame):
    ...
