def sel_sort(L):
    n = len(L)
    if (n < 1):
        return L
    for i in range(n):
        mpos = i
        for j in range(i + 1, n):
            if L[j] < L[mpos]:
                mpos = j
        (L[i], L[mpos]) = (L[mpos], L[i])
    return (L)


if __name__ == '__main__':
    l = [5, 4, 3, 2, 1]
    sel_sort(l)
    print(l)
