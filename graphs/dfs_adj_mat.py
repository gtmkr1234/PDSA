import numpy as np


def dfs_init(AdjMat, v):
    (rows, cols) = AdjMat.shape
    (visited, parent) = ({}, {})
    for i in range(rows):
        visited[i] = False
        parent[i] = -1
    return dfs(AdjMat, visited, parent, v)


def neighbours(AdjMat, ver):
    res = []
    (row, col) = AdjMat.shape
    for j in range(col):
        if AdjMat[ver][j] == 1:
            res.append(j)
    return res


def dfs(AdjMat, visited, parent, v):
    visited[v] = True
    for k in neighbours(AdjMat, v):
        if not visited[k]:
            parent[k] = v
            (visited, parent) = dfs(AdjMat, visited, parent, k)
    return visited, parent


if __name__ == '__main__':
    edge_list = [(0, 1), (1, 2), (2, 3), (0, 2), (3, 2), (4, 5), (5, 4), (3, 4)]
    mat = np.zeros(shape=(10, 10))
    for (i, j) in edge_list:
        mat[i, j] = 1
    (vis, par) = dfs_init(mat, 1)
    print(vis)
    print(par)

