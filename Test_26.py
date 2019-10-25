from collections import defaultdict

timer=0

class Graph:
   def __init__(self,value):
      self.vertex=value
      self.graph=defaultdict(list)
      self.intime=[0]*self.vertex
      self.outtime=[0]*self.vertex
   def addedges(self,u,v):
      self.graph[u].append(v)
      self.graph[v].append(u)
   def DFS_util(self,visited,u):
      visited[u]=True
      global timer
      timer=timer+1
      self.intime[u]=timer
      for i in self.graph[u]:
         if not visited[i]:
            self.DFS_util(visited,i)
      timer=timer+1
      self.outtime[u]=timer
   def query(self,u,v):
     return ((self.intime[u]<self.intime[v])and(self.outtime[u]>self.outtime[v])) or ((self.intime[v]<self.intime[u])and(self.outtime[v]>self.outtime[u]))
   

if __name__=="__main__":
  graph=Graph(9)
  graph.addedges(1,2)
  graph.addedges(1,7)
  graph.addedges(2,5)
  graph.addedges(2,6)
  graph.addedges(7,0)
  graph.addedges(7,4)
  graph.addedges(4,3)
  graph.addedges(4,8)
  visited=[False]*graph.vertex
  graph.DFS_util(visited,1)
  print(graph.intime)
  print(graph.outtime)
  print(graph.query(1,6))
  print(graph.query(2,0))
  print(graph.query(6,0))
  print(graph.query(1,00))


  