import enum

from PySide6.QtWidgets import QMessageBox, QWidget


class MessageBox(QMessageBox):
    class Button(enum.IntFlag):
        NoButton = QMessageBox.StandardButton.NoButton
        Ok = QMessageBox.StandardButton.Ok
        Save = QMessageBox.StandardButton.Save
        SaveAll = QMessageBox.StandardButton.SaveAll
        Open = QMessageBox.StandardButton.Open
        Yes = QMessageBox.StandardButton.Yes
        YesToAll = QMessageBox.StandardButton.YesToAll
        No = QMessageBox.StandardButton.No
        NoToAll = QMessageBox.StandardButton.NoToAll
        Abort = QMessageBox.StandardButton.Abort
        Retry = QMessageBox.StandardButton.Retry
        Ignore = QMessageBox.StandardButton.Ignore
        Close = QMessageBox.StandardButton.Close
        Cancel = QMessageBox.StandardButton.Cancel
        Discard = QMessageBox.StandardButton.Discard
        Help = QMessageBox.StandardButton.Help
        Apply = QMessageBox.StandardButton.Apply
        Reset = QMessageBox.StandardButton.Reset
        RestoreDefaults = QMessageBox.StandardButton.RestoreDefaults
        FirstButton = QMessageBox.StandardButton.FirstButton
        LastButton = QMessageBox.StandardButton.LastButton
        YesAll = QMessageBox.StandardButton.YesAll
        NoAll = QMessageBox.StandardButton.NoAll
        Default = QMessageBox.StandardButton.Default
        Escape = QMessageBox.StandardButton.Escape
        FlagMask = QMessageBox.StandardButton.FlagMask
        ButtonMask = QMessageBox.StandardButton.ButtonMask

    @classmethod
    def about(cls, parent: QWidget, title='', text='') -> None:
        super().about(parent, title, text)

    @classmethod
    def aboutQt(cls, parent: QWidget = None, *, title='') -> None:
        super().aboutQt(parent, title)

    @classmethod
    def critical(cls, title='', text='', *,
                 buttons=Button.Ok,
                 default=Button.NoButton,
                 parent: QWidget = None) -> Button:
        buttons = QMessageBox.StandardButton(buttons)
        default = QMessageBox.StandardButton(default)
        return super().critical(parent, title, text, buttons, default)

    @classmethod
    def information(cls, title='', text='', *,
                    buttons=Button.Ok,
                    default=Button.NoButton,
                    parent: QWidget = None) -> Button:
        buttons = QMessageBox.StandardButton(buttons)
        default = QMessageBox.StandardButton(default)
        return super().information(parent, title, text, buttons, default)

    @classmethod
    def question(cls, title: str, text: str, *,
                 buttons=Button.Yes | Button.No,
                 default=Button.NoButton,
                 parent: QWidget = None) -> Button:
        buttons = QMessageBox.StandardButton(buttons)
        default = QMessageBox.StandardButton(default)
        return super().question(parent, title, text, buttons, default)

    @classmethod
    def warning(cls, title='', text='', *,
                buttons=Button.Ok,
                default=Button.NoButton,
                parent: QWidget = None) -> Button:
        buttons = QMessageBox.StandardButton(buttons)
        default = QMessageBox.StandardButton(default)
        return super().warning(parent, title, text, buttons, default)
