'''
Dictionary:
  It is a collection of key :value pair it is must be unique
  Key must be unique and it should be immutable data type
  (int , str, tuple)
  Dictionary is represented in curly braces " { } ".

example:

details = {1:2,
           'name':'Harshini',
           (1,2):[1,2]}
print(details)


Accessing:

  Dictionary  can access by calling key,we will get value from that key.

Syntax:
   dict['key']

example:


data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}

print(data_['Adr'])


get()method:

  get() method is also used to get the value from that key.

syntax:
  dict.get(key)


example:

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R',
          2:[3,4]}

print(data_.get(2))


Update():
  This method is used to update a key,incase if the key is not present inside dict then it add that "key:value"

syntax:
 dict.update({key:value})

example:

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
print(data_)
data_.update({'name':'santosh'})
data_.update({'profession':'software engineer'})
print(data_)



-->There is another way to update a key

syntax:
 dict[key] = value

example:

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
print(data_)
data_['ATM PIN'] = 1980
print(data_)


values():
  values method is used to get all the values from the dict.

syntax:
  print(dict.values())

example:

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
print(data_.values())

keys():
  keys method is used to det all the keys from the dict.

syntax:
 print(dict.keys())

example:

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
print(data_.keys())


items():
  This method will get the entire key value pair separately from the dict.

syntax:
  print(dict.items())

example:

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
print(data_.items())

clear():
  This method is used to clear or delete all the key value pairs in the dictinary.

syntax:
  print(dict.clear())

example:

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}

print(data_.clear()

delete():
  delete() is used to delete a particular key value from the dictionary.

syntax:
  del dict[key]

example:

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
del data_['Adr']
print(data_)


--- CONDITIONAL STATEMENTS ---

1.IF statement:
   "IF" is a condition,if the condition becomes true,then it will execute inside block of code.
-->Incase,it becomes false,then it will never enter inside to the block of code.

example:

age = 16
if age>=18:
   print("Eligible to vote")

age = 19
if age>=18:
   print("Eligible to vote")
print(age)


a = 90
b = 20

if a>=b:
    print(a)

2.else statement:
   else for 'if' statement is a fall-back statement,incase 'if' codition is false then else block will execute.

example:

a = 90
b = 20

if a<b:
    print(a)
else:
    print(b)




'''
  





#dictionary

details = {1:2,
           'name':'Harshini',
           (1,2):[1,2]}
print(details)

#accessing

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}

print(data_['Adr'])

#get() method

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R',
          2:[3,4]}

print(data_.get(2))

#update 2nd method with direct key values:

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
print(data_)
data_['name'] = 'san'
print(data_)


data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
print(data_)
data_['AC'] = 1986660081
print(data_)


#update:

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
print(data_)
data_.update({'name':'santosh'})
data_.update({'profession':'software engineer'})
print(data_)

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
print(data_)
data_['ATM PIN'] = 1980
print(data_)

#values()method


data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
print(data_.values())

#keys() method

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
print(data_.keys())

#items():

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
print(data_.items())

#del():

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
del data_['Adr']
print(data_)

data_ = {'name':'Harshini',
         'balance':10000,
         'Adr':156748901345,
         'pancard':'GDUPX690R'}
print(data_.clear())


#if condition

age = 16
if age>=18:
   print("Eligible to vote")
print(age)


age = 19
if age>=18:
   print("Eligible to vote")
print(age)


a = 90
b = 20

if a>=b:
    print(a)

#if - else condition

age = 16
if age>=18:
   print(f'your {age} Eligible to vote')
else:
    print(f'your {age} not Eligible to vote')


a = 90
b = 20

if a<b:
    print(a)
else:
    print(b)












