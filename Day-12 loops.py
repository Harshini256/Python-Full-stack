'''

---Loops---

-----for loop statement: ------

   for loop is used to iterate over a sequence or iterable data types.
   i,j,or any num  that we are defined a variable at run time to share values from iterable data type

example:

nums = [12,31,4,5]

for num in nums:
    print(num)

else in for loop:
  unlike if-else, else block in first statement is executed after completed of all iterations.

example:

nums = 'python'

for num in nums:
    print(num)
else:
    print('for ended')


--UDE OF 'break','continue','pass' STATEMENT IN 'for loop' ---

break:

 The break is used to stop the iteration based on the condition.

example:

nums = [1,2,3,5,55,8,9]
for num in nums:
    print(num)
    if num == 3:
        break


continue:

  The continue is a key-word used to skip the current iteration based on the condition.

example:

nums = [1,2,3,5,55,8,9]
for num in nums:
   
    if num == 55:
        continue
    print(num)
  
pass:
  
   A pass is called as a 'Space-Holder that is used after statements like if,for,else not to raise any error.

example-1:

for i in range(1):
    pass

example-2:

for i in range(1,20):
    if i == 21:
        print(i)
    else:
        pass

Assert:
  assert is a keyword used to check the condition,incase the condition is false ,it will raise the error like (Assertion Error).

example:

age = 15

assert age >= 18
print('you are eligible to vote')


A = 85
assert A >= 90
print(f'{A} you are under the category of A grade')


---While Loop---




#for loop

nums = [12,31,4,5]

for num in nums:
    print(num)


for n in range(100 ,0 ,-1):
    print(n)
    
for n in range(1,100,2):
    print(n)
    print("hello")


nums = 'python'

for num in nums:
    print(num)
else:
    print('for ended')



nums = [1,2,3,5,55,8,9]
for num in nums:
    print(num)
    if num == 3:
        break



val_ = [1,3,8,9,5]
for i in val_:
    if i % 2 == 0:
        print(f'{i} is a even number')
    else:
        print(f'{i} is a odd number')



nums = [1,2,3,5,55,8,9]
for num in nums:
   
    if num == 55:
        continue
    print(num)




for i in range(1):
    pass

for i in range(1,20):
    if i == 21:
        print(i)
    else:
        pass



age = 15

assert age >= 18
print('you are eligible to vote')


A = 85
assert A >= 90
print(f'{A} you are under the category of A grade')


num = 1
while num <5:
    print(num)
    num += 1
'''

x = int(input('Enter a Number: '))
count = 0
for i in range(x):
    if x % i == 0:
        print(f'{x} is a prime number')
    else:
        print(f'{x} is not a prime number')




