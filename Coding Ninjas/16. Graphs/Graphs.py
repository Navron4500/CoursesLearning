
from sys import maxsize

# Adjaceny Matrix
class Graph:
    def __init__(self,nVertices) -> None:
        self.nVertices = nVertices
        self.adjMatirx = [[0 for i in range(nVertices)] for j in range(nVertices)]


    def addEdge(self,v1,v2,wt):
        self.adjMatirx[v1][v2] = wt
        self.adjMatirx[v2][v1] = wt

    def __minVertex(self,visited,dist):
        idx = -1
        mini = maxsize
        for i in range(self.nVertices):
            if dist[i] < mini and visited[i] is False:
                idx = i
                mini = dist[i]

        return idx

    def __getNeighbors(self,v,visited):
        adj = []
        for i in range(self.nVertices):
            if self.adjMatirx[i][v] > 0 and visited[i] is False:
                adj.append(i)
        
        return adj

    
    def dijsktra_algo(self):
        visited = [False for i in range(self.nVertices)]
        dist = [maxsize for _ in range(self.nVertices)]
        dist[0] = 0

        for _ in range(self.nVertices):
            current = self.__minVertex(visited,dist)
            visited[current] = True

            neighbors = self.__getNeighbors(current,visited)
            for neigh in neighbors:
                if dist[neigh] > dist[current] + self.adjMatirx[current][neigh]:
                    dist[neigh] = dist[current] + self.adjMatirx[current][neigh]
        

        return dist




g = Graph(4)
g.addEdge(0,1,3)
g.addEdge(0,3,5)

g.addEdge(1,2,1)
g.addEdge(2,3,8)
ans = g.dijsktra_algo()

for i in range(len(ans)):
    print(i,ans[i])