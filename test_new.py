class A:
  def __init__(self,a,b):
     self.a=a
     self.b=b
  def __call__(self,f,*args):
    def fun(*args):
       print("Executing function")
       f(*args)
       print("Function Executed")
    return fun

@A(2,3)
def display(Something):
  print("{} will display".format(Something))

if __name__=="__main__":
   display("Hello something")