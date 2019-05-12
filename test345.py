class Supermeta(type):
  def __call__(metaname,clsname,baseclass,attrs):
      print("Super meta executed")
      clsa=type.__new__(metaname,clsname,baseclass,attrs)
      type.__init__(clsa,clsname,baseclass,attrs)
      return clsa

class Mymeta(type,metaclass=Supermeta):
  def __call__(cls,*args,**kwargs):
     print("My meta executed")
     ob=object.__new__(cls,*args)
     ob.__init__(*args)
     return ob
print("Created all class")
class Kls(metaclass=Mymeta):
   def __init__(self,data):
     self.data=data
   def printd(self):
      print(self.data)

print('Class Created')
ik=Kls('arun')
ik.printd()
ik2=Kls('aaa')
ik2.printd()
