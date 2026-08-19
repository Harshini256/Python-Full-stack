Input formatting:

#-->Integer:--> syntax - (int(input))

num = (int(input('Enter a number:')))
print(num)
print(num + 20)

#float:--> syntax - (float(input()))

marks = (float(input('Enter a decimal: ')))
print(marks + 5)

#string --> syntax - (str(input()))

name = (str(input('Enter your name: ')))
print('hello',name)


#list -->1 2 3 --> [1,2,3]

x = list(map(int, input('Enter some values: ').split()))
print(x)

#tuple --> 1 2 3 -->(22,33,44)

y = tuple(map(int, input('Enter some values: ').split()))
print(y)

#set --> 1 2 3 -->{22,33,44}

y = set(map(int, input('Enter some values: ').split()))
print(y)

# eval: it is a keyword way of following rules

data_ = eval(input('enter: '))
print(type(data_))
print(id(data_))

#output formatting:

#string output formatting 
name = 'Harshini'
age = 21
print('hello I am',name,'age is',age)
print('hello',name)

#f-string
name = 'Harshini'
age = 21
print(f'My name is {name} and my age is {age} years old')
'''
# modulus (%)

name = 'Harshini'
age = 21
print('My name is %s and my age is %d years old' %(name,age))




 

