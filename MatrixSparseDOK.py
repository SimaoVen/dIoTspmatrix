from __future__ import annotations
from asyncio.windows_events import NULL
from sys import getsizeof
from MatrixSparse import *
from Position import *

spmatrix = dict[Position, float]

class MatrixSparseDOK(MatrixSparse):
    _items = spmatrix

    def __init__(self, zero: float = 0):
        self.index = -1
        self._items = {}
        super(MatrixSparseDOK, self).__init__(zero)

    def __copy__(self):
        return MatrixSparseDOK(self._zero)

    def __eq__(self, other: MatrixSparseDOK):
        return self._items == other

    def __iter__(self):
        self.it = sorted(self._items.keys(), key=lambda k:[k[0], k[1]]) 
        return self
        
    def __next__(self):
        self.index += 1
        if self.index == len(self.it):
            self.index = -1
            raise StopIteration
        return self.it[self.index]

    @MatrixSparse.zero.setter
    def zero(self, val: float):
        MatrixSparse.zero.fset(self, val)
        newMS = self._items.copy()
        for pos in self._items.keys():
            if(self._items[pos] == val):
                newMS.pop(pos)
        self._items = newMS.copy()

    def __getitem__(self, pos: [Position, position]) -> float:
        if not(isinstance(pos, Position) or isinstance(pos, tuple) and len(pos) == 2):
            raise ValueError('__getitem__() invalid arguments')
        if not(isinstance(pos[0], int) and isinstance(pos[1], int) and pos[0] >= 0 and pos[1] >= 0):
            raise ValueError('__getitem__() invalid arguments')

        if pos in self._items.keys():
            return self._items[pos]
        else:
            return self.zero

    def __setitem__(self, pos: [Position, position], val: [int, float]):
        if not(isinstance(pos, Position) or isinstance(pos, tuple) and len(pos) == 2):
            raise ValueError('__setitem__() invalid arguments')
        if not(isinstance(val, (int, float))) or not((val >= 0) and isinstance(pos[0], int) and isinstance(pos[1], int) and pos[0] >= 0 and pos[1] >= 0):
            raise ValueError('__setitem__() invalid arguments')

        if float(val) == self.zero:
            if pos in self._items.keys():
                self._items.pop(pos)
        else:
            self._items.update({pos:float(val)})

    def __len__(self) -> int:
        return len(self._items)

    def _add_number(self, other: [int, float]) -> Matrix:
        newM = MatrixSparseDOK(self.zero)
        for cord in self._items.keys():
            value = self._items[cord]
            newM[cord] = value + other
        return newM

    def _add_matrix(self, other: MatrixSparse) -> MatrixSparse:
        newM = MatrixSparseDOK(self.zero)
        if self.zero == other.zero:
            for cord_items in self._items.keys():
                value_items = self._items[cord_items]
                newM[cord_items] = value_items

            for cord_other in other:
                value_other = other[cord_other]
                value = value_other
                if newM[cord_other] == self.zero:
                    newM[cord_other] = value
                else:
                    newM[cord_other] += value

            return newM
        else:
            raise ValueError('_add_matrix() incompatible matrices')

    def _mul_number(self, other: list[int, float]) -> Matrix:
        newM = MatrixSparseDOK(self.zero)

        for cord_items in self._items.keys():
            value_items = self._items[cord_items]
            newM[cord_items] = value_items

        for pos in self._items.keys():
            newM[pos] *= other
        return newM

    def _mul_matrix(self, other: MatrixSparse) -> MatrixSparse:
        newM = MatrixSparseDOK(self.zero)

        dim_items = self.dim()
        dim_other = other.dim()
        h_items = dim_items[1][0] - dim_items[0][0] + 1
        w_items = dim_items[1][1] - dim_items[0][1] + 1
        h_other = dim_other[1][0] - dim_other[0][0] + 1
        w_other = dim_other[1][1] - dim_other[0][1] + 1

        if w_items == h_other and h_items == w_other and self.zero == other.zero:
            col_items = dim_items[0][1]
            row_items = dim_items[0][0]
            col_other = dim_other[0][1]
            row_other = dim_other[0][0]

            for i in range(h_items):
                for j in range(w_other):
                    newM[row_items, col_other] -= newM.zero
                    for k in range(w_items):
                        try:
                            value_items = self._items[row_items, col_items]
                        except Exception as e:
                            value_items = 0
                        try:
                            value_other = other[row_other, col_other]
                        except Exception as e:
                            value_other = 0
                        newM[row_items, col_other] += value_items*value_other
                        row_other += 1
                        col_items += 1
                    col_other += 1
                    col_items = dim_items[0][1]
                    row_other = dim_other[0][0]
                row_items += 1
                col_other = dim_other[0][1]
        else:
            raise ValueError('_mul_matrix() incompatible matrices')
        return newM

    def dim(self) -> tuple[Position, ...]:
        keys = self._items.keys()
        w_max, w_min, h_max, h_min = 0, 0, 0, 0
        if keys:
            itr = sorted(self._items.keys(), key=lambda k:[k[0], k[1]])
            itr_len = len(itr)
            notitr = sorted(self._items.keys(), key=lambda k:[k[1], k[0]])
            notitr_len = len(notitr)
            w_min = notitr[0][1]
            w_max = notitr[notitr_len-1][1]
            h_min = itr[0][0]
            h_max = itr[itr_len-1][0]
            return [(h_min, w_min), (h_max, w_max)]
        return ()

    def row(self, row: int) -> Matrix:
        newM = MatrixSparseDOK(self.zero)
        for cord in self._items.keys():
            if cord[0] == row:
                value = self._items[cord]
                newM[cord] = value

        return newM

    def col(self, col: int) -> Matrix:
        newM = MatrixSparseDOK(self.zero)
        for cord in self._items.keys():
            if cord[1] == col:
                value = self._items[cord]
                newM[cord] = value

        return newM

    def diagonal(self) -> Matrix:
        newM = MatrixSparseDOK(self.zero)
        for keys in self._items.keys():
            if keys[0] == keys[1]:
                value = self._items[keys]
                newM[keys] = value

        return newM

    @staticmethod
    def eye(size: int, unitary: float = 1.0, zero: float = 0.0) -> MatrixSparseDOK:
        if (size >= 0):
            newM = MatrixSparseDOK(zero)

            for i in range(size):
                newM[i, i] = unitary

            return newM
        else:
            raise ValueError('eye() invalid parameters')


    def transpose(self) -> MatrixSparseDOK:
        newM = MatrixSparseDOK(self.zero)
        for cord in self._items.keys():
            value = self._items[cord]
            newM[cord[1], cord[0]] = value

        return newM

    def compress(self) -> compressed:
        if self.sparsity() < 0.5:
            raise ValueError('compress() dense matrix')

        dim_items = self.dim()
        pos_min = dim_items[0]
        h_items = dim_items[1][0] - dim_items[0][0] + 1

        it = sorted(self._items.keys(), key=lambda k:[k[1], k[0]])

        list_values = [0.0] * len(it)
        list_indexes = [-1] * len(it)
        list_offsets = [0] * h_items
        list_row_offsets = []
        for j in range(h_items):
            row_items = it[0][0]
            list_row_offsets.append(row_items)

            list_aux = []
            first_number = -1
            x = 0
            list_items = dim_items[1][1] + 1
            for y in range(list_items):
                try:
                    list_aux.append(self._items[row_items, y])
                    if first_number == -1:
                        first_number = y - dim_items[0][1]
                except Exception as e:
                    if first_number != -1:
                        list_aux.append(0.0)
            
            for x in reversed(range(len(list_aux))):
                if list_aux[x] == 0.0:
                    list_aux.pop(x)
                else:
                    break

            offset = 0
            a = first_number
            c = 0
            list_indexes_aux = list_indexes.copy()
            list_values_aux = list_values.copy()
            restart_for = True
            while restart_for:
                restart_for = False
                for b in range(len(list_aux)):
                    if a >= len(list_values_aux):
                        list_values.append(0.0)
                        list_values_aux = list_values.copy()
                        list_indexes.append(-1)
                        list_indexes_aux = list_indexes.copy()
                        a = first_number
                        c = 0
                        offset = 0
                        restart_for = True
                        break

                    if list_aux[b] != 0.0:
                        if list_values_aux[a] + list_aux[b] == list_aux[b]:
                            list_values_aux.pop(a)
                            list_values_aux.insert(a, list_aux[b])
                            list_indexes_aux.pop(a)
                            list_indexes_aux.insert(a, row_items)
                            if c == 0:
                                first = a
                                c = 1
                            a += 1
                        else:                            
                            if c == 0:
                                a += 1
                                offset += 1
                                restart_for = True
                                break
                            else:
                                list_values_aux = list_values.copy()
                                list_indexes_aux = list_indexes.copy()
                                a = first + 1
                                c = 0
                                offset += 1
                                restart_for = True
                                break
                    else:
                        a += 1

            list_values = list_values_aux.copy()
            list_indexes = list_indexes_aux.copy()

            it_aux = it.copy()
            for x in reversed(range(len(it))):
                if it[x][0] == list_row_offsets[j]:
                    it_aux.pop(x)
            it = it_aux.copy()

            list_offsets[list_row_offsets[j] - pos_min[0]] = offset
            
            if it == []:
                break

        return (pos_min, float(self.zero), tuple(list_values), tuple(list_indexes), tuple(list_offsets))

    @staticmethod
    def doi(compressed_vector: compressed, pos: Position) -> float:
        if not(isinstance(compressed_vector, tuple) and isinstance(compressed_vector[0], tuple) and len(compressed_vector[0]) == 2 and isinstance(compressed_vector[1], float) and isinstance(compressed_vector[2], tuple) and isinstance(compressed_vector[3], tuple) and isinstance(compressed_vector[4], tuple)):
            raise ValueError('doi() invalid parameters')

        pos_min = compressed_vector[0]
        offset = compressed_vector[4][pos[0] - pos_min[0]]
        
        if len(compressed_vector[3]) > pos[1] + offset - pos_min[1] and pos[0] == compressed_vector[3][pos[1] + offset - pos_min[1]]:
            return compressed_vector[2][pos[1] + offset - pos_min[1]]
        else:
            return compressed_vector[1]

    @staticmethod
    def decompress(compressed_vector: compressed) -> MatrixSparse:
        newM = MatrixSparseDOK(compressed_vector[1])
        pos_min = compressed_vector[0]

        for x in range(len(compressed_vector[2])):
            if compressed_vector[3][x] >= 0:
                offset = compressed_vector[4][compressed_vector[3][x] - pos_min[0]]
                newM[(compressed_vector[3][x], x + compressed_vector[0][1] - offset)] = compressed_vector[2][x]
        
        return newM
