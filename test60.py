from contextlib import contextmanager

class A:
   def __init__(self,name):
      self.name=name
   def __enter__(self):
      self.m=open(self.name,'w')
      return self.m
   def __exit__(self,x,y,z):
      if self.m:
        self.m.close()


@contextmanager
def test(name):
   try:
      m=open(name,'w')
      yield m
   finally:
      m.close()

from abc import ABC,abstractmethod

class C(ABC):
   @abstractmethod
   def home(self):
      pass

   @abstractmethod
   def house(self):
      pass

class B(C):
   def play(self):
      print("hello")
   def home(self):
      print("home")
   def house(self):
      print("house")
   

if __name__=="__main__":
   with A("home.txt") as a:
       a.write("Hello world\n")
       a.write("Hello India\n")
       a.write("Hello USA\n")
   with test("hello24.txt") as t:
       t.write("hello 100\n")
       t.write("hello 200\n")
       t.write("hello 300\n")
   try:
     b=B()
     b.play()
   except Exception as e:
     print("Not implemented error")
     print(e)

