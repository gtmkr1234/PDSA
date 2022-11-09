from queue import Queue

adj_lst = {"A":["B","C"], "B":["D","E"], "C":["B","F"], "E":["F"]}
visited = {}
level = {}
output = []
for i in ["A","B","C","D","E","F"]:
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
            if visited[v] == False:
                visited[v] = True
                queue.put(v)
                level[v] = level[u] + 1
print(output)
print(level)
