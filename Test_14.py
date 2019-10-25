from collections import defaultdict

class Graph:
   def __init__(self,vertex):
     self.vertex=vertex
     self.graph=defaultdict(list)
   def  addedges(self,u,v):
     self.graph[u].append(v)
   def DFS(self,u):
     stack=[]
     visited=[False]*self.vertex
     stack.append(u)
     while stack:
        s=stack.pop()
        if not visited[s]:
          print(s)
          visited[s]=True
        for i in self.graph[s]:
          if not visited[i]:
             stack.append(i)


if __name__=="__main__":
  graph=Graph(6)
  graph.addedges(5,0)
  graph.addedges(5,2)
  graph.addedges(4,1)
  graph.addedges(4,0)
  graph.addedges(2,3)
  graph.addedges(3,1)
  graph.DFS(5)
