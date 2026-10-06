'''
scope of variables --> scope is basically the region or area where the data is accessible.

local scope,Global Scope,Global Keyword,Enclosing scope(non  local keyword)

Built-in Scope



#local scope(local variables) --> Variable(s) defined inside the function are accessible only.

def data():
    """Local scope"""
    name='codegnan'
    return f'{name} is in vizag.'
print(data())
    



#GLOBAL VARIABLES: --> variables defined outside the function can be accessible inside the function also.

count=10
def details():
    """Global scope"""
    print(f'value of count is {count} inside  the function')
    #count = count+5 (raises unboundlocalERROR)
details()
print(f'value of count is {count} outside  the function')


#count as a updated one
count=10
def details():
    """priority of local vs global"""
    count = 15
    print(f'value of count is {count} inside  the function')
    count = count+5 
details()
print(f'value of count is {count} outside  the function')


#usage of global  keyword:

count=10
def details():
    """Usage of global keyword"""
    global count
    count = count+20
    print(f'value of count is {count} inside  the function') 
details()
print(f'value of count is {count} outside  the function')


#Enclosing scope -->Nested Functions

def outer():
    """nested functions"""
    count = 5
    def inner():
        """Inner function to use count variable"""
        #print(count)
        nonlocal count
        count = count*4
        print(f'value of count is {count}')
    inner()
    print(f'value of count is {count} outside')
outer()

#print(f'value of count is {count} outside  the function') ---> this is cannot be accessible by global bcoz it cannot define a count outside of the count.

#Built-in Scope --> Usage of built-in functions as variables

len = 12
print(len)
print(len*2)

#a = ['codegnan','python','java']
#print(len(a)) ---> this line raises an error because we can already define the len() function with a integer


#LEBG rule --> local,Enclosing,Built-in,Global

#Built-in-funtions,Anonymous Functions,recursive functions


#print(dir())
#print(dir(__builtins__))  # --> it returns the  list of all built-ins

#Every built-in datatype is a built-in-function -->(int,float,str,list,tuples,set,dic,bool)

print(bool('codegnan'))  #returns boolean value (true)


print(float(int(bool(24)))) #functions as first class objects

print(abs(-23))

#use of all() and any():

x = [1,2,'poll']
print(all(x))
x.append(None)
print(x)
print(all(x)) #all (iterable) it needs all values in the iterable to be exist.

print(any(x)) #it needs as any one of the value to be present

'''

print(bin(12)) #bin() returns the binary value.

print(chr(67)) #returns the concerened object (char)

print(ord('A')) #returns the ASCII value for any character,symbol


#print(),type(),min(),max(),len(),input()

print(divmod(6,2)) #performs 6//2(quotient) --> 3 6%2(remainder) -->0
print(pow(4,2))
print(round(9.45))
print(round(2.456,5)) #digits to be rounded off



















