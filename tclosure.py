from collections import defaultdict

class Graph:

   def __init__(self,V):
      self.vertex=V
      self.graph=defaultdict(list)

   def add_edges(self,u,v):
      self.graph[u].append(v)

   def transitive_closure(self):
       matrix=[[0 for i in range(self.vertex)] for j in range(self.vertex)]
       for i in range(N):
           self.DFS_util(matrix,i,i)       
       print([[matrix[j][i] for i in range(N)] for j in range(N)])
           
   def DFS_util(self,matrix,u,v):
       matrix[u][v]=1
       for i in self.graph[v]:
                  self.DFS_util(matrix,i,i)

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(0,1)
   graph.transitive_closure()

          