# Import Library
from collections import defaultdict

# Function
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def solve(self, s, d):
        path = []
        with open('bai2.out') as f:
            path = [int(x) for x in next(f).split()]

        if path[0] == -1:
            visited = set()
            self.DFSUtil(s, visited)
            for i in visited:
                if i == d:
                    print("Incorrect!! X_X")
                    return
            print("Correct!! ^o^")
        else:
            sz = len(path)
            if path[sz - 1] != d:
                print("Incorrect!! X_X")
                return
            for i in range(0, sz - 1):
                u = path[i]
                v = path[i + 1]
                check = 0
                for neighbour in self.graph[u]:
                    if neighbour == v:
                        check = 1
                if check == 0:
                    print("Incorrect!! X_X")
                    return
            print("Correct!! ^o^")


# Main

# Read file output
g = Graph()
with open('bai2.inp') as f:
    n, m, s, d = [int(x) for x in next(f).split()]  # read first line
    for line in f:  # read rest of lines
        u, v = [int(x) for x in line.split()]
        g.addEdge(u, v)
        g.addEdge(v, u)
    g.solve(s, d)