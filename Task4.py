import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.v1 = vertice1
        self.v2 = vertice2
        self.v3 = vertice3

    def perimeter(self):
        print(self.v1._Point__x)
        print(self.v1._Point__x)
        side1 = math.hypot(abs(self.v1._Point__x - self.v2._Point__x), abs(self.v1._Point__y - self.v2._Point__y))
        side2 = math.hypot(abs(self.v1._Point__x - self.v3._Point__x), abs(self.v1._Point__y - self.v3._Point__y))
        side3 = math.hypot(abs(self.v2._Point__x - self.v3._Point__x), abs(self.v2._Point__y - self.v3._Point__y))
        return side1 + side2 + side3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())