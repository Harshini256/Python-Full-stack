'''
variable length arguments(*args),key-variable length arguments( **kwargs)


Variable-Length aruguments:
    We can pass any number of arguments but the data will be stored in a ______,but we use symbolically *args as representation.
'''
def new(*harshini):
    """usage of variable length arguments"""
    print(harshini)
    print(type(harshini))
new()   #it returns a empty tuple as we didnot pass any args
new(1,2,3)
new(1,2)
new("harshini","santosh","sneha","baaghi")


details=[1234,'data','webinar','hackathon']
new(details)   #In this case entire list is stored insisde a tuple as a sinle object.
new(*details)   #In this case we can extract the values from the above list as a tuple


a,b,c = 1,3,4
a,*b,c= 1,'harshini','sakshi','indhu',121
print(a)
print(b)
print(c)


# '*' is mainly used to unpack the values from a collection.

a = ['codegnan','python','data',45,6.7]
print(*a)

for i in a:
    print(i,end=' ')

#In above case both "for loop and line 33 result is same.



#Task: Find the sum of arguments in a function

def add(*a):
    """sum of arguments using *args"""
    print(a)
    print(type(a))
    #we need to have output variable
    result = 0

        
    for i in a:
        #if type(i) == int or type(i)== float:
         if type(i) in (int,float):
             
                result=result+i
                print(result)
    return result
        
print(add())
print(add(1,3,4))
print(add(12,3,4,'codegnan','saketh',2.3))


#keyword variable length arguments --> we can pass any no. of keyword arguments,we will use the representation as **kwargs,data is stored in dictionary ..


def admission(**a):
    """usage of keyword variable length arguments"""
    print(a)
    print(type(a))
admission()
admission(name='Harshini',mobile=6301644154,email_id='golusu@hmail.com')

details ={'idnos':[234,134,154],
          'names':['harshini','baaghi','sneha'],
          'batches':['PFS','DA','JFS']
          }
admission(**details)


#Usage of both *args band **kwargs into a function:

def simple(*a,**b):
    """Usage of *args and **kwargs"""
    print(a)
    print(b)
    result=0
    for i in a:
        #if type(i) == int or type(i) == float:
        if type(i) in (int,float):
            result = result + i
    print(result)
    for key,value in b.items():
        print(f'key is{key}')
        print(f'value is{value}')
simple()
simple(1,2,4,'poll',22,name='codegnan',place='vizag')
#simple(23,4,batch='pfs6',data='python',3.5) ---> it can raise an error because of suntax followed by the function  #positional arguments always follow keyword arguments.





      










