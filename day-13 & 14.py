#prime series using nested-if:

limit = 100
for i in range(2,limit+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f'{i} is prime')
    else:
        print(f'{i} is not a prime')

#pattern series:
        
star = 10
for i in range(1,star+1):
    for j in range(1,i+1):
        print('*',end=" ")
    print()

star = 10
for i in range(1,star+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()



star = 10
count = 0
for i in range(1,star+1):
    for j in range(1,i+1):
        count +=1
        print(count,end=" ")
    print()
    

star = int(input('Enter a number: '))
count = 0
for i in range(1,star+1):
    for j in range(1,i+1):
        count +=1
        print(count,end=" ")
    print()


star = 5
for i in range(0,star-1):
    for j in range(0,i-1):
        print('*',end=" ")
    print()


ran = int(input('Enter a Number: '))
for i in range(1, ran+1):
    if i % 2 == 0:
        print(f'{ran} is a even number')
    else:
        print(f'{ran} is a odd number')

#odd number printing using for anf if conditions

ran = int(input('Enter a number'))
for i in range(1, ran+1):
    if i % 2 != 0:
        print(f'{i} is a odd number')


#printing even or odd using for loop and if-else condition:
        
nums = [23,78,97,5]
for i in nums:
    if i % 2 == 0:
        print(f'{i} is a even number')
    else:
        print(f'{i} is a odd  number')
  

# consonants

words = input('Enter a word:').lower()
vowels = 'aeiou '
count = 0
for i in  words:
    if i  not in vowels:
        count +=1
        print(f'{i} is consonant')
print(count)


#adding duplicates values into empty list

nums = [23,78,97,5,78,5]
empty = []
for i in nums:
    if i not in empty:
        empty.append(i)
print(empty)
    



nums = (23,78,97,5,78,5)
x = set(nums)
unique_numbers = set(nums)
print(unique_numbers)
    

#split function.

words = input('enter a str: ')
text = words.split(' ')
print(text)
print(len(text))


digits = (1,2,3,3,4,5)
for i in digits:
    if i in digits:
        print(f'{i} is a duplicate')
















