def InsertionSort(L):
    n = len(L)
    for i in range(n):
        j = i
        while (j > 0 and L[j] < L[j - 1]):
            (L[j], L[j - 1]) = (L[j - 1], L[j])
            j -= 1
    return(L)

def Insert(L,v):
    n=len(L)
    if n==0:
        return([v])
    if(v>L[-1]):
        return(L+[v])
    else:
        return(Insert(L[:-1],v)+L[-1:])


def Isort(L):
    n=len(L)
    if(n<1):
        return(L)
    L=Insert(Isort(L[:-1]),L[-1])
    return(L)


if __name__ == '__main__':
    print(InsertionSort([5,4,3,2,1]))
    print(Isort([6,2,1,4,8,9,10,0,54,8,32]))