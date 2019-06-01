from functools import wraps

def decorator(func):
   @wraps(func)
   def wrapper(*args):
       print("Wrapper executed")
       print("first argument {}".format(args[0]))
       func(*args)
       print("Second argument {}".format(args[1]))
       return
   return wrapper

def function(*args):
   print("Argument {} executed".format(args[0]))
   print("Argument {} executed".format(args[1]))

fun=decorator(function)

if __name__=="__main__":
  fun(1,2,3)
  function(4,5)