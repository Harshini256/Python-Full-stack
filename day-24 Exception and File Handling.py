'''
=== FILE AND EXCEPTION HANDLINGS ===

--- EXCEPTION HANDLING: ---

 -- EXCEPTION HANDLING IS USED TO RECTIFY THE ERRORS.
 -- exception handling is way of handling the errors.
 -- we can write n no.of exceptions for one code written at try block.

  
They are 4 components:

-- try:
     The 'try' block where we can write a code which may contain errors.
    syntax:
    try:
        code lines.
-- except:
     This will handle errors that are raised at 'try' block.
    syntax:
    except ErrorName:
        print('ErrorName')
example:
        
try:
    print(num)
    print(5/0)
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')

        
-- else:
     The else block will only execute,if no error at try block.
example:

try:
    print('num')
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
else:
    print('No Error')
    

       
-- finally:
     This block will execute regardless with the errors at try block.
example:

try:
    print(num)
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
else:
    print('No Error')
finally:
    print('End')


---- FILE HANDLING ---

File Handling:
    the file handler is an object,which is used to create,update,read and delete...

Modes of file handling:

--> r: This r mode is used to read() function is used ( r is mode, read() is a function)

--> w: This  r mode is used to write("") function and change alraedy written text and enter a new text which we written in write() function.

-->a : this a mode is used to append again same text which we written in the write function it can append at the last.

    
'''

#try
try:
    print(6/0)
except ZeroDivisionError:
    print('Not divisible by zero')


#except
try:
    print(num)
    print(5/0)
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')

#else:

try:
    print('num')
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
else:
    print('No Error')


try:
    print(num)
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
else:
    print('No Error')
finally:
    print('End')

# -- file handling:

with open('demo.txt','r')as file:
    print(file.read())

with open('demo.txt','w')as file:
    file.write('This is harshini,want to become a software developer')

with open('demo.txt','a')as file:
    file.write('This is harshini,want to become a software developer')








    
    

    
    
