import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None
        self._elapsed_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop()")
        self._start_time = time.perf_counter()

    def stop(self):
        """Save the elapsed time and re-initialize timer"""
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start()")
        self._elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

    def elapsed(self):
        """Report elapsed time"""
        if self._elapsed_time is None:
            raise TimerError("Timer has not been run yet. Use .start()")
        return (self._elapsed_time)

    def __str__(self):
        """print() prints elapsed time"""
        return (str(self._elapsed_time))


import sys
sys.setrecursionlimit(2**31-1)


def merge(A, B):
    (m, n) = (len(A), len(B))
    (C, i, j, k) = ([], 0, 0, 0)
    while k < m + n:
        if i == m:
            C.extend(B[j:])
            k = k + (n - j)

        elif j == n:
            C.extend(A[i:])
            k = k + (m - i)

        elif A[i] < B[j]:
            C.append(A[i])
            (i, k) = (i + 1, k + 1)

        else:
            C.append(B[j])
            (j, k) = (j + 1, k + 1)

    return C


def sort(A):
    n = len(A)
    if n <= 1:
        return A
    L = sort(A[:n // 2])
    R = sort(A[n // 2:])

    B = merge(L, R)
    return B


if __name__ == '__main__':
    t=Timer()
    t.start()
    sort([i for i in range(0,1000000,2)]+[j for j in range(1,1000000,2)])
    t.stop()
    print(t)