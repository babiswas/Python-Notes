def metafunc(name,bases,attrs):
  nattrs={'mod'+key:attrs[key] for key in attrs}
  return type(name,bases,nattrs)

MyMeta=metafunc

class Kls(metaclass=MyMeta):
   def setd(self,dat
a):
      self.data=data
   def getd(self):
      return self.data

k=Kls()
k.modsetd('Hello')
print(k.modgetd())
