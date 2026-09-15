'''
Input formatting : accept input from user.
input function can be any integer,float,string,coma seperated values,space seperated values.


#input from user -->input() -- it can accept any type -->but result will be stored in the string type

name = input('enter the name: ')
print(name)
print(type(name))
print(len(name))

#split() -->split function of space-seperated values.

names = input('enter the names: ').split()
print(names)
print(type(names))
print(len(names))



#split(',') split function of ',' seperated values

names = input('enter the names: ').split(',')
print(names)
print(type(names))
print(len(names))


#accept single integer,multiple integer values,group of integers.

num1 = int(input('enter the no. : '))
print(type(num1))
print(num1)

#every built-in data type is a built in function --> "functions" can also called as "objects"

#usage of map()function -->for the group of integers.

numbers = list(map(int, input('enter the values: ').split(',')))
print(numbers)
print(type(numbers))

#group of float values
temperatures = list(map(float, input('enter the values: ').split(',')))
print(temperatures)
print(type(temperatures))

#accept multiple values -->integers.

temperature,pressure = map(float, input('enter the values: ').split(','))
print('Temperature is',temperature)
print('pressure is',pressure)
'''
#file-handling:

text = input('enter the secret note: ')
with open('secret.txt','w')as file:
    file.write(text)
with open('secret.txt') as new_file:
    print(new_file.read())


