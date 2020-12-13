Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
#Question-3
>>> dict = {"brand" :"Ford","model":"Mustang","year":1964}
>>> x=dict.get("brand")
>>> print(x)
Ford
>>> y=dict.keys()
>>> print(y)
dict_keys(['brand', 'model', 'year'])
>>> dict.update({"color":"Black"})
>>> print(dict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'Black'}
>>> z=dict.values()
>>> print(z)
dict_values(['Ford', 'Mustang', 1964, 'Black'])
>>> dict.pop("color")
'Black'
>>> print(dict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>>