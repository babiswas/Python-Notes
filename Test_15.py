from collections import defaultdict

timer=0

class Graph:
   def __init__(self,vertex):
      self.vertex=vertex
      self.graph=defaultdict(list)
      self.intime=[0]*self.vertex
      self.outtime=[0]*self.vertex
   def addedges(self,u,v):
      self.graph[u].append(v)
      self.graph[v].append(u)
   def DFS_util(self,visited,u):
       global timer
       visited[u]=True
       print(visited)
       timer=timer+1
       self.intime[u]=timer
       for i in self.graph[u]:
         if not visited[i]:
            self.DFS_util(visited,i)
       timer=timer+1
       self.outtime[u]=timer
   def query(self,u,v):
      return ((self.intime[u]<self.intime[v] and self.outtime[u]>self.outtime[v]) or (self.intime[u]>self.intime[v] and self.outtime[u]<self.outtime[v]))


if __name__=="__main__":
   graph=Graph(8)
   graph.addedges(1,2)
   graph.addedges(1,3)
   graph.addedges(1,4)
   graph.addedges(2,5)
   graph.addedges(3,6)
   graph.addedges(4,7)
   visited=[False]*graph.vertex
   print(visited)
   graph.DFS_util(visited,1)
   print(graph.intime)
   print(graph.outtime)
   print(graph.query(1,5))
   print(graph.query(2,6))
  
   

   
