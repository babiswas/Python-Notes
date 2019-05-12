class B:
  def __init__(self,b):
     self.c=b
  def cube(self):
     print("cube method of the B class executed")
     return self.b*3

class Mymeta(type):
   def __new__(metaclass,classname,baseclass,attrs):
      print("New method of metaclass executed")
      attrs['get_cube']=B.__dict__['cube']
      return type.__new__(metaclass,classname,baseclass,attrs)
   def __init__(self,classname,baseclass,attrs):
      print("Init method of the metaclass executed")
      pass

class A(metaclass=Mymeta):
   def __init__(self,a,b):
      self.a=a
      self.b=b

a=A(2,"Hello")
print(a.get_cube())




  

