def dfs(visited, Alist, v):
    visited[v] = True
    for i in Alist[v]:
        if not visited[i]:
            dfs(visited, Alist, i)
    return


def findMasterTank(tanks, pipes):
    Glist = {i: [] for i in tanks}
    for i, j in pipes:
        Glist[i].append(j)

    visited = {t: False for t in tanks}
    lastvisited = tanks[0]
    for t in tanks:
        if not visited[t]:
            dfs(visited, Glist, t)
            lastvisited = t

    visited = {t: False for t in tanks}
    dfs(visited, Glist, lastvisited)

    for v in visited:
        if not visited[v]:
            return 0
    return lastvisited


v = [item for item in input().split(" ")]
#Tanks(vertices) numbered from 1 to n in string format.
numberOfEdges = int(input())
e = []
for i in range(numberOfEdges):
  s = input().split(" ")
  e.append((s[0], s[1]))
print(findMasterTank(v, e))