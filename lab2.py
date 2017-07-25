Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a = 4
>>> b = 'panda bears'
>>> "a " + b
'a panda bears'
>>> a + " " + b
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a + " " + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(a) + " " + b
'4 panda bears'
>>> name = "shelly Weisman"
>>> len(name)
14
>>> len(5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    len(5)
TypeError: object of type 'int' has no len()
>>> len("5")
1
>>> name[5]
'y'
>>> test = I love meet
SyntaxError: invalid syntax
>>> name = shelly Weisman
SyntaxError: invalid syntax
>>> name = "Sghelly Weisman"
>>> name.swapcase(e)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    name.swapcase(e)
NameError: name 'e' is not defined
>>> name.capitalize(e)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    name.capitalize(e)
NameError: name 'e' is not defined
>>> name
'Sghelly Weisman'
>>> name.remove("h")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    name.remove("h")
AttributeError: 'str' object has no attribute 'remove'
>>> name = "Shelly Weisman"
>>> name
'Shelly Weisman'
>>> name.upper()
'SHELLY WEISMAN'
>>> name
'Shelly Weisman'
>>> name.lower()
'shelly weisman'
>>> name.capitalize()
'Shelly weisman'
>>> name.swapcase()
'sHELLY wEISMAN'
>>> name.swapcase().swapcase()
'Shelly Weisman'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a = MEET
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a = MEET
NameError: name 'MEET' is not defined
>>> 
>>> 
>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> a = "MEET"
>>> b = "meat"
>>> c = "meat"
>>> a == b
False
>>> a==c
False
>>> b==c
True
>>> b = "meet"
>>> b==c
False
>>> a != b
True
>>> a != a
False
>>> 
