from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
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
   graph=Graph(4)
   graph.addedges(2,0)
   graph.addedges(0,2)
   graph.addedges(2,3)
   graph.addedges(3,3)
   graph.addedges(0,1)
   graph.addedges(1,2)
   print("Enter the graph through 2")
   graph.DFS(2)
   print("Enter the graph through 0")
   graph.DFS(0)
   print("Enter the graph through 3")
   graph.DFS(3)
   print("Enter the graph through 1")
   graph.DFS(1)

      