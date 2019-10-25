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
   #Nodes at level k from given node.
   def BFS_k(self,u,k):
      queue=[]
      visited=[False]*self.vertices
      queue.append(u)
      len_queue=0
      count=0
      visited[u]=True
      while queue:
         len_queue=len(queue)
         if count==k:
             break
         else:
            count=count+1
         while len_queue:
             s=queue.pop(0)
             for i in self.graph[s]:
                 if not visited[i]:
                    queue.append(i)
                    visited[i]=True
             len_queue=len_queue-1
         print(count)
      print(queue)
      

if __name__=="__main__":
   graph=Graph(4)
   graph.addedges(2,0)
   graph.addedges(0,2)
   graph.addedges(2,3)
   graph.addedges(3,3)
   graph.addedges(0,1)
   graph.addedges(1,2)
   graph.BFS(2)
   print("Nodes at level 1 from 2")
   graph.BFS_k(2,2)
