from PySide6.QtGui import QFontDatabase


class FontDatabase(QFontDatabase):
    @classmethod
    def applicationFontFamilies(cls, fileNames: list[str]) -> list[str]:
        return [super().applicationFontFamilies(y) for
                y in [cls.addApplicationFont(x) for x in fileNames]]
