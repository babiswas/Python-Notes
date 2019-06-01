class B:
  def __init__(self,name):
     self.name=name
  def __enter__(self):
     self.m=open(self.name,'w')
     return self
  def __exit__(self,x,y,z):
     if self.m:
        self.m.close()
  def printt(self):
     self.m.write(' ')
     self.m.write('hello')


if __name__=="__main__":
   with B("testtest.txt") as b:
       for i in range(0,10):
           b.printt()
