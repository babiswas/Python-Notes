from collections import defaultdict

class Graph:
   def __init__(self,vertex):
     self.vertex=vertex
     self.graph=defaultdict(list)
   def addedges(self,u,v):
      self.graph[u].append(v)
   def DFS_util(self,visited,u):
       visited[u]=True
       for i in self.graph[u]:
          if not visited[i]:
             self.DFS_util(visited,i)
   def Mother_vertex(self):
      visited=[False]*self.vertex
      m=0
      for i in range(0,self.vertex):
          if not visited[i]:
              self.DFS_util(visited,i)
              m=i
              print(i)
      visited=[False]*self.vertex
      self.DFS_util(visited,m)
      if False not in visited:
         print("{} is the mother vertex".format(m))
      else:
         print("No mother vertex in the graph")

if __name__=="__main__":
   graph=Graph(6)
   graph.addedges(5,0)
   graph.addedges(5,2)
   graph.addedges(5,4)
   graph.addedges(4,1)
   graph.addedges(4,0)
   graph.addedges(4,5)
   graph.addedges(2,3)
   graph.addedges(3,1)
   graph.Mother_vertex()


      