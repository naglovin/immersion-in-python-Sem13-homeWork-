
from myException import FormatError


class Matrix:
    """Создаем класс матрица"""
    def __init__(self, matr):
        """«__init__» — зарезервированный метод в классах Python. Он известен как конструктор в концепциях ООП.
        Этот метод вызывается, когда объект создается из класса, и он позволяет классу инициализировать атрибуты класса."""
        self._matr = matr

    def get_matrix(self):
        """Функция для работы с защищенными переменными"""
        return self._matr

    def __add__(self, other):
        """Добавление матрицы, если длины совпадают"""
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise FormatError('a')
        else:
            return Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])

    def __mul__(self, other):
        """Перемножение матриц"""
        if len(self._matr[0]) != len(other._matr):
            raise FormatError('b')
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            return Matrix(new_matr)

    def __eq__(self, other):
        """СРавниваем матрицы и возвращаем TRUE или FALSE"""
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise FormatError()
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            return True

    def __str__(self):
        """__str__() – магический метод для отображения информации об объекте класса для пользователей
        (например, для функций print, str);"""
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i]) + '\n'
        return s


m_1 = [[11, 22, 34, 10],
          [5, 6,  8, 8],
          [21, 53, -12, 6],
          [10, 25, 10, 5]]

m_2 = [[1, 24, 44],
          [5, 62,  8],
          [51, 65,  85],
          [-2, 2, 0]]

m_3 = [[1, 21, 4, 5],
          [5, 65, 8, 10],
          [15, 40, -71, 1]]

m_4 = [[1, 12, 14, 5, 0],
          [5, 6, 8, 0, 10],
          [5, 0, -7, 1, 50]]

matrix_1 = Matrix(m_1)
matrix_2 = Matrix(m_2)
matrix_3 = Matrix(m_3)
matrix_4 = Matrix(m_4)

print ("Cложение матриц:")
matr_sum = matrix_1 + matrix_2
print(matr_sum)

print ("Умножение матриц:")
matr_mul = matrix_1 * matrix_3
print(matr_mul)
print(matrix_1 * matrix_4)

print ("Cравнение матриц:")
print(matrix_1 == matrix_1)
print(matrix_1 == matrix_2)
help(Matrix)