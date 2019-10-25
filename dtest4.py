from collections import defaultdict

class Graph:
   def __init__(self,n):
      self.graph=defaultdict(list)
      self.V=n

   def add_edges(self,u,v):
      self.graph[u].append(v)

   def find_all_path(self,u,v):
      path=[]
      visited=[False]*self.V
      self.find_all_path_util(visited,path,u,v)

   def find_all_path_util(self,visited,path,u,v):
      visited[u]=True
      path.append(u)
      if u==v:
        print(path)
      else:
        for i in self.graph[u]:
          if not visited[i]:
             self.find_all_path_util(visited,path,i,v)
      path.pop()
      visited[u]=False


if __name__=="__main__":
    g=Graph(4)
    g.add_edges(0,2)
    g.add_edges(2,0)
    g.add_edges(1,3)
    g.add_edges(0,1)
    g.add_edges(2,3)
    g.add_edges(3,3)
    g.find_all_path(2,3)

   
   


      