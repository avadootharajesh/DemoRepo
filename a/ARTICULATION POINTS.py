
# Finding Articulation Points in a Graph

# Time Complexity : O(V + E)
# Space Complexity : O(V)

from collections import defaultdict as dd

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = dd(list)
        self.time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def aputil(self, u, visited, ap, parent, low, disc):
        children = 0
        visited[u] = True

        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        
        for v in self.graph[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                self.aputil(v, visited, ap, parent, low, disc)
                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1: ap[u] = True
                if parent[u] != -1 and low[v] >= disc[u]: ap[u] = True
            elif v != parent[u]: low[u] = min(low[u], disc[v])

        if parent[u] == -1 and children > 1: ap[u] = True

    def articulationPoints(self):
        visited = [False] * self.vertices
        disc = [float('inf')] * self.vertices
        low = [float('inf')] * self.vertices
        parent = [-1] * self.vertices
        ap = [False] * self.vertices

        for i in range(self.vertices):
            if not visited[i]: self.aputil(i, visited, ap, parent, low, disc)

        for i in range(self.vertices):
            if ap[i]: print(i, end = " ")

        print()

g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print ("\nArticulation points in first graph ")
g1.articulationPoints()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("\nArticulation points in second graph ")
g2.articulationPoints()

g3 = Graph (7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print ("\nArticulation points in third graph ")
g3.articulationPoints()