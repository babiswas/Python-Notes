from collections import defaultdict

class Graph:
  def __init__(self,v):
     self.vertex=v
     self.graph=defaultdict(list)
  def addedges(self,u,v):
     self.graph[u].append(v)
  def DFS(self,v):
     stack=[]
     visited=[False]*self.vertex
     stack.append(v)
     while stack:
        s=stack.pop()
        if not visited[s]:
            print(s)
            visited[s]=True
        for i in self.graph[s]:
           if not visited[i]:
              stack.append(i)

if __name__=="__main__":
  graph=Graph(5)
  graph.addedges(2,0)
  graph.addedges(0,2)
  graph.addedges(0,4)
  graph.addedges(0,1)
  graph.addedges(4,1)
  graph.addedges(1,3)
  graph.addedges(2,3)
  graph.DFS(2)
