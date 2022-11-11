from Stack_Queue.queue import Queue
import numpy as np


def bfsAdjMat(AdjMat, vertex):
    (rows, cols) = AdjMat.shape
    visited = {}
    for start in range(rows):
        visited[start] = False
    q = Queue()

    visited[vertex] = True
    q.addq(vertex)

    while not q.isEmpty():
        temp = q.delq()
        for k in neighbours(AdjMat, temp):
            if not visited[k]:
                visited[k] = True
                q.addq(k)

    return visited


def neighbours(AdjMat, ver):
    res = []
    (row, col) = AdjMat.shape
    for j in range(col):
        if AdjMat[ver][j] == 1:
            res.append(j)
    return res


if __name__ == '__main__':
    edge_list = [(0, 1), (1, 2), (2, 3), (0, 2), (3, 2), (4, 5), (5, 4), (3, 4)]
    mat = np.zeros(shape=(10, 10))
    for (i, j) in edge_list:
        mat[i, j] = 1

    print(bfsAdjMat(mat, 1))
