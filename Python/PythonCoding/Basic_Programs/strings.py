Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s1 = 'hello'
>>> s1
'hello'
>>> tpe(s1)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tpe(s1)
NameError: name 'tpe' is not defined. Did you mean: 'type'?
>>> type(s1)
<class 'str'>
>>> s1 capitalize()
SyntaxError: invalid syntax
>>> s1.upper
<built-in method upper of str object at 0x0000024242B338D0>
>>> s1.upper()
'HELLO'
>>> s1='hEllO'
>>> s1.casefold()
'hello'
>>> s1.count(s1)