from __future__ import annotations

from enum import Enum

from PySide6.QtNetwork import QAbstractSocket


class AbsSocket(QAbstractSocket):
    class State(Enum):
        Unconnected = 0
        HostLookup = 1
        Connecting = 2
        Connected = 3
        Bound = 4
        Listening = 5
        Closing = 6

        def __eq__(self, other: AbsSocket.State | int) -> bool:
            value = other if isinstance(other, int) else other.value
            return self.value == value
