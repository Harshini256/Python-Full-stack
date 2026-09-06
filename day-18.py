'''
map():

map() function will perform on all elements of a iterable.
syntax:
map(lambda arguments: expression, iterable)

example:

nums = [1,2,3,4,5]
data_ = map(lambda a: a+6,nums)
print(list(data_))


reduce():
The reduce() function repeatedly applies a function to elements and reduces them to one final value.
It is available in the functools module.

example:

from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,range(1,7))
print(data_)









'''
nums = [1,2,3,4,5]
data_ = filter(lambda a: a%2==0,nums)
print(tuple(data_))


nums = [1,2,3,4,5]
data_ = filter(lambda a: a>2,nums)
print(tuple(data_))

nums = [1,2,3,4,5]
data_ = map(lambda a: a+6,nums)
print(list(data_))


from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,nums)
print(data_)


from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,range(1,7))
print(data_)













