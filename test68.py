def fun():
  print("Hello")

class A:
  pass




if __name__=="__main__":
   print(fun.__name__)
   dir(fun)
   a=A()
   a.b=2
   print(a.__dict__)
   dir(a)
   print(a.__dict__)
   setattr(a,'k',3)
   print(a.__dict__)
   setattr(a,'m',{'test':1,'id':2})
   print(a.__dict__)

   