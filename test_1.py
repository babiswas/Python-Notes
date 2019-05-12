class A:
  value=2
  def __init__(self,a,b):
     self.a=a
     self.b=b
  def __str__(self):
     return str(self.a)+'  '+str(self.b)
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
  def sum(self):
    return self.a+self.b

if __name__=="__main__":
  a=A(2,4)
  print(a)
  a.seta=5
  a.setb=5
  print(a)
  if hasattr(a,'sum'):
     print("The object has this attributes")
  else:
     print("The object doesn't have this attributes")
  print(str(A.value)+'is the value of the static variable')

