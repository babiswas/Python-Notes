def decorator(*params,**kwargs):
   def wrapper(*args):
       print(params[0])
       print(params[1])
       return args[0]
   return wrapper


@decorator("Execute1","Execute2","Execute3")
def fun(*args):
  print("fun executed {}".format(args[0]))
  print("fun executed {}".format(args[1]))
  print("fun executed {}".format(args[2]))
  
if __name__=="__main__":
  fun(1,2,3)