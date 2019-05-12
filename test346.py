class A:
  def __init__(self,a,b):
     self.a=a
     self.b=b
  def __call__(self,a,b):
     self.a=a
     self.b=self.a+b

class B:
  def __init__(self,a):
    self.a=a

if __name__=="__main__":
    num=5
    if callable(num):
       print("num is callable")
    else:
       print("num is not callable")
    num=A
    if callable(num):
       print("num is callable now")
    else:
       print("num is not callable")
    num=B(2)
    if callable(num):
       print("num is again callable")
    else:
       print("num is not callable again")
    