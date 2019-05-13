class A:
  def __new__(cls,*args,**kwargs):
     print("new method called")
     l=super().__new__(cls)
     return l
  def __init__(self,a,b,**kwargs):
     print("init method called")
     for i in kwargs:
      print(kwargs[i])
     self.a=a
     self.b=b


if __name__=="__main__":
   a=A(1,2,**{'e':12,'f':13,'c':14})
   print(a.__dict__)
   setattr(a,"name","Bapan")
   setattr(a,"num",12)
   print(a.__dict__)

     