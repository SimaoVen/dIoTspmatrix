from __future__ import annotations
from Matrix import *

position = tuple[int, int]
compressed = tuple[position, float, tuple[float], tuple[int], tuple[int]]


class MatrixSparse(Matrix):
    _zero = float

    def __init__(self, zero):
        if(type(zero) is float or type(zero) is int):
            self._zero = float(zero)
        else:
            raise ValueError("__init__() invalid arguments")

    @property
    def zero(self) -> float:
        return self._zero

    @zero.setter
    def zero(self, val: float):
        if(type(val) is float or type(val) is int):
            self._zero = float(val)
        else:
            raise ValueError("zero() invalid arguments")

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError

    def sparsity(self) -> float:
        pass

    @staticmethod
    @abstractmethod
    def eye(size: int, unitary: float = 1.0, zero: float = 0.0) -> MatrixSparse:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def compress(self) -> compressed:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def doi(compressed_vector: compressed, pos: Position) -> float:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def decompress(compressed_vector: compressed) -> Matrix:
        raise NotImplementedError
