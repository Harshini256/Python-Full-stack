Concatination:
The "+" symbol will behave in 2 ways for numerics and strings
 For Numerics it works normally.
And for various other data types like "string,list,tuple" it will concatenate.

Operators:
To perform some mathematical operations.
the operators are used to perform operations in variables and the values.
1.Arithmetic operators:
 This operators are used to perform mathematical operations.
 +,-,*,/,//,% ..
ex -1
num = 90
num_1 = 52
print(num + num_1)
ex-2:
an = 'python'
of = 'language
print(an + of)

Subtraction(-):
a = 20
b = 5
print(a - b)

Multiplication(*):
v = 5
c = 5
print(v * c)

division(/):

x = 8
y = 4
print(8 / 4)

float division(//):
x = 8.6
a = 2.3
print(x // a)
modulus(%):
d = 4
e = 8
print(4 % 8)

2.Assignment Operators:
= , += , -= , /= , %= , /= ..
--> += --> Increment operator:
    a = 0
    print(a)
    a += 1
    print(a)
---> -= -->Decrement operator:
example:
b = 67
b -= 5
print(b)

c = 7
c *= 2
print(c)


d = 8
d /= 3
print(d)

e = 42
e //= 11
print(e)

f = 2
f %= 1
print(f)
3.Comparision operators:
== , >= ,<= ,> ,< , !=  --> this are the comparision operators.
examples:
num = 10
num_1 = 5
print(num == num_1)  #10 == 5
print(num != num_1)  #10 != 5
print(num > num_1)   #10 > 5
print(num < num_1)   #10 < 5
print(num >= num_1)
print(num <= num_1)

num_2 = 10
num_3 = 9
print(num_2 >= num_3)
print(num_2 <= num_3)


4.Logical operators:
 (and ,or ,not)---> logical operators
num = 9
num_2 = 20
print(num >= num_2 and num <= 11)
print(num <= num_2 and num >= 11)

print(num >= num_2 or  num < 11)
print(not(num >= num_2 or  num < 11))


5.Identity operators:
(is, is not) --> this are the identity operators.
a = [1,2]
b = [1,2]
print(a is b)
print(a == b)

print(id(a))
print(id(b))
print(a is not b)


6.Membership operators:
Menbership is nothing but checking whether the printed string is present in the given string in it.
example-1:
num = 'python is a language'
print('y' in num)
print('l' not in num)

#example2:
num = 1,2,3,4,5
print(7 in num)
7.Bitwise operators.