from __future__ import annotations


class Position:
    _pos = (int, int)

    def __init__(self, row: int, col: int):
        if((type(row) is int or type(row) is float) and row >= 0  and (type(col) is int or type(col) is float) and col >= 0):
            self._pos = (int(row),int(col))
        else:
            raise ValueError('__init__() invalid arguments')
      

    def __str__(self):
        return '(' + str(self._pos[0]) + ', ' + str(self._pos[1]) + ')'

    def __getitem__(self, item: int) -> int:
        if(item >= 0 and item <= 1):
            return self._pos[item]
        else:
            raise ValueError('__getitem__() invalid arguments')

    def __eq__(self, other: Position):
        return self._pos == other