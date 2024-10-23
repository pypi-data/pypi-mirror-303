import tempfile
from hashlib import md5
from pathlib import Path
from typing import Optional, Union

from PySide6.QtCore import Qt, QEventLoop, QUrl, QByteArray, QSize, QBuffer, QIODevice, QDateTime
from PySide6.QtGui import QPixmap, QResizeEvent
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PySide6.QtWidgets import QLabel

from .Widget import WidgetMix


class Label(WidgetMix, QLabel):
    def __init__(self, text='', align: Qt.AlignmentFlag = None, **kwargs):
        super().__init__(text, **kwargs)
        if align is not None: self.setAlignment(align)


class Text(Label):
    def __init__(self, text='', **kwargs):
        super().__init__(text, fill_width=True, **kwargs)


class ImageLabel(Label):
    __loop = QEventLoop()
    __manager = QNetworkAccessManager()

    def __init__(self, src='', **kwargs):
        super().__init__(
            ignore_width=True,
            ignore_height=True,
            align=Qt.AlignmentFlag.AlignCenter,
            **kwargs
        )

        self.__origin_pixmap = QPixmap()
        self.__reply: Optional[QNetworkReply] = None

        self.cache_path = Path.home() / f'AppData/Local/images_cache'
        self.cache_path.mkdir(parents=True, exist_ok=True)

        self.destroyed.connect(lambda: self.__reply and self.__reply.abort())
        self.load(src)

    def load(self, url: str, sync=False) -> None:
        flag = url.startswith('http')
        path = self.cache_path / md5(url.encode()).hexdigest() if flag else Path(url)
        if path.exists():
            self.__finished(path, None)
            return

        self.__reply = self.__manager.get(QNetworkRequest(QUrl(url)))
        if sync:
            self.__reply.finished.connect(self.__loop.quit)
            self.__loop.exec(
                QEventLoop.ProcessEventsFlag.ExcludeUserInputEvents |
                QEventLoop.ProcessEventsFlag.ExcludeSocketNotifiers
            )
            self.__finished(path, self.__reply.readAll())
            return

        self.__reply.finished.connect(lambda: self.__finished(path, self.__reply.readAll()))
        return

    def __finished(self, path: Path, data: Union[QByteArray, bytes, None]) -> None:
        pixmap = QPixmap(f'{path.resolve()}') if data is None else QPixmap()
        if data and not data.isNull() and not data.isEmpty():
            path.write_bytes(data)
            pixmap.loadFromData(data)
        self.__origin_pixmap = pixmap
        self.setPixmap(pixmap)

    def resizeEvent(self, e: QResizeEvent) -> None:
        super().resizeEvent(e)
        self.setPixmap(self.__origin_pixmap)

    def setPixmap(self, pixmap: QPixmap, size: QSize = None) -> None:
        if pixmap.isNull():
            return
        super().setPixmap(pixmap.scaled(
            size or self.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    def scaled(self, size: QSize) -> None:
        self.setPixmap(self.__origin_pixmap, self.size().boundedTo(size))

    def isNull(self) -> bool:
        return self.__origin_pixmap.isNull()

    def pixel_width(self) -> int:
        return self.__origin_pixmap.width()

    def pixel_height(self) -> int:
        return self.__origin_pixmap.height()

    def pixel_size(self) -> QSize:
        return self.__origin_pixmap.size()

    def data(self, format_='PNG', quality=-1) -> bytes:
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        self.pixmap().save(buffer, format=format_, quality=quality)
        return byte_array

    def save(self, fmt='jpg', quality=-1) -> Path:
        now = QDateTime.currentDateTime()
        name = now.toString(f'yyyyMMddHHmmsszzz-{quality}.{fmt}')

        path = Path(tempfile.gettempdir()) / 'jdback/images'
        path.mkdir(parents=True, exist_ok=True)
        path = path / name

        self.__origin_pixmap.save(path.as_posix(), fmt, quality)
        return path
