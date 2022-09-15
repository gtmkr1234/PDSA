def factorsof(n):
    factor = []
    for i in range(1, n + 1):
        if n % i == 0:
            factor.append(i)
    return factor


def isprime(a):
    if len(factorsof(a)) == 2:
        return True
    return False


def primelist(n):
    pl = []
    for i in range(1, n + 1):
        if isprime(i):
            pl.append(i)
    return pl


def Goldbach(num):
    plst = primelist(num)
    length = len(plst)
    res = []
    for i in range(length):
        for j in range(i, length):
            if plst[i] + plst[j] == num:
                res.append((plst[i], plst[j]))
    return res


if __name__ == '__main__':
    n = int(input())
    print(sorted(Goldbach(n)))
