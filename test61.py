import json

class A:
  def __init__(self,a,b):
     self.a=a
     self.b=b
  def __repr__(self):
     return "{} and {}".format(self.a,self.b)
  def fun(self):
     self.m=3
  def __radd__(self,other):
     if  isinstance(other,int):
        return other+self.a
  def __add__(self,other):
     if isinstance(other,A):
        return other.a+self.a
     elif isinstance(other,int):
        return other+self.a
     elif isinstance(other,str):
        return self.__str__()+'  '+other
     else:
        raise ValueError

     

if __name__=="__main__":
   a=A(2,3)
   print(a)
   print(a.__dict__)
   print(json.dumps(a.__dict__))
   a.fun()
   print(a.__dict__)
   b=A(5,3)
   print(b)
   print(a+b)
   print(a+2)
   print(a+"Mumbai")
   try:
      print(a+.23)
   except Exception as e:
      print("Exception occured")
      print(e)
   print(2+b)
   print(b+8)
