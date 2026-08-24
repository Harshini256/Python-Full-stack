'''
-->1.Tuple:
      Tuple is a collection of different data types that seperated by commas(,) and represented by"()".
      It is Mutable data type.
      we can pass a tuple of values and that can be assign to the variables,but it should match same no. of variables and values inside the tuple.
      
    Syntax: print(variable_name())
    
example of tuple:

name, age, batch = ('harshini',21,6)
print(name)
print(age)
print(batch)

    
-->Functionalities of Tuple:
    
-->1.indexing:
example:

t = (1,'python',[3,4],(7,9))
print(t[2][1])

-->2.Index():
    If a item is not present in the tuple,it will raise value error.
  syntax:
example:
t = (1,'python',[3,4],(7,9))
print(t.index('python'))

-->3.len():

example:
t = (1,'python',[3,4],(7,9))
print(len(t))

-->4.max():
   It is used to find out the max value from the tuple.
  syntax: print(max(variable_name)

example:

so = (22,3,45,82,93)
print(max(so))


-->5.min():
  It is used to find out the least value from the tuple.
 syntax: print(min(variable_name)

example:

so = (22,3,45,82,93)
print(min(so))

-->6.count():
   count() is used to count an item present in the tuple,which is repeated n no.of times.

example:

so =(9,9,2,3,4,5,9)
print(so.count(9)

-->7.concatination:

x = (1,2,3,4)
y = (6,7,8)

result = (x + y)
print(result)






  




'''

t = (1,'python',[3,4],(7,9))
print(t[2][1])

t = (1,'python',[3,4],(7,9))
print(t.index('python'))

t = (1,'python',[3,4],(7,9))
print(len(t))


name, age, batch = ('harshini',21,6)
print(name)
print(age)
print(batch)


so = (22,3,45,82,93)
print(max(so))

so = (22,3,45,82,93)
print(min(so))


so =(9,9,2,3,4,5,9)
print(so.count(9))


x = (1,2,3,4)
y = (6,7,8)

result = (x + y)
print(result)

