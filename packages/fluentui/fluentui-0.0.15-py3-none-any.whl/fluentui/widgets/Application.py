import sys
from typing import Callable, Never

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

from fluentui.gui import FontDatabase


class Application(QApplication):
    def __init__(self, font: QFont = None,
                 font_families: list[str] = None,
                 quit_on_last_window_closed=True,
                 about_to_quit: Callable[[], None] = None,
                 ):

        # 支持高分辨率
        self.setAttribute(Qt.ApplicationAttribute.AA_ShareOpenGLContexts)
        self.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
        self.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
        self.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        super().__init__(sys.argv)

        if font_families:
            print(FontDatabase.applicationFontFamilies(font_families))
        if about_to_quit: self.aboutToQuit.connect(about_to_quit)
        if font: self.setFont(font)

        self.setQuitOnLastWindowClosed(quit_on_last_window_closed)

    def exec(self) -> Never:
        return sys.exit(super().exec())
