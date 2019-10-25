import json
class A:
  def __init__(self,a,b):
    self.a=a
    self.b=b
    self.obj=None
  def __str__(self):
    if not self.obj:
       return str(self.a)+'  '+str(self.b)
    else:
       return str(self.a)+'   '+str(self.b)+' '+json.dumps(self.obj.__dict__)
  class B:
    def __init__(self,a):
       self.a=a
  def fun(self,d):
     self.obj=self.B(d)
    
if __name__=="__main__":
   a=A(2,3)
   a.fun(6)
   print(a)
   print(a.__dict__)
   
   
