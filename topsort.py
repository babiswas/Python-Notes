from collections import defaultdict

class Graph:
   def __init__(self,v):
     self.vertices=v
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
     visited=[False]*self.vertices
     stack=[]
     for i in range(0,self.vertices):
       if not visited[i]:
           self.topsort_util(visited,stack,i)
     while stack:
        print(stack.pop())


if __name__=="__main__":
  g=Graph(6)
  g.addedges(5,0)
  g.addedges(5,2)
  g.addedges(4,0)
  g.addedges(4,1)
  g.addedges(2,3)
  g.addedges(3,1)
  g.topsort()


      