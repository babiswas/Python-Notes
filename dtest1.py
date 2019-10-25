from collections import defaultdict
class Graph:
  def __init__(self,n):
     self.vertices=n
     self.graph=defaultdict(list)
  def add_edges(self,u,v):
     self.graph[u].append(v)
  def BFS(self,u):
     queue=[]
     visited=[False]*self.vertices
     queue.append(u)
     visited[u]=True
     while queue:
        p=queue.pop(0)
        print(p)
        for i in self.graph[p]:
            if not visited[i]:
               queue.append(i)
               visited[i]=True


if __name__=="__main__":
   g=Graph(4)
   g.add_edges(0,2)
   g.add_edges(2,0)
   g.add_edges(2,3)
   g.add_edges(3,3)
   g.add_edges(1,2)
   g.add_edges(0,1)
   g.BFS(2)
