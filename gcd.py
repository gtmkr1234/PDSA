def gcd(m, n):
    (a, b) = (max(m, n), min(m, n))
    if a % b == 0:
        return b
    else:
        return gcd(b, (a - b))


def gcd_euclid(m, n):
    (a, b) = (max(m, n), min(m, n))
    if a % b == 0:
        return b
    else:
        return gcd_euclid(b, a % b)


if __name__ == "__main__":
    print(gcd_euclid(95, 2))
