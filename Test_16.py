from collections import defaultdict

class Graph:
   def __init__(self,vertices):
     self.vertices=vertices
     self.graph=defaultdict(list)

   def addedges(self,u,v):
      self.graph[u].append(v)

   def BFS(self,u):
      queue=[]
      visited=[False]*self.vertices
      queue.append(u)
      visited[u]=True
      while queue:
        s=queue.pop(0)
        print(s)
        for i in self.graph[s]:
           if not visited[i]:
              queue.append(i)
              visited[i]=True


if __name__=="__main__":
   graph=Graph(4)
   graph.addedges(2,0)
   graph.addedges(0,2)
   graph.addedges(2,3)
   graph.addedges(3,3)
   graph.addedges(0,1)
   graph.addedges(1,2)
   graph.BFS(2)
