Datatypes & TypeConversions:
.Data:Anything that we should giving information is called as Data.
Data type: The kind of data that we are holding is called a data type.

The different types of data are of:
1.Numeric Datatype
 ->float and integers is called as numeric data type.
 float:
  A number which contains decimal values ,we call it as a float datatype.
eg:56.89
code:
price = 56.89
print(type(price))
 Integer(int)
  A normal number without any decimal values.
eg: 89
code:
num  = 89
num_1 = 21
2.String:
  String which is nothing but a "Sequence of Characters".
---> How the sequence of characters will come?
  example 1:
	any_ = 1,2,3,4,5
	for i in range(6):
	    print(j)
example 2:
any_ = 'python is a interpreted language'
for i in any_:
    print(i )  		#This are sample examples of sequence of characters.

String Definition:
If we consider anything inbetween the single(' '),double(" "),triple(''' ''') that we should consider it as a string.
String is a sequence of characters that are enclosed in ' '," ",''' ''' .
String is a Immutable.
 eg:
 any_ = 'Python is a scripting language to understand easily'
 all_ = 'Ab,.&[)-+'

3.List:
  List is a collection of different data types.
  It is represented by "[]" that are separated by (,)then inside it we call it as items .
  Inside the list we call it as items.
  List is Mutable (# mutable means we can modify the list)

 example:1
any_ = [1,2,'python',(2,1)]
print(type(any_))
4.Tuple:
Tuple is a collection of different data types that are enclosed in "()" and those 	are     separated by commas(,).
Tuple is Immutable. [:Immutable means cannot be modified]
example1:
data_ = [1,2,3]
all_ = (1,2,3)
print(type(data_))
print(type(all_))
example2:
all_ = 'python is a programming language'

print(all_.replace('python', 'java'))
print(all_)                               							 #once the items in the tuple can be printed it cannot be changed or modified.
         #To replace the data in the tuple we can use "replace" function in it that can be 	added to another  but the existing one which have printed cannot be modified and a 	new string is printed if use replace function.
example:3
nums = (1,89.67,'python',[3,4],(8,9))
print(nums)

5.Dictionary:
-It is a Collection of key:value pairs
-Keys and values are separated by(:).
-we can call "Key:value pair" as a 'item'.
-This items are separated by comma(,) again.
-Dictionary is represented using"{}".
-In keys place we can use immutable data type.
-In values place we can use any data type.
example1:
nums = {'name':'harshini',
        'age':21}
print(nums)
print(type(nums))

example2:
data_ = {1:2,
	 'name':'harshini',
	 (2,3):'tuple'}
print(data_)
print(type(data_))

6.Set:
-Sets is a collection of unique elements.
-Set can't allow any duplicate values inside it.
-Set is represented by "{}'curly braces,and the elements are separated by commas(,).
example:
an = {1,2,4,4,5,3}
print(an)

Type Conversions:

1.float ----> int,str
eg:
price = 45.67
print(int(price))

price = 45.67
con = str(price)
print(type(con))

2.integer ---> float(),string
example:
num = 78
con_ = str(num)
print(type(con_))

3.string ---> int,float.
example:int()

do = '6788'
print(int(do))

--->float()
do_ = 98.6
print(float(do_))

4.list ---> tuple,string.
eg: -->tuple()
nums=[1,2,3,4]
print(tuple(nums))

5.tuple --->list
eg:list()
all_ = {5,6,7}
print(tuple(all_))

details = [('name', 'harshini'),('edu', 'B.tech')]
print(dict(details))



