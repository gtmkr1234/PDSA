def dfs(visited, Alist, v):
    visited[v] = True
    for i in Alist[v]:
        if not visited[i]:
            dfs(visited, Alist, i)
    return


def findComponents_undirectedGraph(vertices, edges):
    Alist, visited = {}, {}
    compid = 0
    for i in vertices:
        Alist[i] = []
        visited[i] = False

    for (i, j) in edges:
        Alist[i].append(j)
        Alist[j].append(i)

    while (len([k for k in visited if not visited[k]]) >= 1):
        ver = min([k for k in visited if not visited[k]])
        dfs(visited, Alist, ver)
        compid += 1
    return compid