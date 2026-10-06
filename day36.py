''''
Functions ---> User Defined functions,Built-in-Functions,Anonymous Functions(lambda keyword),Recursive function.


Anonymous functions --> nameless functions(helper functions),we define them by using lambda keyword.

syntax:
lambda arg(S):expression


#create a function to cal the area of rectangle where and breadth are 7,4


def rectangle(l,b):
    """Area of rectangle"""
    return l * b
print(rectangle(7,4))
print('Area of rectangle is' ,rectangle(7,4))



#same functio using anonymous  function

area = lambda l,b:l*b
print(area(7,4))
print(type(area))


#find the area of square with side value as 5

area = lambda side:side**2
print(area(5))


#social media user login first_name last_name -->full name

fname,lname=input('enter the names: ').split(',')

#print(fname,lname)
full_name=lambda fname,lname:fname.title().strip()+" "+lname.title().strip()
print(full_name(fname,lname))



#accepting input from user and find even or odd

n = int(input('enter a number: '))
result = lambda n:'even' if n%2==0 else 'odd'
result1 = lambda n: n**2 if n%2==0 else n**3
print(result(n))
print('new result is',result1(n))

'''
names = ['codegnan','python','saketh','data','java']
g = lambda x:x in names

h = lambda x:len(x) in names

o = lambda x:len(x)

print(g('python'))
print(h('codegnan'))
print(o('data'))


#filter(),map(),reduce()

#filter() --> we want to specific filtered result

data = [1,3,4,5,24,12,36,3]

new_data = list(filter(lambda x:x%2==0,data))
print(new_data)


#try above with a user defined function with a for loop:

data = [1,3,4,5,24,12,36,3]
def filter_data(data):
    result=[]
    for i in data:
        if i%2==0:
            result.append(i)
    return result
print(filter_data(data))


#filter desired names from the list

names = ['harshi','bhagii','snehaa','anu','reena']
new_names = list(filter(lambda i:len(i) >= 6,names))
print(new_names)


#map() -->it will apply logic for each value(google maps)

lst = list(map(int, input('enter the values: ').split(',')))
print(lst)
data = [1,3,4,5,-23]
print(data)
final = list(map(lambda x,y:x+y,lst,data))  #it automatically maps the length
print(final)


#dicount of 10% for every price in a given program

prices = [2000,1800,1600,1400,1000]
disc_prices = list(map(lambda price:(price - price*0.1),prices))
print(disc_prices)


#reduce --> functools
#reduce --> it will check for logic and make it to a single value

import functools
from functools import reduce
result = reduce(lambda x,y:x*y,[12,3,2,1])
print(result)
f = reduce(lambda x,y:x+y,[12,3,2,1])
print(f)


#task : try above two cases using functions



#Recursive Functions: A function can call itself

#This "recurive functions can be used in the programs of -->factorial,fibanocci series,sum og numbers ..."

#Recursive functions --> because(it tells when to stop the recursion)
#                     -->recursive case(it tells how to start recursion)


'''
def func():
    """docstring"""
    if base:#base case
        return
    func() #recursive case
func()

'''
#def test():
#    """testing"""
#    return test()  #we missed base case
#print(test())


#let's link above case to factorial
#5! => 5 * (5-1) *(5-2) *(5-3) *(5-4) * 1

n = int(input('enter the value: '))
def fact(n):
    """factorial"""
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "input must be greater than 1"
    else:
        return n * fact(n-1)
print(fact(n))







    
    

