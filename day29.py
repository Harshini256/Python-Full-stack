#task --> user can enter height in centimeters, feets ---> meters(calculate bmi)
#make all user validations for height --> cms,feets.
#post link in git hub.


#if the same bmi scenario we want it to be repeated for specific number of times.

# -- Repititive Statements --(for,while)
#for keyword -->

'''
for temp_vaiable in range/collection
      "statements"
    .......
    ...

for i in range(5):
    weight = int(input('enter weight in kgs'))
    height = float(input('enter the height in metres:'))
    name = input('enter the name: ')
    if weight > 0 and height > 0:
        bmi = weight / ((height)**2)
        if bmi<18.5:
            print(f'bmi of {name} is {bmi} and you are underweight')
        elif bmi>18.5 and bmi<24.9:
             print(f'bmi of {name} is {bmi} and you are Healthy --> keep consistent')
        elif bmi>=25 and bmi<=29.9:
             print(f'bmi of {name} is {bmi} and you are Overweight -->\start exercising')
        elif bmi>30:
             print(f'{name} is in obase category and bmi is {bmi}')
    else:
        print('do enter only positive values greater than 0')




#task


a = {'names':[],
     'weights':[],
     'heights':[]}
n = int(input('enter how many times you want to repeat: '))
for i in range(n):
    weight = int(input('enter weight in kgs'))
    a['weights'].append(weight)
    height = float(input('enter the height in metres:'))
    a['heights'].append(height)
    name = input('enter the name: ')
    a['names'].append(name)
    
    if weight > 0 and height > 0:
        bmi = weight / ((height)**2)
        if bmi<18.5:
            print(f'bmi of {name} is {bmi} and you are underweight')
        elif bmi>18.5 and bmi<24.9:
             print(f'bmi of {name} is {bmi} and you are Healthy --> keep consistent')
        elif bmi>=25 and bmi<=29.9:
             print(f'bmi of {name} is {bmi} and you are Overweight -->\start exercising')
        elif bmi>30:
             print(f'{name} is in obase category and bmi is {bmi}')
    else:
        print('do enter only positive values greater than 0')
print(a)


#exception handling:

#exception handling is a mechanism to a program which responds to run time errors or compilations.

#exception --> it tries to make our program in a normal flow.

# we can 3 types to control errors and continue with the work flow of a profram -->[try,except,finally]


#try,except,finally

try:
    #code that may cause an error...
    ....
except:
    #code that handles the error...
    ....
finally:
    .....
    ......


#simple scenario to understand the exception:
a,b = map(int, input('enter the values').split(','))
try:
    result = a/b
    print(result)
except Exception as e:
    print('find it')
    print(e)


# or

try:
    a,b = map(int, input('enter the values').split(','))
    result = a/b
    print(result)
except Exception as e:
    print('find it')
    print(e)


#in the above case we will get ValueError,ZeroDivisionError ...
#possible type of errors --> TypeError,ValueError,NameError .... Index Error,ZeroDivisionError,AttributeError,ArithmeticError.

try:
    a,b = map(int, input('enter the values').split(','))
    result = a/b
    print(result)
except ValueError:
    print('please enter the code correctly with only the type of integers')
except ZeroDivisionError:
    print('make sure to give denominator  greater tha 0')
except NameError:
    print('please first understand the syntax aand be good at spellings')
except AttributeError:
    print('please check the methods or function names properly')
finally:
    print('its done now you have understood exception handling')

'''

#how to write a code with multiple exceptions at a time.

try:
    a = [12,3,4,5]
    print(a[0])      #take 1 example as print(a[45])  ---------------
    a.append('codegnan')    #take 1 example as a.appen('codegan') --------    THIS MAY CAUSES VARIOUS ERRORS .
    print(a)                #take 1 example as print(v)               ------------
except(IndexError,NameError,AttributeError)as e:
    print(e)
finally:
    print('done')

#In above case all errors will never happen.




    
