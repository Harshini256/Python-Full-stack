'''
--- CONDITIONAL STATEMENTS ---

1.if statement:
   "if" is a condition,if the condition becomes true,then it will execute inside block of code.
-->Incase,it becomes false,then it will never enter inside to the block of code.

example-1:

age = 16
if age>=18:
   print("Eligible to vote")

age = 19
if age>=18:
   print("Eligible to vote")
print(age)

example-2:

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

3.elif statement:
   elif statement is used to check more possible outcomes.
example - 1:

a = 60
b = 78
c = 27


if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


example -2:


x = 21
y = 9

user_opt = int(input('Enter \n1.add \n2.sub \n3.mul \n4.div \n5.pow: '))

if user_opt ==1:
    print(x + y)
elif user_opt ==2:
    print(x - y)
elif user_opt ==3:
    print(x * y)
elif user_opt ==4:
    print(x / y)
else user_opt ==5:
    print(x ** y)

4. nested-if:
   'if' inside a 'if' statement is called as nested if.

example:

app_details = {'pin':1980}
import random
user_pass = (int(input('Enter your app password: ')))
otp = random.randint(1000, 9999)
if user_pass == app_details['pin']:
    print('password is correct')
    print(otp)
    user_otp = (int(input('Enter 4 digit OTP: ')))

    if user_otp == otp:
        print('Welcome to the app')
    else:
        print('incorrect otp')
    
else:
    print('password id incorrect')

    


'''





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

    


#elif condition


a = 60
b = 78
c = 27


if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

    


# if-elif-else condition


x = 21
y = 9

user_opt = int(input('Enter \n1.add \n2.sub \n3.mul \n4.div \n5.pow:'))

if user_opt ==1:
    print(x + y)
elif user_opt ==2:
    print(x - y)
elif user_opt ==3:
    print(x * y)
elif user_opt ==4:
    print(x / y)
else:
    print(x ** y)
    


#nested-if:

app_details = {'pin':1980}
import random
user_pass = (int(input('Enter your app password: ')))
otp = random.randint(1000, 9999)
if user_pass == app_details['pin']:
    print('password is correct')
    print(otp)
    user_otp = (int(input('Enter 4 digit OTP: ')))

    if user_otp == otp:
        print('Welcome to the app')
    else:
        print('incorrect otp')
    
else:
    print('password id incorrect')

    

#if-else:


a = int(input('Enter a number: '))
if a % 2 == 0:
    print(f'{a} is a even number')

else:
    print(f'{a} is a odd number')

    


#if-elif-else:

marks_ = int(input("Enter your marks:"))
if marks_ >=90:
    print('A+')
elif marks_ >=80:
    print('A')
elif marks_ >=70:
    print('B+')
elif marks_ >=60:
    print('B')
elif marks_ >=50:
    print('C+')
elif marks_ >=40:
    print('C')
else:
    print('Fail')

















