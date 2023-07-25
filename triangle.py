from myException import MyError

class Triangle:

    def __init__(self, a: int, b: int, c: int) -> None:
        if a > 0:
            self.a = a
        else:
            raise MyError (a, 0)
        if b > 0:
            self.b = b
        else:
            raise MyError (b, 0)
        if c > 0:
            self.c = c
        else:
            raise MyError (c, 0)

    def check_sides(self):

        check1 = self.a + self.b
        check2 = self.a + self.c
        check3 = self.b + self.c
        if (check1 < self.c or check2 < self.b or check3 < self.a):
            raise MyError(self.a, self.b, self.c)
        else:
            if (a == b and b == c and c == a):
                print("Треугольник равносторонний")
            elif (a == b or b == c or c == a):
                print("Треугольник равнобедренный")
            else:
                print("Треугольник разносторонний")

if __name__ == '__main__':
    a = 2
    b = 3
    c = 4
    check = Triangle(a, b, c)
    print(check.check_sides())

