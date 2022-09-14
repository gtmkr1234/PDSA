class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def translate(self,deltax,deltay):
        self.x += deltax
        self.y +=deltay

    def odistance(self):
        import math
        d = math.sqrt(self.x**2 + self.y**2)
        return d


class Point2:
    def __init__(self, a=0, b=0):
        import math
        self.r = math.sqrt(a*a + b*b)
        if a == 0:
            theta = 0
        else:
            theta = math.atan(b/a)

    def odistance(self):
        return self.r

if __name__ == '__main__':
    s = Point2(3,4)
    print(s.odistance())