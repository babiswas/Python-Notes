from collections import defaultdict

class Graph:
   def __init__(self,value):
      self.vertex=value
      self.graph=defaultdict(list)
   def addedges(self,u,v):
     self.graph[u].append(v)
   def DFS_util(self,visited,u):
       visited[u]=True
       for i in self.graph[u]:
         if not visited[i]:
            self.DFS_util(visited,i)
   def find_mother_vertex(self):
       visited=[False]*self.vertex
       m=0
       for i in range(0,self.vertex):
          if not visited[i]:
             self.DFS_util(visited,i)
             m=i
       visited=[False]*self.vertex
       self.DFS_util(visited,m)
       if False in visited:
         print("No mother vertex")
       else:
         print("{} is the mother vertex".format(m))

if __name__=="__main__":
  graph=Graph(6)
  graph.addedges(5,0)
  graph.addedges(5,2)
  graph.addedges(2,3)
  graph.addedges(3,1)
  graph.addedges(4,1)
  graph.addedges(4,0)
  graph.find_mother_vertex()
  print("Find the mother vertex for the current graph")
  graph=Graph(4)
  graph.addedges(2,0)
  graph.addedges(0,2)
  graph.addedges(2,3)
  graph.addedges(3,3)
  graph.addedges(0,1)
  graph.addedges(1,2)
  graph.find_mother_vertex()
  


       
      