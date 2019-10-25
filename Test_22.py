from collections import defaultdict

class Graph:
   def __init__(self,value):
      self.vertex=value
      self.graph=defaultdict(list)
   def addedges(self,u,v):
      self.graph[u].append(v)
   def topsort_util(self,visited,stack,u):
      visited[u]=True
      for i in self.graph[u]:
          if not visited[i]:
             self.topsort_util(visited,stack,i)
      stack.append(u)

   def topsort(self):
      stack=[]
      visited=[False]*self.vertex
      for i in range(0,self.vertex):
         if not visited[i]:
            self.topsort_util(visited,stack,i)
      while stack:
        print(stack.pop())

if __name__=="__main__":
   graph=Graph(6)
   graph.addedges(5,0)
   graph.addedges(5,2)
   graph.addedges(2,3)
   graph.addedges(3,1)
   graph.addedges(4,0)
   graph.addedges(4,1)
   graph.topsort()



      
      