'''
batch = ['santu', 'pfs-6', 'da-6', 'Harshini', 'indhu', 'python', 'shreya']
batch.insert(2,('vizag','hyd','rjy'))
print(batch)
print(len(batch[2]))
print(batch[2][:2])  #('vizag','hyd')
print(batch[2][1]) #this returns 'hyd' --> string
print(batch[2][::2]) #returns('vizag' , 'rjy')
print(batch[2].index('hyd')) #tuple will have only count,index
#index --> first occurence
#count --> returns the count of objects.
print(batch[2].count('codegnan'))  #returns count as 0   #index will raise error,where as count will return 0.

batch.insert(3,['Pfs','Da','Jfs'])
print(batch)
print(len(batch))

#now lwt us apply some of list functions in above batch list.
print(batch[3])
print(batch[3][1])

#convert  only jfs as upper case

batch[3][2] = batch[3][2].upper()
print(batch[3][2])

#now we want to add new course in batch[3] position --> AAA
batch[3].append('AAA')
print(batch[3])
print(len(batch))
batch.remove('indhu')  #remove() it can be applicable  for  --> value , -->pop() can be  remove the elements using index
print(batch)
batch.pop()   #pop by default removes index value
print(batch)

#batch[2].remove('hyd') --> it can raise an AttributeError
#del batch[2][1] #tuple is immutable so we can't insert/remove.

#batch.clear()   # if we want to remove entire data but keep the list as it is -->clear()
print(batch)

'''

#Lets work on Dictionaries:

# -- dictionary is a combination of key value pair [-> dict --> {k:v}] , keys must be unique , keys can be int,float,string,list


details = {}

print(len(details))
details['batch'] = ['pfs6']
print(details)
details['course'] = ['python full stack']
print(len(details))
print(details)
details['students'] = ['bhaagi','sneha','harshini']
print(details)
details.update({'batch':('hyd', 'vizag'),
                'subjects':{'python','aptitude','softskills'}})
print(details)
print(details.keys())
#details['batch'].extend(['JFS','DA'])
print(details)
details['students'].extend(['riya','sakshi'])
print(details)
details['subjects'].add('DSA')  #set is a unique and unordered.


#task --> details --> list,set,dictionary (use codegnan portal as example)
#exams,mock interviews,project demos.

#push to github --> share ur link in whatsapp group.
