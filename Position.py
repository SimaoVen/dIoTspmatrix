from __future__ import annotations


class Position:
    _pos = (int, int)

    def init(self, row: int, col: int):
        if(type(row) is int  and row >= 0  and type(col) is int  and col >= 0):
            self._pos = (row,col)
        elif(type[row] is float and row >= 0 and type(col) is float and col >= 0):
            if(row - int(row) != 0 and col - int(col) != 0 and col >= 0 and row >= 0):
                self._pos = (int(row),int(col))
            else:
                raise ValueError('init() invalid arguments')
        else:
            raise ValueError('init() invalid arguments')

    def str(self):
        return '(' + str(self._pos[0]) + ', ' + str(self._pos[1]) + ')'

    def getitem(self, item: int) -> int:
        if(item >= 0 and item <= 1):
            return self._pos[item]
        else:
            raise ValueError('getitem() invalid arguments')

    def eq(self, other: Position):
        return self._pos == other