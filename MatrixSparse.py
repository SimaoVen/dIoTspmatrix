from __future__ import annotations
from Matrix import *

position = tuple[int, int]
compressed = tuple[position, float, tuple[float], tuple[int], tuple[int]]


class MatrixSparse(Matrix):
    _zero = float

    #Description: Initializes the object (MatrixSparse) attributes (zero)
    #Parameters: zero -> All types
<<<<<<< HEAD
    #Return: 
=======
    #Return:
>>>>>>> dd7f8bd12b48776d1df8a1a9e5b36e792c48846d
    def __init__(self, zero):
        if(type(zero) is float or type(zero) is int):
            self._zero = zero
        else:
            raise ValueError("__init__() invalid arguments")

    #Description: Returns the zero of the matrix
    #Parameters:
    #Return: self._zero -> float
    @property
    def zero(self) -> float:
        return self._zero

    #Description: Sets the zero of the matrix with the value of the parameter (val)
    #Parameters: val -> float
<<<<<<< HEAD
    #Return: 
=======
    #Return:
>>>>>>> dd7f8bd12b48776d1df8a1a9e5b36e792c48846d
    @zero.setter
    def zero(self, val: float):
        self._zero = val

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError

    #Description: Returns the sparsity by calculating it.
<<<<<<< HEAD
    #Parameters: 
=======
    #Parameters:
>>>>>>> dd7f8bd12b48776d1df8a1a9e5b36e792c48846d
    #Return: float
    def sparsity(self) -> float:
        dim = self.dim()
        if dim:
            min = dim[0]
            max = dim[1]
            w = max[0] - min[0] + 1
            h = max[1] - min[1] + 1
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