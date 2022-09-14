class Triangle:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.z = z


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    T = Triangle(a, b, c)
    print(T.Is_valid())
    print(T.Side_Classification())
    print(T.Angle_Classification())
    print(T.Area())
