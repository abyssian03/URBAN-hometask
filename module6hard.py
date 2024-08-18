from math import sqrt

pi = 3.1415926

def side_condition(num):
    if isinstance(num, int) and num > 0:
        return (True)
    return (False)

def input_sides():
    str = input("Введите новые данные длины (через пробел): ")
    sides = [int(substr) for substr in str.split()]
    return (sides)

def color_condition(num):
    if isinstance(num, int) and num >= 0 and num <= 255:
        return (True)
    return (False)

def input_color():
    print("Введите новые данные цвета")
    rgb = []
    for str in ["R", "G", "B"]:
        rgb.append(int(input(f"Значение для {str}: ")))
    return (rgb)

class Figure:
    sides_count = 0

    def __init__(self, sides_count, __sides, __color, filled):
        self.sides_count = sides_count
        if len(__sides) == self.sides_count and all([side_condition(num) for num in __sides]):
            self.__sides = __sides
        else:
            print("Несовпадение параметров, использовано значение длины по умолчанию")
            self.__sides = [1] * self.sides_count
        if len(__color) == 3 and all([color_condition(num) for num in __color]):
            self.__color = __color
        else:
            print("Несовпадение параметров, использовано значение цвета по умолчанию")
            self.__color = [0] * 3
        self.filled = bool(filled)

    def get_color(self):
        return (self.__color)

    def __is_valid_color(self, r, g, b):
        for i in (r, g, b):
            if not color_condition(i):
                print(f"Недопустимое значение: {i}")
                return (False)
        return (True)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            print(f"Цвет изменен")
            self.__color = (r, g, b)
        else:
            print("Изменения не внесены")

    def __is_valid_sides(self, sides):
        if len(sides) != self.sides_count:
            print("Несовпадение параметров")
            return (False)
        for side in sides:
            if not (isinstance(side, int) and side > 0):
                print(f"Недопустимое значение: {side}")
                return (False)
        return (True)

    def get_sides(self):
        return (self.__sides)

    def __len__(self):
        return (sum(self.__sides))

    def set_sides(self, new_sides):
        if self.__is_valid_sides(new_sides):
            print("Геометрия изменена")
            self.__sides = new_sides
        else:
            print("Изменения не внесены")

class Circle(Figure):
    def __init__(self, *args):
        Figure.__init__(self, 1, *args)

    def radius(self):
        return (len(self) / (2*pi))

    def get_square(self):
        return (pi * (self.radius() ** 2))

class Triangle(Figure):
    def __init__(self, *args):
        Figure.__init__(self, 3, *args)

    def get_square(self):
        p = len(self) / 2
        s = p
        for side in self.get_sides():
            s = s * (p - side)
        s = sqrt(s)
        return (s)

class Cube(Figure):
    def __init__(self, side, *args):
        side_list = side * 12
        Figure.__init__(self, 12, side_list, *args)

    def get_volume(self):
        return (self.get_sides()[0] ** 3)

circle = Circle([5], (50, 50, 50), 0)
print("Радиус окружности:", circle.radius())
print("Цвет окружности", circle.get_color())
circle.set_color(*input_color())
circle.set_sides(input_sides())
print("Площадь круга:", circle.get_square())
triangle = Triangle([3, 4, 5], (4, 5, 6), 10)
print("Длины сторон треугольника:", triangle.get_sides())
print ("Заполненность треугольника:", triangle.filled)
triangle.set_sides(input_sides())
print("Площадь треугольника:", triangle.get_square())
cube = Cube([-3], (33, 33, 33), 1)
print("Сумма ребер куба:", len(cube))
print("Цвет куба:", cube.get_color())
print("Объем куба:", cube.get_volume())
