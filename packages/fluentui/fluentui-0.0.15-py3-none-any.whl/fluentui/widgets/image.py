import json
from hashlib import md5
from pathlib import Path
from typing import Optional, Callable

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QPixmap, qGray, qRgb
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager
from PySide6.QtWidgets import QLabel, QSizePolicy

from .Widget import WidgetMix


class Request(QNetworkRequest):
    manager = QNetworkAccessManager()

    def send(self, finished: Callable[[bytes], None]) -> QNetworkReply:
        print('\n' + json.dumps({
            'url': self.url().toString(QUrl.None_ | QUrl.RemoveQuery),
        }, indent=4))

        reply = self.manager.get(self)
        reply.finished.connect(lambda: finished(self.on_finished(reply)))
        return reply

    @staticmethod
    def on_finished(reply: QNetworkReply) -> bytes:
        if reply.error() == 5:
            return bytes()
        return reply.readAll().data()


class Image(WidgetMix, QLabel):
    def __init__(self, *args, placeholder='', **kwargs):
        QLabel.__init__(self)
        super().__init__(*args, **kwargs)

        self.__is_load = False  # 图片是否已加载
        self.__gray = False
        self.reply: Optional[QNetworkReply] = None

        self.__pixmap = QPixmap(placeholder)
        self.setPixmap(self.__pixmap)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def load(self, name: str):
        if self.__is_load or not name:
            return

        self.__is_load = True
        if not name.startswith('http'):  # 加载缓存图片
            if (path := Path(name)).is_file():
                self.__finished(path.read_bytes())
            return

        filename = md5(name.encode()).hexdigest()
        if (path := Path(f'assets/caches/{filename}')).is_file():
            self.__finished(path.read_bytes())
            return

        req = Request(url=QUrl(name))
        self.reply = req.send(lambda data: self.__finished(data, path))

    def to_gray(self, on=True):
        image = self.pixmap().toImage()
        if not image or on == self.__gray:
            return

        self.__gray = on
        if not on:
            self.setPixmap(self.__pixmap)
            return

        for x in range(image.width()):
            for y in range(image.height()):
                if (v := image.pixel(x, y)) == 0:
                    continue
                z = qGray(v)
                rgb = qRgb(z, z, z)
                image.setPixel(x, y, rgb)

        self.pixmap().convertFromImage(image)
        self.setPixmap(self.pixmap())

    def __finished(self, data: bytes, path: Optional[Path] = None):
        """ 图片请求完成时调用 """
        if data and not self.pixmap().loadFromData(data):
            return

        self.__pixmap = self.pixmap().scaled(
            self.size(),
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        )

        self.setPixmap(self.__pixmap)
        path and (path.touch() or path.write_bytes(data))
