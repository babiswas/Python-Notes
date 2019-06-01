def decorator(*args,**kwargs):
    print("Inside decorator")
    def inner(func):
        print(kwargs['like'])
        return func
    return inner

@decorator(like="hello")
def func():
   print("Inside func")


def decorate(*args,**kwargs):
   def wrapper(*params):
      print(kwargs['test'])
      params[0]
      return
   return wrapper

@decorate(test="hello test")
def fun():
   print("hello test hi")

if __name__=="__main__":
   func()
   fun()
