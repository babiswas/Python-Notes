from collections import defaultdict

class Graph:
    def __init__(self,value):
       self.vertex=value
       self.graph=defaultdict(list)
    def addedges(self,u,v):
       self.graph[u].append(v)
    def topsort(self):
       count=0
       indegree=[0]*self.vertex
       queue=[]
       for i in range(0,self.vertex):
         for j in self.graph[i]:
              indegree[j]=indegree[j]+1
       for i in range(0,self.vertex):
           if indegree[i]==0:
              queue.append(i)
       while queue:
          s=queue.pop(0)
          print(s)
          for i in self.graph[s]:
             indegree[i]=indegree[i]-1
             if indegree[i]==0:
                 queue.append(i)
          count=count+1
       if count==self.vertex:
          print("Topsort is possible for this graph")
       else:
          print("The graph has a cycle")

if __name__=="__main__":
   graph=Graph(6)
   graph.addedges(5,0)
   graph.addedges(5,2)
   graph.addedges(2,3)
   graph.addedges(3,1)
   graph.addedges(4,0)
   graph.addedges(4,1)
   graph.topsort()
   print("REsult for the cyclic graph")
   graph1=Graph(5)
   graph1.addedges(2,0)
   graph1.addedges(0,2)
   graph1.addedges(2,3)
   graph1.addedges(0,1)
   graph1.addedges(1,3)
   graph1.addedges(0,4)
   graph1.addedges(4,1)
   graph1.topsort()



                  
          
          