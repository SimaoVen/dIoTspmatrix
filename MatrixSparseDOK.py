from __future__ import annotations
from MatrixSparse import *
from Position import *

#spmatrix = dict[Position, float]

class MatrixSparseDOK(MatrixSparse):
    #_items = spmatrix

    def __init__(self, zero: float = 0.0):
        self._items = ({}, zero)

    def __copy__(self):
        return self._items

    def __eq__(self, other: MatrixSparseDOK):
        return self._items == other

    def __iter__(self):
        self.matrix_iter = []
        for pos1, value in self._items[0].keys():
            for pos2 in self._items[0].keys():
                if pos2 < pos1:
                    break
                if pos2 == pos1:


    def __next__(self):
        return next(self.__iter__)

    def __getitem__(self, pos: [Position, position]) -> float:
        if pos in self._items[0].keys():
            return self._items[1]
        else:
            return self.zero()

    def __setitem__(self, pos: [Position, position], val: [int, float]):
        if pos in self._items[0].keys():
            zero = self.zero()
            if float(val) == zero:
                del self._items[0]
            else:
                self._items[1].update(float(val))
        else:
            self._items[0] = float(val)


    def __len__(self) -> int:
        return len(self._items)

    def _add_number(self, other: [int, float]) -> Matrix:
        while self._items[0].keys():
            self._items[1] += other
        return self._items

    def _add_matrix(self, other: MatrixSparse) -> MatrixSparse:
        while other[0].keys():
            if other[0].keys()

    def _mul_number(self, other: [int, float]) -> Matrix:
        pass

    def _mul_matrix(self, other: MatrixSparse) -> MatrixSparse:
        pass

    def dim(self) -> tuple[Position, ...]:
        pass

    def row(self, row: int) -> Matrix:
        pass

    def col(self, col: int) -> Matrix:
        pass

    def diagonal(self) -> Matrix:
        pass

    @staticmethod
    def eye(size: int, unitary: float = 1.0, zero: float = 0.0) -> MatrixSparseDOK:
        pass

    def transpose(self) -> MatrixSparseDOK:
        pass

    def compress(self) -> compressed:
        pass

    @staticmethod
    def doi(compressed_vector: compressed, pos: Position) -> float:
        pass

    @staticmethod
    def decompress(compressed_vector: compressed) -> MatrixSparse:
        pass
