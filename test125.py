class Mymeta(type):
   def __call__(cls,*args):
       print("Call method executed")
       instance=object.__new__(cls)
       instance.__init__(*args)
       return instance

class Kls(metaclass=Mymeta):
     def __init__(self,data):
        print("Init method executed")
        self.data=data
     def printd(self):
        print("Member method executed")
        print(self.data)

ik=Kls('arun')
ik.printd()







