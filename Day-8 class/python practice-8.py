Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
Ori_list = ["Shirt", "Shoes", "Bag"]
Ori_list
['Shirt', 'Shoes', 'Bag']
dup_list = Ori_list
dup_list
['Shirt', 'Shoes', 'Bag']
id(Ori_list)
2297393825152
id(dup_list)
2297393825152
>>> dup_list.sort()
>>> dup_list
['Bag', 'Shirt', 'Shoes']
>>> Ori_list
['Bag', 'Shirt', 'Shoes']
>>> #this deep copy
>>> #this shallow copy
>>> 
>>> Ori_list = ["Shirt", "Shoes", "Bag"]
>>> Ori_list
['Shirt', 'Shoes', 'Bag']
>>> dup_list = ori_list.copy()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    dup_list = ori_list.copy()
NameError: name 'ori_list' is not defined. Did you mean: 'Ori_list'?
>>> dup_list = Ori_list.copy()
>>> dup_list
['Shirt', 'Shoes', 'Bag']
>>> id(dup_list)
2297393976832
>>> id(Ori_list)
2297393839808
>>> dup_list.sort()
>>> dup_list
['Bag', 'Shirt', 'Shoes']
>>> Ori_list
['Shirt', 'Shoes', 'Bag']
>>> a ={1,2,3,4,5}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a ={1,2,3,4,5}
>>> KeyboardInterrupt
>>> b= {1,2,3,4,5,6,7}
>>> a|b
{1, 2, 3, 4, 5, 6, 7}
>>> a&b
{1, 2, 3, 4, 5}
>>> a^b
{6, 7}
>>> a-b
set()
b-a
{6, 7}
a.isdisjoint(b)
False
b.isdisjoint(a)
False
a.subset(b)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.subset(b)
AttributeError: 'set' object has no attribute 'subset'. Did you mean: 'issubset'?
a.issubset(b)
True
b.issubset(a)
False
a.issuperset(b)
False
b.issuperset(a)
True
