import queue

# Adjaceny Matrix
class Graph:
    def __init__(self,nVertices) -> None:
        self.nVertices = nVertices
        self.adjMatirx = [[0 for i in range(nVertices)] for j in range(nVertices)]


    def addEdge(self,v1,v2):
        self.adjMatirx[v1][v2] = 1
        self.adjMatirx[v2][v1] = 1


    def __hasPathHelper(self,v1,v2,visited):
        adj = []
        visited[v1] = True

        # Adjacent Matrix Check
        for i in range(self.nVertices):
            if (self.adjMatirx[v1][i] > 0 and visited[i] is False):
                adj.append(i)
                if   i == v2:
                    return True
        
        for ele in adj:
            ans = self.__hasPathHelper(ele,v2,visited)
            if ans:
                return True
        return False    

    def hasPath(self,v1,v2):
        # DFS (DEPTH FIRST SEARCH)
        # ans = False
        visited = [False for i in range(self.nVertices)]
        ans = self.__hasPathHelper(v1,v2,visited)
        
        return ans

    def __getPathDFSHelper(self,v1,v2,visited, soFar = []):
        adj = []
        visited[v1] = True
        if v1 == v2:
            soFar.reverse()
            for k in soFar:
                print(k,end=" ")
            return True


        for i in range(self.nVertices):
            if (self.adjMatirx[v1][i] > 0 and visited[i] is False):
                adj.append(i)
        
        for ele in adj:
            newSoFar = soFar + [ele]
            ans = self.__getPathDFSHelper(ele,v2,visited,newSoFar)
            if ans:
                return True
        return False

    def getPathDFS(self,v1,v2):
        visited = [False for i in range(self.nVertices)]
        self.__getPathDFSSHelper(v1,v2,visited,[v1])

    def getPathBFS(self,v1,v2):
        visited = [False for i in range(self.nVertices)]
        d = {}

        q = queue.Queue()
        q.put(v1)
        visited[v1] = True
        d[v1] = [v1]


        while not q.empty():
            current = q.get()
            if current == v2:
                print(*d[current])
                return

            for i in range(self.nVertices):
                if self.adjMatirx[current][i] > 0 and visited[i] is False:
                    visited[i] = True
                    toEnqueue = [i] + d[current]
                    d[i] = toEnqueue
                    q.put(i)
        return None

    def bfs(self):
        # BFS = BREATH FIRST SEARCH

        count = 0
        for i in range(self.nVertices):
            count += self.adjMatirx[i].count(1)
        if  count == 0:
            for i  in range(self.nVertices):
                print(i,end=" ")
            return

        
        visited = [False for i in range(self.nVertices)]
        q = queue.Queue()
        q.put(0)
        visited[0] = True
        while not q.empty():
            current_vertx = q.get()
            print(current_vertx,end=" ")
            # visited[current_vertx] = True
            for i in range(self.nVertices):
                if self.adjMatirx[current_vertx][i] > 0 and visited[i] == False:
                    q.put(i)
                    visited[i] = True

    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return 
        self.adjMatirx[v1][v2] = 0
        self.adjMatirx[v2][v1] = 0


    def containsEdge(self,v1,v2):
        return True if self.adjMatirx[v1][v2] > 0 else False

    def __connectedHelper(self,v,visited):
        if visited.count(True) == self.nVertices-1:
            return True
        
        visited[v] = True
        for i in range(self.nVertices):
            if visited[i] is False and self.adjMatirx[v][i] > 0:
                res = self.__connectedHelper(i,visited)
                if res:
                    return True
        return False

    def connected(self):
        visited = [False for i in range(self.nVertices)]
        res = self.__connectedHelper(0,visited)
        return res


    def __allConnected(self,v,visited):
        adj = []
        for i in range(self.nVertices):
            if self.adjMatirx[v][i] > 0 and visited[i] is False:
                visited[i] = True
                adj.append(i)
        
        visited[v] = True
        if len(adj) == 0:
            return [v]
        
        ans = []

        for ele in adj:
            newans = self.__allConnected(ele,visited)
            ans = ans + newans
        return [v] + ans

    def allConnected(self):
        visited = [False for i in range(self.nVertices)]
        res = []
        for i in range(self.nVertices):
            if visited[i] is False:
                newRes = self.__allConnected(i,visited)
                res.append(newRes)
        for l in res:
            print(*l)

    def __str__(self):
        return str(self.adjMatirx)


g = Graph(9)
g.addEdge(0,8)
g.addEdge(1,6)
g.addEdge(1,7)
g.addEdge(1,8)
g.addEdge(5,8)
g.addEdge(6,0)
g.addEdge(7,3)
g.addEdge(7,4)
g.addEdge(8,7)
g.addEdge(2,5)

g.allConnected()



# V,E = input().split()
# vert,edge = int(V), int(E)
# g = Graph(vert)
# for i in range(edge):
#     v1,v2 = input().split()
#     g.addEdge(int(v1),int(v2))

# v1,v2 = input().split()
# g.getPathDFS(int(v1),int(v2))
        
