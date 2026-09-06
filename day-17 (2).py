'''
--- SCOPE OF VARIABLES ---
1.Scope of variables:


They are 2 types of variables:
1.Local variable:
    A variable is defined inside of a function can call it as local variable,where the variable can only access within that function.

example:

def display():
    name = 'harshini'
    print(name)
display()


2.Global variable:
   A variable that is defined outside the function call and it can be access anywhere through out program.
   
example:

a = 142
def display():
    print(a)
display()
print(a)





3.Global keyword:
     Global keyword is used to reaccess new values to variable that was already define outside the function call.
  
example:

a = 50
print(a)
def display():
     global a
     a  = 10
display()
print(a)


---- RECURSIVE FUNCTION -----

recursive finction:
   The function call itself until the base condition met ....

example:

def Fac(a):
    if a == 0 or a == 1:
        return a
    return a * Fac(a-1)
print(Fac(2 ))



'''

#local variables:

def display():
    name = 'harshini'
    print(name)
display()


#global variables:
  

a = 142
def display():
    print(a)
display()
print(a)


#global keyword:

a = 50
print(a)
def display():
     global a
     a  = 10
display()
print(a)


#====== PASS BY VALUE =====



def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(100)

# ==== PASS BY REFERENCE =====

num = 87
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(num)



# === RECURSIVE FUNCTION ====

def Fac(a):
    if a == 0 or a == 1:
        return a
    return a * Fac(a-1)
print(Fac(2 ))








    

