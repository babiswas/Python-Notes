import json

class A:
  def __init__(self,a,b):
     self.a=a
     self.b=b
  @property
  def seta(self):
     return self.a
  @seta.setter
  def seta(self,a):
     self.a=a
  @property
  def setb(self):
    return self.b
  @setb.setter
  def setb(self,b):
     self.b=b


class B:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def seta(self,a):
     self.a=a
  def setb(self,b):
     self.b=b
  def geta(self):
     return self.a
  def getb(self):
     return self.b
  def dela(self):
     print("Deleted a")
     del self.a
  def delb(self):
     del self.b

  val=property(geta,seta,dela)
  pal=property(getb,setb,delb)

if __name__=="__main__":
    a=A(2,3)
    print("Default value of a")
    print(a.seta)
    a.seta=4
    print("Modified value of b")
    print(a.seta)
    print("Default value of b")
    print(a.setb)
    a.setb=5
    print("Modified value of b")
    print(a.setb)
    print(a.__dict__)
    print(json.dumps(a.__dict__))
    b=B(2,3)
    print("Value of a is")
    print(b.val)
    print("Modified value of a is")
    b.val=10
    print(b.val)
    del b.val
    print(b.__dict__)
