import sys


def find_Min_Difference(L, P):
    L.sort()
    min_diff = sys.maxsize
    n = len(L)
    for i in range(n - P + 1):
        min_diff = min(min_diff, abs(L[i] - L[i + P - 1]))
    return min_diff


if __name__ == '__main__':
    L = eval(input().strip())
    P = int(input())
    print(find_Min_Difference(L, P))
