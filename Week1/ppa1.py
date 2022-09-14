def factors(n):
    factor = []
    for i in range(1, n + 1):
        if n % i == 0:
            factor.append(i)
    return factor


def prime(a):
    if len(factors(a)) == 2:
        return True
    return False


def primes(n, m):
    lst = []
    for i in range(n, m + 1):
        if prime(i):
            lst.append(i)
    return lst


def Twin_Primes(n, m):
    res = []
    lst = primes(n,m)
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if lst[j]-lst[i]==2:
                res.append((lst[i],lst[j]))
    return res


if __name__ == '__main__':
    # n = int(input())
    # m = int(input())
    # print(sorted(Twin_Primes(n, m)))
    print(Twin_Primes(2,6))