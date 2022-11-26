from Stack_Queue.queue import Queue


def bfsListPath(AList, v):
    (visited, parent) = ({}, {})
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    q = Queue()

    visited[v] = True
    q.addq(v)

    while not q.isEmpty():
        j = q.delq()
        for k in AList[j]:
            if not visited[k]:
                visited[k] = True
                parent[k] = j
                q.addq(k)
    return visited


def components(Alist):
    component = {}
    for i in Alist.keys():
        component[i] = -1

    (compid, seen) = (0, 0)
    while seen <= max(Alist.keys()):
        startv = min([i for i in Alist.keys() if component[i] == -1])
        visited = bfsListPath(Alist, startv)
        for i in visited.keys():
            seen += 1
            component[i] = compid
        compid += 1

    return compid

if __name__ == '__main__':
    edge_list = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"], "D": ["H", "I"], "E": ["J", "K"], "F": ["L", "M"], "G": ["N", "O"], "H": [], "I": [], "J": [], "K": [], "L": [], "M": [], "N": [], "O": []}
    print(components(edge_list))