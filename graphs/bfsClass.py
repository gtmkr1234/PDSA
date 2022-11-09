from queue import Queue

adj_lst = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"], "D": ["H", "I"], "E": ["J", "K"], "F": ["L", "M"], "G": ["N", "O"]}
visited = {}
level = {}
output = []
for i in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]:
    level[i] = -1
    visited[i] = False
s = "A" #Starting Index
visited[s] = True
level[s] = 0
queue = Queue()
queue.put(s)
while not queue.empty():
    u = queue.get()
    output.append(u)
    if u in adj_lst.keys():
        for v in adj_lst[u]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)
                level[v] = level[u] + 1
print(output)
print(level)
