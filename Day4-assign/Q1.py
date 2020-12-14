Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #Question-1
>>> File=open("HEY.txt",'w')
>>> File.write("I Love LetsUpgrade")
18
>>> File.close()
>>> File=open("HEY.txt",'r')
>>> content=File.read()
>>> File.close()
>>> print(content)
I Love LetsUpgrade
>>> File=open("HEY.txt",'a')
>>> File.write("I enjoy learning on LetsUpgrade")
31
>>> File.close()
>>>