Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1 = 'hello'
type(s1)
<class 'str'>
id(s1)
2910130746976
s2='hi'
id(s2)
140733150082488
s3 = s1
id(s3)
2910130746976
s1
'hello'
s1='hi'
id(s1)
140733150082488
s1='india'
id(s1)
2910133558832
s1='indian'
id(s1)
2910133559120
list1 = [10,20]
list1
[10, 20]
type(list1)
<class 'list'>
list[0]
list[0]
list[-1]
list[-1]
list1 = [10,20,30,40]
list1
[10, 20, 30, 40]
list1[-1]
40
list1[0:3]
[10, 20, 30]
list1[0;4]
SyntaxError: invalid syntax
list1[0:4]
[10, 20, 30, 40]
list2 = list('hi','hello')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list2 = list('hi','hello')
TypeError: list expected at most 1 argument, got 2
s1
'indian'
list2=list(s1)
list2
['i', 'n', 'd', 'i', 'a', 'n']
list3 = list1
list3
[10, 20, 30, 40]
id(list1)
2910133470720
id(list3)
2910133470720
list4 = [100,'hi',100,True,69.33]
list4
[100, 'hi', 100, True, 69.33]
list4[2]=23
list4
[100, 'hi', 23, True, 69.33]
list1.append('hey')
list1
[10, 20, 30, 40, 'hey']
list1.remove('hey')
list1
[10, 20, 30, 40]
list1.count(20)
1
list1.insert(2,22)
list1
[10, 20, 22, 30, 40]
id(list1)
2910133470720
list1.pop()
40
list1
[10, 20, 22, 30]
list1.pop(2)
22
list1
[10, 20, 30]
list2
['i', 'n', 'd', 'i', 'a', 'n']
list2.clear()
list2
[]
del(list2)
list2
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    list2
NameError: name 'list2' is not defined. Did you mean: 'list1'?
tuple1=(11,22,33,44,55)
tuple1
(11, 22, 33, 44, 55)
tuple1[3]
44
tuple1[0:4:2]
(11, 33)
tuple1.index(44)
3
tuple1.count(22)
1
tuple2 = tuple1
tuple2
(11, 22, 33, 44, 55)
tuple3=tuple(list1)
tuple3
(10, 20, 30)
list1
[10, 20, 30]
list1.append(tuple1)
list1
[10, 20, 30, (11, 22, 33, 44, 55)]
list1[4]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    list1[4]
IndexError: list index out of range
list1[3]
(11, 22, 33, 44, 55)
list5=list(tuple1)
list5
[11, 22, 33, 44, 55]
tuple2 = (1,2,3,4,5)
tuple2
(1, 2, 3, 4, 5)
id(tuple2)
2910131719232
tuple2 = (1,2,3,4)
id(tuple2)
2910133515776
>>> set1 = {10,20,30,40,50}
>>> set1
{50, 20, 40, 10, 30}
>>> set1.add(25)
>>> set1
{50, 20, 40, 25, 10, 30}
>>> set2 = set(set1)
>>> set2
{50, 20, 40, 25, 10, 30}
>>> set2.remove(25)
>>> set2
{50, 20, 40, 10, 30}
>>> set1.union(set2)
{40, 10, 50, 20, 25, 30}
>>> set1.add('25')
>>> set1
{50, 20, '25', 40, 25, 10, 30}
>>> set1.intersection(set2)
{40, 10, 50, 20, 30}
>>> id(Set1)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    id(Set1)
NameError: name 'Set1' is not defined. Did you mean: 'set1'?
>>> id(set1)
2910133216512
>>> set1 = {1,2,3,4,5}
>>> id(set1)
2910133214496