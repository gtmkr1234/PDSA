def binarySearchIndexAndComparisons(L, k):
    if len(L)<1:
        return False, 0
    count = 0
    while L:
        mid = (len(L)-1) // 2
        count += 1
        if L[mid] == k:
            return True, count
        if L[mid] < k:
            L = L[mid + 1:]
        if L[mid] > k:
            L = L[:mid]

    return False, count


if __name__ == '__main__':
    L = list(map(int,input().split(',')))
    a = int(input())
    print(binarySearchIndexandComparisons(L , a))
