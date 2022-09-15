def canJump(n):
    true_stmt = "yes"
    false_stmt = "no"
    if n % 3 == 0 or n % 6 == 1:
        return true_stmt
    return false_stmt


if __name__ == '__main__':
    n = int(input())
    print(canJump(n))
