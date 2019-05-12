class A:
  vehicles=2
  def __init__(self,a,b):
     self.a=a
     self.b=b
  @property
  def seta(self):
     return self.a
  @property
  def setb(self):
     return self.b
  @seta.setter
  def seta(self,a):
    self.a=a
  @setb.setter
  def setb(self,b):
    self.b=b

if __name__=="__main__":
  a=A(3,4)
  print(a.seta)
  print(a.setb)
  a.seta=10
  a.setb=11
  print(a.seta)
  print(a.setb)
  if hasattr(a,"seta"):
     print("seta")
  if hasattr(a,"setb"):
     print("setb")