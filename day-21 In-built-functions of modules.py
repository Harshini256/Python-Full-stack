
#In built functions:

#math function
import math
print(math.pi)
print(math.ceil(4.3))
print(math.floor(5.6))
print(math.sqrt(25))
print(math.sin(2))
print(math.pow(2, 3))

#random function
import random
print(random.randint(100000, 999999))
print(random.randrange(1, 100))

color = ['green','red','white','purple']
print(random.choice(color))
random.shuffle(color)
print(color)

#platform function

import platform
print(platform.python_version())
print(platform.system())
print(platform.platform())
print(platform.processor())

#collections function

import collections
data_ = ['banana','strawberry','apple','banana','apple']
print(collections.Counter(data_))
all = collections.Counter(data_)
print(all.most_common())


#defaultdict

from collections import defaultdict
data_ = defaultdict(list)
data_['python'].append('harshini')
data_['python'].append('honey')
data_['java'].append('sony')
print(data_)

#date & time:

from datetime import datetime
today = datetime.today()
now = datetime.now()
print(today.month)
print(today.day)
print(today.year)
print(today.hour)
print(today.minute)

from datetime import datetime
now = datetime.now()
print(now.strftime('%d-%m-%y'))
print(now.strftime('%H-%M-%S'))
print(now.strftime('%c'))



#=== guess the number ===

import random
atmpt_ = 3
num = random.randrange(1, 100)
print(num)
while atmpt_ >0:
    game_ = int(input('enter a number between 1 and 100: '))

    if game_ == num:
        print('your guess is correct')
        break
    else:
        atmpt_ -= 1

if atmpt_ ==3:
    print('price money is 500')
elif atmpt_ ==2:
    print('price money is 250')
elif atmpt_ ==1:
    print('price money is 100')
else:
    print('better luck next time ...')


#itertools :--

import itertools
a = itertools.count(45)
print(next(a))
print(next(a))

b = itertools.repeat('python', 3)
for i in b:
    print(i)

c = itertools.cycle(['python','java','c'])
for j in c:
    print(j)


n = itertools.chain([1,4,3],[1,4,3,2])
print(list(n))


        
        











