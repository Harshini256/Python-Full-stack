'''
Nested loops ---> Pattern problems -->square,rectangle,number grid number

'''
#Right angle triangle:

for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()

#Inverted Triangle

for i in range(5):
    for j in range(5-i):
        print('*',end=' ')
    print()
#Star Pyramid Triangle:
    
rows = 5
for i in range(1,rows+1):
    for j in range(rows-i):
        print(' ',end='')
    for j in range(i):
        print('*',end=' ')
    print()

for i in range(5):
    for j in range(i+1):
        print(j,end=' ')
    print()


n = 1
for i in range(4):
    for j in range(i+1):
        print(n,end=" ")
        n+=1
    print()


cap = 65
for i in range(4):
    for j in range(i+1):
        print(chr(cap),end=" ")
        cap+=1
    print()
'''
star = 5
count = 0
for i in range(1,star+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''


#diamond pattern printing: --->task


#datatypes,operators,control block,exception handling,file handling

#procedure oriented programming -> functions -->A function is a block of code that performs a specific task,we have keyword "def" :

'''
syntax: of Function:

def fname(parameters):
    """Doc String(describe your function)"""
    statements(s)...
    .....
    ...
    return value(s)....
fname(args) #function call

'''

def intro():
    """Intro to Functions"""
    return "hope you are learning and enjoying the journey"               #one return function can take any no. of values
print(intro())


#POSITIONAL ARGUMENTS,KEYWORD ARGUMENTS,DEFAULT ARGUMENTS,VARIABLE ARGUMENTS,KEYWORD VARIABLE LENGTH ARGUMENTS.


def add(a,b):
    """simple addition function"""
    return a+b
print(add(5,7)) #addition
print(add('codegnan','python')) #concatenation.
print(add([1,2,3,4],[9,90,86])) #merging

c,d = map(int, input("enter the values").split(','))
print(add(c,d))


#print(add(9,8,6,3))



#Grocery store code using functions:

def grocery(item,price):
    """Keyword arguments usage"""
    print(f'Item is:{item}')
    print(f'Price is:{price}')
grocery('milk',35)
print(grocery(price=45,item="bread")) #it also returns none as nothing to be printed

#grocery('jam',6,6) --> in this case the positional arguments fails as we have 2 aruguments.


#default 2 arguments in dunction definition


def grocery(item='drink',price=60):
    """Keyword arguments usage"""
    print(f'Item is:{item}')
    print(f'Price is:{price}')
grocery('milk',35)
grocery('bread',40)
grocery()












    

