import time

class A:
  def __init__(self,name):
    self.name=name
  def method(self):
     print('{} is avialble now'.format(self.name))
class Producer:
   def __init__(self):
     self.isavailable="No"
     self.prod=None
   def produce(self):
     if self.isavailable=="yes":
       time.sleep(2)
       self.prod=A("Hello")
       self.prod.method()
     else:
       time.sleep(3)
       print("A is not available")


a=Producer()
a.produce()
a.isavailable="yes"
a.produce()
     
