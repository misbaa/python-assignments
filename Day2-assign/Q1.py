Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #Question-1
>>>
>>> txt="welcome to the page"
>>> x=txt.split()
>>> print(x)
['welcome', 'to', 'the', 'page']
>>> y=txt.capitalize()
>>> print(y)
Welcome to the page
>>> z=txt.center(25)
>>> print(z)
   welcome to the page
>>> m=txt.find("the")
>>> print(m)
11
>>> n=txt.index("welcome")
>>> print(n)
0
