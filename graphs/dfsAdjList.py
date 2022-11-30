def dfs(AdjList, visited, v):
    visited[v] = True
    for k in AdjList.keys():
        if not visited[k]:
            visited = dfs(AdjList, visited, k)
    return visited


if __name__ == '__main__':
    AdjList = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"], "D": ["H", "I"], "E": ["J", "K"], "F": ["L", "M"], "G": ["N", "O"], "H": [], "I": [], "J": [], "K": [], "L": [], "M": [], "N": [], "O": []}
    visited = {i: False for i in AdjList.keys()}
    print(dfs(AdjList, visited, "A"))

