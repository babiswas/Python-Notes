class Cell:
   def __init__(self,x=0,y=0,dist=0):
       self.x=x
       self.y=y
       self.dist=dist

def isinside(x,y,N):
    if x<0 or x>N:
        return False
    if y<0 or y>N:
        return False
    return True


def source_target(kpos,tpos,N):
    #Set the direction vectors
    dx=[2,2,-2,-2,-1,1,-1,1]
    dy=[1,-1,1,-1,2,2,-2,-2]
    visited=[[False for i in range(N+1)] for j in range(N+1)]
    visited[kpos[0]][kpos[1]]=True
    queue=[]
    queue.append(Cell(kpos[0],kpos[1],0))
    while queue:
       m=queue.pop(0)
       print(f"{m.x},{m.y},{m.dist}")
       if (m.x==tpos[0]) and (m.y==tpos[1]):
          print(f"Found {m.x} {m.y} {m.dist}")
          return m.dist
       for i in range(8):
             x=m.x+dx[i]
             y=m.y+dy[i]
             if isinside(x,y,N) and (visited[x][y]==False):
                 queue.append(Cell(x,y,m.dist+1))
                 visited[x][y]=True

if __name__=="__main__":
   kpos=[1,1]
   tpos=[28,28]
   N=30
   steps=source_target(kpos,tpos,N)
   print(f"The no of steps required is {steps}")



    
    
    

