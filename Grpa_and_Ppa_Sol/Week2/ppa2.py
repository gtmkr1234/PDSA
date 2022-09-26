def sortInRange(L,r):
    n = len(L)
    cnt = dict({i for i in range(r)})
    for i in range(n):
        cnt[L[i]] += 1
    print(cnt)

if __name__ == '__main__':
    sortInRange([5,4,3,2,1],6)