def decorator(*params,**kwargs):
   def wrapper(*args):
       print(params[0])
       print(params[1])
       args[0]()
       print(params[2])
       return 
   return wrapper


@decorator("Execute1","Execute2","Execute3")
def fun():
  print("fun executed")
  
if __name__=="__main__":
  fun()
