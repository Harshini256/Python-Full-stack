'''
=== MODULES ===

   A module is a python file (.py) that return using functions,variables,operators etc...

example:

import math
print(math.pow(2, 3)

They are 2 types:

1.Built-in-Modules
    Modules are developed by the programmers and those comes with installation.
  example:
  1.math
  2.os
  3.sys
  4.random

2.User-defined-Modules:
    Users can create a file as of their own and import the file of module they created and get the expected output.

syntax: from module import function

example:

from harshini import add_
print(add_(50,7))


from harshini import sub_
print(sub_(8,1))


import harshini as hs
print(hs.mul_(5,7))


'''
   


#modules:

#1.Built-in-modules:

import math
print(math.pow(2, 3))


import os
print(os.getcwd())

import sys
print(sys.version)

import random
print(random.randint(1000, 9999))

#2.User-defined-modules:

from harshini import add_
print(add_(50,7))


from harshini import sub_
print(sub_(8,1))


import harshini as hs
print(hs.mul_(5,7))
