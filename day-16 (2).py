#palindrome:

words = 'madam'
empty_str = ''
for i in words:
    empty_str = i + empty_str
if empty_str == words:
    print(f'{words} is a palindrome')
else:
    print(f'{words} is not a palindrome')

#Armstrong number:

num = 153
length = len(str(num))
armstrong = 0
for i in str(num):
    armstrong = armstrong + int(i)**length
    print(armstrong)
if armstrong == num:
    print(f'{num} is a armstrong number')
else:
    print(f'{num} is not a armstrong number')


#perfect nmber:

#1 + 2 + 3 = 6
#1 + 2 + 3 + 4 + 7 + 14 = 28


num = int(input('Enter a number: '))
sum = 0
for i in range(1,num):
      if num % i == 0:
             sum += i
if sum == num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')

#fibanocci series:
    
num = 0
num1 = 1
print(num,num1,end =' ')
for i in range(1,20):
    num2 = num + num1
    num = num1
    num1 = num2
    print(num2,end =' ')


             

             
            

