from PySide6.QtWidgets import QWidget, QLineEdit

from fluentui.widgets import LineEdit, Frame, ScrollArea
from src.fluentui.widgets import Application, Widget


if __name__ == '__main__':
    print('---------------------')
    app = Application()

    w = Widget()
    edit = LineEdit(parent=w, width=200)

    # f = ScrollArea(hor_scroll_bar_policy=)

    w.show()
    app.exec()
