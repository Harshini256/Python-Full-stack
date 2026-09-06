'''
List compression :
 List compression is the short form of syntax to create a list.

 syntax:
  1. --> [expression loop condition]
  2.   --> [expression condition else loop]

example:

old = 'python'
new = [i for i in old]
print(new)

Nested comprehension:

  using list comprehension  generating list inside list.

#matrix or nested matrix:

any_ = [[i*j for i in range(1,6)]for j in range(1,10)]
print(any_)



#nested comprehension:

of = [[1,2,3],
      [4,5,6],
      [7,8,9]]

all_ = [num for i in of for num in i]
print(all_)



Generating function:
   A generator is a special function which generates one value at a time.
example:

def all_():
    for j in range(1,10):
        yield j
j = all_()
print(next(j))


  

'''
old = (1,2,3,4,5)
new_ =  [i for i in old if i%2 == 0]
print(new_)

old = 'python'
new = [i for i in old]
print(new)


#matrix or nested matrix:

any_ = [[i*j for i in range(1,6)]for j in range(1,10)]
print(any_)



#nested comprehension:

of = [[1,2,3],
      [4,5,6],
      [7,8,9]]

all_ = [num for i in of for num in i]
print(all_)


#generating function:

def all_():
    for j in range(1,10): 
        yield j
j = all_()
print(next(j)) 



