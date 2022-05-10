from __future__ import annotations


class Position:
    _pos = tuple[int, int]

    def __init__(self, row: int, col: int):
        if not (type(row) is int and row >= 0) or not (type(col) is int and col >= 0):
            raise ValueError('__init__() invalid arguments')
        self._pos = (row, col)

    def __str__(self):
        return "(" + str(self._pos[0]) + ", " + str(self._pos[1]) + ")"

    def __getitem__(self, item: int) -> int:
        if isinstance(item, int) and (item in (0, 1)):
            return self._pos[item]
        else:
            raise ValueError('__getitem__() invalid arguments')

    def __eq__(self, other: Position):
        return self._pos == other._pos
