class MyError(Exception):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a <= 0 and self.b <= 0:
            return f"Ошибка ввода: обе стороны имеют не правильное значения = {self.a}; {self.b}"
        else:
            if self.a <= 0:
                return f"Ошибка ввода: сторона имеет не правильное  значение = {self.a} "
            else:
                return f"Ошибка ввода: сторона имеет не правильное значение  = {self.b}"


class FormatError(Exception):
    def __init__(self, operation: str):
        self.operation = operation

    def __str__(self):
        if self.operation == 'a':
            return f"Error: Нельзя сложить матрицы, матрицы разных размеров"
        elif self.operation == 'b':
            return f"Error: ни как нельзя умножить матрицы: разные размеры"
        else:
            return f"Error: Не сравнить. Матрицы разных размеров"