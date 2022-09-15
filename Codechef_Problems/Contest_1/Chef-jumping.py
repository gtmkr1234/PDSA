def canJump(n):
    true_stmt = "yes"
    false_stmt = "no"
    if n == 0:
        return true_stmt
    while n > 0:
        n -= 1
        if n == 0:
            return true_stmt
        n -= 2
        if n == 0:
            return true_stmt
        n -= 3
        if n == 0:
            return true_stmt
    return false_stmt


if __name__ == '__main__':
    n = int(input())
    print(canJump(n))
