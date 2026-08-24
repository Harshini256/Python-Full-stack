'''
Sets:
  Set is a unordered collection of elements.
  No Duplicates allowed in the set
  set is represented by "{}"
example:

nums = {1,2,3,4,4,4,5,5,28}
print(nums)

--- Operations of Sets: ---

-->1.Union:
     The union() function will combine two sets into a single set.
     It doesnot allow the duplicate values while combining the sets.
    Syntax:
     set_1.union(set_2) or set_1 | set_2
example:

data_ = {1,3,2,4}
nums = {8,5,4}
print(data_.union(nums))
      or 
data_ = {1,3,2,4}
nums = {8,5,4}
print(data_ | nums)


-->2.Intersection:
      It will gives us the common elements from both sets.
     Syntax:
       set_1.intersection(set_2) or set_1 & set_2

example:

data_ = {1,3,2,4}
nums = {8,5,4,5}
print(data_.intersection(nums))
print(data_ & nums)


-->3.Difference():
      It will display elements from set_1,but not the set_2 elements.
     Syntax:
      set_1.difference(set_2) or set_1 - set_2

example:

data_ = {1,3,2,4}
nums = {8,5,4}
print(nums.difference(data_))


-->4.Symmetric difference():
      Different elements from the both sets.
     syntax:

example:

data_ = {1,3,2,4}
nums = {8,5,4}
print(data_.symmetric_difference(nums))
print(nums ^ data_)



Methods of sets:

-->1.add()
      add() method will add only one element at a time.
     Syntax: set.add(element)

example:

data_ = {1,3,4,5}
print(data_)
data_.add(6)
print(data_)

-->2.Update():
      We can add more than one element by using update method.
     Syntax:
       set.update([elements]) or set_1.update(set_2)

example:

data_ = {1,2,3,4}
nums = {4,5,6}
print(data_)
data_.update([7,8])
print(data_)
data_.update(nums)
print(data_)


-->remove():
     The remove() method will delete the given element from the set,if the element is not present in the set then,it will raise a error.
    syntax:
     set.remove(element)

example:

data_ = {1,3,4,5}
data_.remove(3)
print(data_)

data_.remove(6)     (#It throws a error because the element doesnot present in the given data)
print(data_)


-->discard():
    This discard() method is used to delete the elements from the set,but never raise any error even the element not inside the set.
   Syntax:
   
     set.discard(element)

example:

data_ = {1,3,4,5}
data_.discard(6)     -->it will not throw any error if the element is not present in the given set of elements of data
print(data_)

data_ = {1,3,4,5}
data_.discard(1)    if the element is present in the given set it can delete the given element just like the remove() method.
print(data_)


-->5.clear():
       This method is used to delete all elements from the set and it will return empty set.
     Syntax: set.clear()

example:

data_ =  {1,2,3,4}
print(data_)
data.clear()
print(data_)



    



'''

nums = {1,2,3,4,4,4,5,5,28}
print(nums)


data_ = {1,3,2,4}
nums = {8,5,4}
print(data_.union(nums))
      
data_ = {1,3,2,4}
nums = {8,5,4}
print(data_ | nums)


data_ = {1,3,2,4}
nums = {8,5,4,5}
print(data_.intersection(nums))
print(data_ & nums)

data_ = {1,3,2,4}
nums = {8,5,4}
print(nums.difference(data_))
print(data_ - nums)

data_ = {1,3,2,4}
nums = {8,5,4}
print(data_.symmetric_difference(nums))
print(nums ^ data_)

data_ = {1,3,4,5}
print(data_)
data_.add(6)
print(data_)

data_ = {1,2,3,4}
nums = {4,5,6}
print(data_)
data_.update([7,8])
print(data_)
data_.update(nums)
print(data_)

data_ = {1,3,4,5}
data_.remove(3)
print(data_)

data_ = {1,3,4,5}
data_.discard(6)
print(data_)

data_ = {1,3,4,5}
data_.discard(1)
print(data_)

data_ =  {1,2,3,4}
print(data_)
data_.clear()
print(data_)


set_a = {9,3,8,4,7,2,6}
set_b = {1,3,5,7,9,4,2}

print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.symmetric_difference(set_b))

a = {'s','a','g','a','r','i','e'}
b = {'n','a','b','e','e','n','k','u','m','a','r'}

print(a.union(b))
print(a.intersection(b))
print(a.symmetric_difference(b))



print(b - a)

a.clear()
print(a)
b.clear()
print(b)















