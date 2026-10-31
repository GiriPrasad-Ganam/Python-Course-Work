Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list = [1,2,3,4,5,6]
list
[1, 2, 3, 4, 5, 6]
int(list)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int(list)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(list)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    float(list)
TypeError: float() argument must be a string or a real number, not 'list'
complex(list)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    complex(list)
TypeError: complex() first argument must be a string or a number, not 'list'
set(list)
{1, 2, 3, 4, 5, 6}
tuple(list)
(1, 2, 3, 4, 5, 6)
dist(list)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dist(list)
NameError: name 'dist' is not defined. Did you mean: 'list'?
dict(list)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(list)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(list)
True
b = (1,2,3,4,5)
b
(1, 2, 3, 4, 5)
int(b)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int(b)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(b)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    complex(b)
TypeError: complex() first argument must be a string or a number, not 'tuple'
list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'list' object is not callable
set(b)
{1, 2, 3, 4, 5}
list(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list(b)
TypeError: 'list' object is not callable
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(b)
True
set = {1,2,3,4,5}
set
{1, 2, 3, 4, 5}
int(set)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(set)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(set)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(set)
TypeError: float() argument must be a string or a real number, not 'set'
complex(set)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    complex(set)
TypeError: complex() first argument must be a string or a number, not 'set'
list(set)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(set)
TypeError: 'list' object is not callable
tuple(set)
(1, 2, 3, 4, 5)
dict(set)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict(set)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(set)
True
dict = {1:2, 2:4, 3:6, 4:8}
dict
{1: 2, 2: 4, 3: 6, 4: 8}
int(dict)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(dict)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(dict)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    float(dict)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(dict)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    complex(dict)
TypeError: complex() first argument must be a string or a number, not 'dict'
list(dict)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    list(dict)
TypeError: 'list' object is not callable
tuple(dict)
(1, 2, 3, 4)
set(dict)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    set(dict)
TypeError: 'set' object is not callable
>>> bool(dict)
True
>>> boolean = true
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    boolean = true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> boolean = True
>>> boolean
True
>>> int(boolean)
1
>>> float(boolean)
1.0
>>> complex(boolean)
(1+0j)
>>> list(boolean)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    list(boolean)
TypeError: 'list' object is not callable
>>> tuple(boolean)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    tuple(boolean)
TypeError: 'bool' object is not iterable
>>> set(boolean)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    set(boolean)
TypeError: 'set' object is not callable
>>> dict(boolean)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    dict(boolean)
TypeError: 'dict' object is not callable
