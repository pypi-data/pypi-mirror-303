from PySide6.QtWidgets import QFrame

from .Widget import WidgetMix


class FrameMix(WidgetMix):
    def __init__(self: QFrame, frame_shape: QFrame.Shape = None, **kwargs):
        super().__init__(**kwargs)
        if frame_shape is not None:
            self.setFrameShape(frame_shape)


class Frame(FrameMix, QFrame):
    ...
