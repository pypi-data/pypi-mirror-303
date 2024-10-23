from PySide6.QtGui import QFont


class Font(QFont):
    def __init__(self,
                 families='Segoe UI, Microsoft YaHei, PingFang SC', *,
                 size=14,
                 weight=QFont.Weight.Normal,
                 italic=False,
                 ):
        super().__init__([x.strip() for x in families.split(',')], -1, weight, italic)
        self.setPixelSize(size)
