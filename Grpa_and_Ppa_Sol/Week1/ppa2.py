import math


class Triangle:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z

    def Is_valid(self):
        if ((self.a + self.b) > self.c) and ((self.b + self.c) > self.a) and ((self.a + self.c) > self.b):
            return "Valid"
        else:
            return "Invalid"

    def Side_Classification(self):
        if self.Is_valid() != "Invalid":
            if self.a == self.b == self.c:
                return "Equilateral"
            if self.a == self.b or self.b == self.c or self.a == self.c:
                return "Isosceles"
            else:
                return "Scalene"
        return "Invalid"

    def Angle_Classification(self):
        if self.Is_valid() != "Invalid":
            if self.a ** 2 + self.b ** 2 > self.c ** 2:
                return "Acute"
            if self.a ** 2 + self.b ** 2 < self.c ** 2:
                return "Obtuse"
            if self.a ** 2 + self.b ** 2 == self.c ** 2:
                return "Right"
        return "Invalid"

    def Area(self):
        if self.Is_valid() != "Invalid":
            s = (self.a+self.b+self.c)/2
            return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return "Invalid"

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    T = Triangle(a, b, c)
    print(T.Is_valid())
    print(T.Side_Classification())
    print(T.Angle_Classification())
    print(T.Area())
