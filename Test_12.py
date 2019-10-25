from collections import defaultdict

class Graph:
   def __init__(self,vertices):
      self.vertex=vertices
      self.graph=defaultdict(list)
   def addedges(self,u,v):
      self.graph[u].append(v)
   def DFS(self,u):
      visited=[False]*self.vertex
      self.DFS_util(visited,u)
   def DFS_util(self,visited,u):
       visited[u]=True
       print(u)
       for i in self.graph[u]:
           if not visited[i]:
              self.DFS_util(visited,i)

if __name__=="__main__":
  graph=Graph(6)
  graph.addedges(5,0)
  graph.addedges(5,2)
  graph.addedges(2,3)
  graph.addedges(3,1)
  graph.addedges(4,0)
  graph.addedges(4,1)
  graph.DFS(5)

      
      
      