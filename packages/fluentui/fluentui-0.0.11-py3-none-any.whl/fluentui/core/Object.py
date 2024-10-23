from PySide6.QtCore import QObject

if (__object := object) is None:
    __object = QObject


class ObjectMix(__object):
    def __init__(self, *args, parent=None, props: dict = None, **kwargs):
        # noinspection PyArgumentList
        super().__init__(parent=parent, *args, **kwargs)
        for name, value in (props or {}).items():
            self.setProperty(name, value)
