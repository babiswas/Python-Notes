class A(Exception):
   def __init__(self,name):
     self.name=name
   def __str__(self):
     return '{}'.format(self.name)

if __name__=="__main__":
   try:
        print("Inside try block")
        raise A("Exception Occured")
   except  A as b:
        print("Inside Exception block")
        print(b)
        print("Finished printing Exception")
