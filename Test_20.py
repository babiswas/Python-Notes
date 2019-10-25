from collections import defaultdict

class Graph:
   def __init__(self,value):
      self.vertex=value
      self.graph=defaultdict(list)
   def addedges(self,u,v):
      self.graph[u].append(v)
   def find_all_path(self,u,v):
      visited=[False]*self.vertex
      path=[]
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
       visited[u]=False
       path.pop()

if __name__=="__main__":
   graph=Graph(4)
   graph.append(0,2)
   graph.append(2,3)
   graph.append(1,3)
   graph.append(0,1)
   graph.append(0,4)
   graph.append(4,1)
   graph.find_all_path(2,3)



