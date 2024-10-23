from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect


class GraphicsDropShadowEffect(QGraphicsDropShadowEffect):
    def __init__(self, blurRadius: float = 1, offset=(0.8, 0.8), color='#b43f3f3f', parent=None):
        super().__init__(parent)
        self.setBlurRadius(blurRadius)
        self.setOffset(*offset)
        if color: self.setColor(QColor(color))
