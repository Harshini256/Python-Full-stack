'''
Strings:
    Sequence of characters
Types of Strings:
1.Indexing:[]
 Indexing is used to get the character that you are looking to access.
They are 2 types of Indexing:
--> Positive Indexing
      Positive index start from 0 index
    Syntax:
     print(variable name[index_position])
example:
     
text = 'Santosh'
print(text[4])

--> Negative Indexing:
      Negative index start from -1 index
    Syntax:
     print(variable name[Negative index_position])
example:

text = 'Santosh'
print(text[-1])

2.Length ---> len() is a built in function is used to get number of char present in the string.
 Syntax: --> length(variable_name)

example:
text = 'Santosh'
print(len(text))

string = 'python is a programming language'
print(len(string))


3.Slicing:
   This "Slicing" is used to access the particular part from the string.
  Syntax:-->print(variable_name[start:end]
example:
string = 'python is a programming language'
print(string[12:])
print(string[:23])
print(string[12:23])

word = 'madam'
print(txt[::-1])


Upper():
-->Used to convert all small char into capital

string = 'python is a programming language'
print(string.upper())

Lower():
-->It is used to covert all capital letters into small letters.
 Syntax: --> print(variable_name.lower())

name = 'harshini'
User_input = input('Enter your name: ').lower

name = 'Python'
print(name.lower())

Index():
-->It is used to know the index position of a character.
 Syntax:print(variable_name.index('substring'))


txt = 'python is a programming language'
print(txt.index('i'))
print(txt[7])
print(txt.index('i', 9,))

replace():
 -->It is used to replace the old sub-string to new sub-string.
  Syntax: -->print(variable_name.replace('old substring' , 'new substring))
example:

txt = 'python is a programming language'
print(txt.replace('python', 'java'))
print(txt.replace(' ', 'web techologies'))

split():
--> This method is used to separate the string based on the given sub-string.
 Syntax:print(variable_name.split('sub-string'))
 
example:

txt = 'python is a programming language'
print(txt.split('p'))
print(txt.split(' '))

count():

 Syntax:-->print(variable_name.count('substring', start, end))
        -->print(variable_name.count('substring'))

example:

txt = 'python is a programming language'
print(text.count('a', 1, 20))







  
   

'''

text = 'Santosh'
print(text[4])
print(text[-1])

text = 'Santosh'
print(text[4])
print(text[-1])

string = 'python is a programming language'
print(len(string))


string = 'python is a programming language'
print(string[12:23])
print(string[12:])
print(string[:23])


word = 'madam'
print(word[::-1])

string = 'python is a programming language'
print(string.upper())


name = 'Python'
print(name.lower())

txt = 'python is a programming language'
print(txt.index('i'))
print(txt[7])
print(txt.index('i', 9,))

txt = 'python is a programming language'
print(txt.replace('python', 'java'))
print(txt.replace(' ', 'web techologies'))

txt = 'python is a programming language'
print(txt.split('p'))
print(txt.split(' '))

txt = 'python is a programming language'
print(text.count('a', 1, 20))









