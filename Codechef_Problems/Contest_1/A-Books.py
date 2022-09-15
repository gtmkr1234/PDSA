import sys


def fun(a):
    res = []
    for i in range(len(a) - 1):
        count: int = 0
        for j in a[i + 1:]:
            if j > a[i]:
                count += 1
        res.append(count)
    res.append(0)
    return res


def display(a):
    for i in a:
        print(i, end=" ")


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    while n > 0:
        s = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        display(fun(a))
        n -= 1
        print()