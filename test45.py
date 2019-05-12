def even_integer_function(l):
   for i in l:
      if i%2==0:
        yield i

l=[1,2,3,4,5,6,7,8,9,10]

m=even_integer_function(l)
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())

   