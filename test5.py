class MyError(Exception):
    def __init__(self,value):
       self.value=value
    def __str__(self):
       return str(self.value)


if __name__=="__main__":
   try:
      raise MyError(2)
   except MyError as e:
      print("Exception occured")
      print(e)