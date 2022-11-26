def findAllPaths(vertices, gList, source, destination):
    output = []
    path = [source]
    visited = {}
    for i in vertices:
        visited[i] = False
    dfsu(source, destination, path, output, visited, gList)
    return output


def dfsu(source, destination, path, output, visited, gList):
    if (source == destination):
        output.append(path)
    for i in gList[source]:
        if not visited[i]:
            visited[i] = True
            dfsu(i, destination, path + [i], output, visited, gList)
        visited[i] = False
    return


# Vertices are expected to be labelled as single letter or single digit

# Sort and arrange the result for uniformity
def ArrangeResult(result):
    res = []
    for item in result:
        s = ""
        for i in item:
            s += str(i)
        res.append(s)
    res.sort()
    return res


v = [item for item in input().split(" ")]
Alist = {}
for i in v:
    Alist[i] = [item for item in input().split(" ") if item != '']
source = input()
dest = input()
print(ArrangeResult(findAllPaths(v, Alist, source, dest)))