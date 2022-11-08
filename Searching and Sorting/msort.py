import sys

sys.setrecursionlimit(2 ** 31 - 1)


def mergeSort(A: list[int]):
    if(len(A)==1):
        return A
    mid = len(A)//2
    L = A[:mid]
    R = A[mid+1:]
    merge(L,R)


def merge(L:list[int],R:list[int]):
    



if __name__ == '__main__':
    print(mergeSort([5, 4, 3, 2, 1], 0, 5))
