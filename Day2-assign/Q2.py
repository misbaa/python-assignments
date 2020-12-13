Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #Question-2
>>> lst=["pen","pencil","notebook","bag"]
>>> lst.append("waterbottle")
>>> print(lst)
['pen', 'pencil', 'notebook', 'bag', 'waterbottle']
>>> x=lst.count("notebook")
>>> print(x)
1
>>> lst.insert(2,"chalk")
>>> print(lst)
['pen', 'pencil', 'chalk', 'notebook', 'bag', 'waterbottle']
>>> y=lst.index("bag")
>>> print(y)
4
>>> lst.reverse()
>>> print(lst)
['waterbottle', 'bag', 'notebook', 'chalk', 'pencil', 'pen']
>>>