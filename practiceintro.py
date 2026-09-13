'''
print('Hello,Welcome to Python programming')
#perform operations as below

a = 15
b = 25
print(a+b)

'''
#tokens:-- keywords,variables,operators,punchuators [] - represents lists,() - represents tuples, {} - dictionary,sets.
#variables should not start start with number,space,symbols and also no space.
#netween words

batch = ['pfs-6' , 'da-6']
print(batch)
print(type(batch))   #evrything is an object (pop --> oop)
#len() --> returns the number of items in a collection.
print(len(batch)) #IDLE is a color coding editor (violet indicates --> built-in-functions)

#List -->to insert a collection of elements we use - append(),extend(),insert()
batch.append('Harshini')
print(batch)
'''
batch.append(['indhu','shreya'])
print(batch)
'''
batch.extend(['indhu','shreya'])
print(batch)
batch.insert(0,'santu') #inserts given value at specific index.
print(batch)
batch.insert(-1,'python') #insert can add value before index.
print(batch)
print(len(batch))

#Indexing -->[] -- In programming "Index" starts at 0 and ends at len(obj)-1
print(batch[0])
#print(batch[15])  # -- IndexError --> length is only 8 we are accesing extra so it will be raised an index error.

#Slicing --> Group of values[start:end]

print(batch[0:3])
print(batch[4:6])

# to print last 3 elements --> we use "negative indexing"

print(batch[-3:])
print(batch[:3])


# **** -- Striding ---> [start:end:step] ****

print(batch[::1])
print(batch[::2]) #it skips 1 element from start
print(batch[::3]) #it skips 2 elements from start
print(batch[1:5:2]) #it performs batch[1:5] -->then skip 1 element

print(batch[:7:4])
print(batch[7::4])
print(batch[1::5])
print(batch[1:7:-2]) #this case will receive an empty list.
print(batch[-1:-4:-1]) #in this case we come in reverse order








