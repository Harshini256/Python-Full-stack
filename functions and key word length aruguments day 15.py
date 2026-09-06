'''

Functions:
  A function is a block of code that can be executed only when its called ...
   --> A function starts with "def" keyword and the line is called as definition line,
       where we can define a function name.
   --> if we want to execute the program in the function need to call with the function name
        "define as "def" line"
syntax:
    def fun_name(parameters):
        pass
    fun_name(arguments)
    
example:
def add_(a,b):
    print(a+b)
add_(5, 6)


Arguments:

Positional arguments:
  The arguments should be same at the def line and calling,incase it they are not having
  same number an error will be raised.

Default arguments:
  The default arguments where the function will only consider the data at calling function,even though
  data presennt at the definition line.
  

example:
1.
def feb_(num,num_2):
    print(num + num_2)
feb_([1,3], [5,6])
-------
2.
def data(a=8, b=9):
    print(a+b)
data(1, 2)

exampl -3

num = int(input('enter a number: '))
count = 0
def prime(num=10, count = 1):
    for j in range(1,num+1):
        if num % j == 0:
            count += 1
            print(count)
    if count == 2:
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')

prime(num, count)

keyword arguments:
    Keyword arguments are sending arguments in a pair(a = 2),and a passing order is not consider here.
    
    
example:

def data_(age,name,batch,location):
    print(name)
data_(name='harshini',age=21,batch=6,location='vizag')


variable length argument:(*)
Adding a star ((*) --> we call the star as args) before a variable at parameters we can pass tuple of arguments and can be accessing with indexing.

example:
    
def all_(*Name):
    print(Name[2])
all_('Harshini','santosh','pinky','sai')


Key-word length arguments:(**)

def details_(**data_):
    print(data_.keys())
details_(name='harshini',age=21,batch=6,location='vizag')



return():

return keyword is used inside the function,once the return is executed means it will get back to calling with return values.
example:

def all_(a,b):
    return a-b
print(all_(7,8))








#functions:

a,b = 6,7
def add_(a,b):
    return a+b
all_ = add_(a,b)

#function=arguments:

num = 0
num_1 = 1
def feb_(num, num_1):
    print(num,num1, end=' ')
    for i in range(1,10):
        num2 = num + num_1
        num = num_1
        num_1 = num2
        print(num2, end=' ')
feb_(num, num_1)

#default arguments:

def feb_(num,num_2):
    print(num + num_2)
feb_([1,3], [5,6])


def data(a=8, b=9):
    print(a+b)
data(1, 2)

num = int(input('enter a number: '))
count = 0
def prime(num=10, count = 1):
    for j in range(1,num+1):
        if num % j == 0:
            count += 1
            print(count)
    if count == 2:
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')

prime(num, count)



#keyword arguments:
    #Keyword arguments are sending arguments in a pair(a = 2)

example:

def data_(age,name,batch,location):
    print(name)
data_(name='harshini',age=21,batch=6,location='vizag')

# * = variable length argument:
#       adding a star ((*) --> we call the star as args) before a variable at parameter we can pass tuple of arguments and can be accessing with indexing.

#example:
    
def all_(*Name):
    print(Name[2])
all_('Harshini','santosh','pinky','sai')


#Key-word length arguments:

def details_(**data_):
    print(data_.keys())
details_(name='harshini',age=21,batch=6,location='vizag')


# return(): return keyword is used inside the function,once the return is executed means it will get back to calling with return values.

def all_(a,b):
    return a-b
print(all_(7,8))

'''

def feb_(num,num_2):
    print(num + num_2)
feb_([1,3], [5,6])


def data(a=8, b=9):
    print(a+b)
data(1, 2)

num = int(input('enter a number: '))
count = 0
def prime(num=10, count = 1):
    for j in range(1,num+1):
        if num % j == 0:
            count += 1
            print(count)
    if count == 2:
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')

prime(num, count)
