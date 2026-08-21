'''
List: --
 -->Collection of different data types that separated by commas(,) and it is represented by []
 [].
 Functionalities of List:

 1.Indexing:
 they are
 1.-->Posiive indexing.
  --Positive indexing starts from 0
 2.-->Negative indexing.
 --Negative indexing starts from -1.
 example:
 so = [1,2,3,'python']
 print(so.index[0])
 print(so[3][1])

 example 2

 all_ = [12,[1,'python',[1,4],(78,[6,7])],['java',24]]
 print(all_[1][3][1])
 print(all_[0])
 print(all_[1])
 print(all_[1][0])
 print(all_[1][2])
 print(all_[2])
 print(all_[2][1])

example-3:

 data_ = ['python',[1,2,(90,'Details',[67,0]),(78,'Student')]]
 print(data_)
 print(data_[0])
 print(data_[1])
 print(data_[1][2])
 print(data_[1][2][1][2])

2.-->len():
  This function is used to find the no.of items present in the list.
  -->Syntax:-- print(len(variable_name))
  
example:

 data_ = ['python',[1,2,(90,'Details',[67,0]),(78,'Student')]]
 print(len(data_))
 print(len(data_[1]))
 print(len(data_[1][2]))

3.Sclicing:

 nums = [1,2,3,4,5,6,78,9,0]
 print(nums_[0:7])

 num = [1,2,3,4,5,6,78,9,0]
 print(num[0:6])

 a = [1,2,3]
 b = [4,5,6]

 result = a + b
 print(result)

4.Methods:

They are some methods:

-->1.append():
      append()method will add new items into the list at last index position.
    syntax: print(variable_name.append(item))

 example:
 
 x = [1,2,3]
 print(x)
 x.append('harshini')
 print(x)
 x.append([5,6])
 print(x)

-->2.extend():
      extend() method will add the items into a list at last position,but it will give each
      value as one index inside.
     syntax: print(variable_name.extend(items)).

example:

 y = [1,2,3]
 y.extend([4,5])
 print(y)
 y.append('python')
 print(y)
 y.extend('python')
 print(y)

-->3.pop():
      pop() is used to remove an item from the list and it will delete based on the index position value.
     syntax:print(variable_name.pop(index_position))

example:

n = [1,2,3,4,5]
n.pop(4)
print(n)

example-2

n = [1,2,3,4,5,'harshini']
n.pop()
print(n)

-->4.remove():
      remove() will  delete the items based on value given in it.
     syntax: print(variable_name.remove(value))

example:

l = [1,2,3,4,5,'harshini']
l.remove(4)
print(l)

 '''
#list indexing examples:

so = [1,2,3,'python']
print(so[0])       #postive indexig of list
print(so[3][-1])   #negative indexing

all_ = [12,[1,'python',[1,4],(78,[6,7])],['java',24]]
print(all_[1][3][1])
print(all_[0])
print(all_[1])
print(all_[1][0])
print(all_[1][2])
print(all_[2])
print(all_[2][1])

data_ = ['python',[1,2,(90,'Details',[67,0]),(78,'Student')]]
print(data_)
print(data_[0])
print(data_[1])
print(data_[1][2])
print(data_[1][2][1][2])

#len():

data_ = ['python',[1,2,(90,'Details',[67,0]),(78,'Student')]]
print(len(data_))
print(len(data_[1]))
print(len(data_[1][2]))

#slicing

num = [1,2,3,4,5,6,78,9,0]
print(num[0:6])

a = [1,2,3]
b = [4,5,6]

result = a + b
print(result)

#Methonds:

#1.append():

x = [1,2,3]
print(x)
x.append('harshini')
print(x)
x.append([5,6])
print(x)

#2.extend():

y = [1,2,3]
y.extend([4,5])
print(y)
y.append('python')
print(y)
y.extend('python')
print(y)

#3.pop():
# it is used to remove

n = [1,2,3,4,5,'harshini']
n.pop(4)
print(n)


n = [1,2,3,4,5,'harshini']
n.pop()
print(n)

#4.remove()


l = [1,2,3,4,5,'harshini']
l.remove(4)
print(l)


