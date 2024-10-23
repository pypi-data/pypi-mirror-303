from .DateTimeEdit import DateTimeEdit


class DateEdit(DateTimeEdit):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('display_format', 'yyyy-MM-dd')
        super().__init__(*args, **kwargs)
