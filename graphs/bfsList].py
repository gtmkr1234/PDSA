from Stack_Queue.queue import Queue


def BFSListPath(AList, v):
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
    return visited, parent


if __name__ == '__main__':
    edge_list = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"], "D": ["H", "I"], "E": ["J", "K"], "F": ["L", "M"], "G": ["N", "O"], "H": [], "I": [], "J": [], "K": [], "L": [], "M": [], "N": [], "O": []}
    (vis, par) = BFSListPath(edge_list, "A")
    print(vis)
    print(par)
