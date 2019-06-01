def test(*args):
   print(args)

def testq(**kwargs):
   print(kwargs)

if __name__=="__main__":
  test(1,2,3)
  testq(a=12,b=13,c=14)
  test(*(1,2,3))
  testq(**{'a':2,'b':3})



