def binarySearchIndexandComparisons(L, k):
    left = 0
    right = len(L) - 1
    count = 0

    while right - left > 1:
        mid = (left + right) // 2
        if L[mid] == k:
            count += 1
            return True, count
        if L[mid] < k:
            count += 1
            left = mid + 1
        if L[mid] > k:
            count += 1
            right = mid

    if (L[left] == k) or (L[right] == k):
        return True, count

    return False, count + 2


if __name__ == '__main__':
    L = list(map(int,input().split(',')))
    a = int(input())
    print(binarySearchIndexandComparisons(L , a))
