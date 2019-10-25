from collections import defaultdict

class Graph:
   def __init__(self,n):
      self.V=n
      self.graph=defaultdict(list)
   def addedges(self,u,v):
      self.graph[u].append(v)
   def DFS(self,u):
      stack=[]
      visited=[False]*self.V
      stack.append(u)
      while stack:
         val=stack.pop()
         if not visited[val]:
            print(val)
            visited[val]=True
         for i in self.graph[val]:
           if not visited[i]:
               stack.append(i)

if __name__=="__main__":
   graph=Graph(4)
   graph.addedges(2,0)
   graph.addedges(0,2)
   graph.addedges(1,2)
   graph.addedges(0,1)
   graph.addedges(2,3)
   graph.addedges(3,3)
   graph.DFS(2)
