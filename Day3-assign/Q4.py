Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #Question-4
>>> X= int(input("enter the value:"))
enter the value:30
>>> Number=0
>>> while(Number<=30):
...     count=0
...     i=2
...     while(i<=Number//2):
...             if(Number%i==0):
...                     count=count +1
...                     break
...             i=i+1
...     if(count==0 and Number!=1):
...             print("%d"%Number,end='')
...     Number=Number+1
...
02357111317192329>>>