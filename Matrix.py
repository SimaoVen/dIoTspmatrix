from __future__ import annotations
from abc import ABC, abstractmethod
from Position import *


class Matrix(ABC):

    @abstractmethod
    def __getitem__(self, item):
        raise NotImplementedError

    @abstractmethod
    def __setitem__(self, key, value):
        raise NotImplementedError

    @abstractmethod
    def __iter__(self):
        raise NotImplementedError

    @abstractmethod
    def __next__(self):
        raise NotImplementedError

    @abstractmethod
    def __copy__(self):
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError

    #Description: Depending if the parameter "other" is a int/float or a Matrix,
    #             it chooses to call the function _add_number() or _add_matrix().
    #Parameters: other -> int/float/Matrix
    #Return: Matrix
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self._add_number(other)
        if isinstance(other, Matrix):
            return self._add_matrix(other)
        raise ValueError('_add__ invalid argument')

    @abstractmethod
    def _add_number(self, other: list[int, float]) -> Matrix:
        raise NotImplementedError

    @abstractmethod
    def _add_matrix(self, val: Matrix) -> Matrix:
        raise NotImplementedError

    #Description: Depending if the parameter "other" is a int/float or a Matrix,
    #             it chooses to call the function _mul_number() or _mul_matrix().
    #Parameters: other -> int/float/Matrix
    #Return: Matrix
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self._mul_number(other)
        if isinstance(other, Matrix):
            return self._mul_matrix(other)
        raise ValueError('__mul__ invalid argument')

    @abstractmethod
    def _mul_number(self, other: list[int, float]) -> Matrix:
        raise NotImplementedError

    @abstractmethod
    def _mul_matrix(self, other: Matrix) -> Matrix:
        raise NotImplementedError

    #Description: Puts the matrix into a string format.
    #Parameters:
    #Return: string -> string
    def __str__(self):
        dim = self.dim()
        string = ""
        if dim != ():
            for row in range(dim[0][0], dim[1][0] + 1):
                for col in range(dim[0][1], dim[1][1] + 1):
                    string += str(self[Position(row, col)])
                    if col < dim[1][1]:
                        string += " "
                if row < dim[1][0]:
                    string += "\n"
        return string

    @abstractmethod
    def dim(self) -> tuple[Position, ...]:
        raise NotImplementedError

    @abstractmethod
    def row(self, row: int) -> Matrix:
        raise NotImplementedError

    @abstractmethod
    def col(self, col: int) -> Matrix:
        raise NotImplementedError

    @abstractmethod
    def diagonal(self) -> Matrix:
        raise NotImplementedError

    @abstractmethod
    def transpose(self) -> Matrix:
        raise NotImplementedError