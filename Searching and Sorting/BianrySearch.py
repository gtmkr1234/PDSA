def binarySearch(lst: list[int], val: int) -> bool:
    start = 0
    end = len(lst)-1

    while end-start > 1:
        mid = (start + end) // 2
        if lst[mid] == val:
            return True
        if lst[mid] > val:
            end = mid-1
        if lst[mid] < val:
            start = mid+1
    if lst[start] == val or lst[end] == val:
        return True
    return False


