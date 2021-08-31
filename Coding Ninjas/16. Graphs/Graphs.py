import queue
from sys import maxsize

# Adjaceny Matrix
class Graph:
    def __init__(self,nVertices) -> None:
        self.nVertices = nVertices
        self.adjMatirx = [[0 for i in range(nVertices)] for j in range(nVertices)]


    def addEdge(self,v1,v2,wt):
        self.adjMatirx[v1][v2] = wt
        self.adjMatirx[v2][v1] = wt

    def __getMinVertex(self,wt,visited):
        
        min_vertex = -1
        for i in range(self.nVertices):
            if visited[i] is False and (min_vertex == -1 or wt[min_vertex] > wt[i]):
                min_vertex = i
        return min_vertex


    def prims(self):
        visited = [False for i in range(self.nVertices)]    
        parent = [-1 for i in range(self.nVertices)]
        wt = [maxsize for i in range(self.nVertices)]
        wt[0] = 0


        for i in range(self.nVertices-1):
            min_vertex = self.__getMinVertex(wt,visited)
            visited[min_vertex] = True

        # Explore the Neighbours of minVertex which is not visited and 
        # Update the weight of them if requried

            for j in range(self.nVertices):
                if self.adjMatirx[min_vertex][j] > 0 and visited[j] is False:
                    if(wt[j] > self.adjMatirx[min_vertex][j]):
                        wt[j] = self.adjMatirx[min_vertex][j]
                        parent[j] = min_vertex

        for i in range(1,self.nVertices):
            if parent[i] < i:
                print(parent[i],i,wt[i])
            else:
                print(i,parent[i],wt[i])




g = Graph(4)
g.addEdge(0,1,3)
g.addEdge(0,3,5)
g.addEdge(1,2,1)
g.addEdge(2,3,8)
g.prims()

# print("----------------------------")
# print("""0 1 2
# 2 3 2
# 1 3 2""")