class A:
  def __init__(self,a,b):
     self.a=a
     self.b=b
  def __iter__(self):
     return self
  def __next__(self):
     if self.a!=self.b:
       temp=self.a
       self.a=self.a+1
       return temp
     

if __name__=="__main__":
   a=A(0,4)
   print(a.__dict__)
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))

   