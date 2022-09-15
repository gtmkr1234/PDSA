def canJump(n):
    true_stmt = "yes"
    false_stmt = "no"
    num = 0
    while num < n:
        num += 1
        if num == n:
            return true_stmt
        num += 2
        if num == n:
            return true_stmt
        num += 3
        if num == n:
            return true_stmt
    return false_stmt


if __name__ == '__main__':
    n = int(input())
    print(canJump(n))
