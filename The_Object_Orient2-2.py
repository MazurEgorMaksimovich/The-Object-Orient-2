class TriangleChecker():
    
    def __init__(self, first, second, three):
        self.first = first
        self.second = second
        self.three = three
    
    def is_triangle(self):
        if self.first <= 0 or self.second <= 0 or self.three <= 0:
            print("С отрицательными числами ничего не выйдет!")
        elif self.first + self.second > self.three and self.first + self.three > self.second and self.second + self.three > self.first:
            print("Ура, можно построить треугольник!")
        else:
            print("Жаль, но из этого треугольник не сделать.")


triangle = TriangleChecker(int(input("Введите длину 1-ого отрезка: ")), int(input("Введите длину 2-ого отрезка: ")), int(input("Введите длину 3-ого отрезка: ")))
triangle.is_triangle()