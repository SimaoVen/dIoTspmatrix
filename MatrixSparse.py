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
        self._zero = val

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError

    def sparsity(self) -> float:
        dim = self.dim()
        if dim:
            w = self.dim[1].__getitem__(1) - self.dim[0].__getitem__(1) + 1
            h = self.dim[1].__getitem__(0) - self.dim[0].__getitem__(0) + 1
            return float((w * h - self.__len__()) / (w * h))
        return 1.0


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
