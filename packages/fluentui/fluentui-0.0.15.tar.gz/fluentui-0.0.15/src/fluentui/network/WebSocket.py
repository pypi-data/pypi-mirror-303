from PySide6.QtCore import QByteArray
from PySide6.QtWebSockets import QWebSocket

from .AbsSocket import AbsSocket


class WebSocket(QWebSocket):
    def __init__(self):
        super().__init__()
        self.stateChanged.connect(lambda state: self.onStateChanged(AbsSocket.State(state)))
        self.textMessageReceived.connect(self.onTextMessageReceived)
        self.binaryMessageReceived.connect(self.onBinaryMessageReceived)

    def onStateChanged(self, state: AbsSocket.State) -> None:
        ...

    def onTextMessageReceived(self, text: str) -> None:
        ...

    def onBinaryMessageReceived(self, data: QByteArray) -> None:
        ...

    def isConnect(self) -> bool:
        return self.state() == AbsSocket.State.Connected

    def state(self) -> AbsSocket.State:
        return AbsSocket.State(super().state())
