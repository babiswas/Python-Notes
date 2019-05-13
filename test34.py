class A:
  def __init__(self,a,b):
     self.a=a
     self.b=b
     self.c=0
  def __iter__(self):
     return self
  def __next__(self):
     if self.c!=10:
       temp=self.c
       self.c=self.c+1
       return temp
     else:
       raise StopIteration

if __name__=="__main__":
  a=A(2,3)
  print("Display the iterator using next method")
  print(next(a))
  print(next(a))
  print(next(a))
  print(next(a))
  print(next(a))
  print(next(a))
  print(next(a))
  print(next(a))
  print(next(a))
  print(next(a))
  print(next(a))