class ColumnItem:
    def __init__(self, value: object):
        self.value = value

    def __repr__(self) -> str:
        return f'{self.value}'
