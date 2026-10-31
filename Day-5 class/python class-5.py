Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2&5
0
2|5
7
2^5
7
2~5
SyntaxError: invalid syntax
2~
SyntaxError: invalid syntax
~2
-3
2>>
SyntaxError: invalid syntax
>>2
SyntaxError: invalid syntax
2<<
SyntaxError: invalid syntax
2>>
SyntaxError: invalid syntax
>>2
SyntaxError: invalid syntax
<<2
SyntaxError: invalid syntax
<2
SyntaxError: invalid syntax
a = input("enter your name: ")
enter your name: giri prasad
a
'giri prasad'
b = int(input("enter Your age:"))
enter Your age:25
b
25
c = float(input("enter your basic salary:"))
enter your basic salary:26000.23
c
26000.23
k = list(int(list(input("enter the number")))





         2332232315454
         
SyntaxError: '(' was never closed
k = list(int(list(input("enter the number"))))
         
enter the number12164664646
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    k = list(int(list(input("enter the number"))))
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
k = input()
         
k = input()
5664
         
5664
7
k = input()
         

k = input("enter the numbers:")
         
enter the numbers:12 2635 5689
k
         
'12 2635 5689'
k = input(" enter the numbers:").split()
         
 enter the numbers:12 2635 5689
k
         
['12', '2635', '5689']
k = map(int, input("enter the numbers:").split())
         
enter the numbers:12 2635 5689
k
         
<map object at 0x000001E1B3990A90>
k = list(map(int, input("enter the numbers:").split()))
         
enter the numbers:12 2635 5689
k
         
[12, 2635, 5689]
k = list(map(float, input("enter the numbers:").split()))
         
enter the numbers:12 2635 5689
k
         
[12.0, 2635.0, 5689.0]
k = tuple(map(str, input("enter the numbers:").split()))
         
enter the numbers:12 2635 5689
k
         
('12', '2635', '5689')
k = tuple(map(int, input("enter the numbers:").split()))
         
enter the numbers:12 2635 5689
k
         
(12, 2635, 5689)
k = tuple(map(float, input("enter the numbers:").split()))
         
enter the numbers:12 2635 5689
k
         
(12.0, 2635.0, 5689.0)
k = set(input("enter the numbers:").split()))
SyntaxError: unmatched ')'
k = set(input("enter the numbers:").split())
enter the numbers:12 2635 5689
k
{'12', '5689', '2635'}
k = set(map(int, input("enter the numbers:").split()))
enter the numbers:112 2653 5689
k
{112, 5689, 2653}
k = set(map(float, input("enter the numbers:").split()))
enter the numbers:12 2565 5689
k
{5689.0, 12.0, 2565.0}
email, address = input().split()
ganamgiriprasadyuqtdu@gmail.com
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    email, address = input().split()
ValueError: not enough values to unpack (expected 2, got 1)
email, address = input().split()
gabnnmdgjagdj@gmail  ydsajha
email
'gabnnmdgjagdj@gmail'
address
'ydsajha'
a = eval(input())
123
a
123
a = eval(input())
12.06
a
12.06
a = eval(input())
"hello"
a
'hello'
a = eval(input())
123 56 859 23
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a = eval(input())
  File "<string>", line 1
    123 56 859 23
        ^^
SyntaxError: invalid syntax
a = eval(input())
[123, 56, 32]
a
[123, 56, 32]
a = eval(input())
(123,56,32)
a
(123, 56, 32)
a = eval(input())
{123,56, 32}
a
{56, 32, 123}
a = eval(input())
{1:2,2:4,3:6}
>>> a
{1: 2, 2: 4, 3: 6}
>>> a = eval(input())
true
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a = eval(input())
  File "<string>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a = eval(input())
True
>>> a
True
>>> a = 10
>>> b = 10.02
>>> c = "codegnan"
>>> a
10
>>> b
10.02
>>> c
'codegnan'
>>> print(a, b, c)
10 10.02 codegnan
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 10.02 c= codegnan
>>> print("a=",a,"b=",b,"c=",c, sep="")
a=10b=10.02c=codegnan
>>> print("a=",a,"b=",b,"c=",c, sep="_")
a=_10_b=_10.02_c=_codegnan
>>> print("a=",a,"b=",b,"c=",c, sep="_" end="@")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> 
>>> print("a=",a,"b=",b,"c=",c, sep="_", end="@")
a=_10_b=_10.02_c=_codegnan@
>>> print(f'a={a}, b={b}, c={c}')
a=10, b=10.02, c=codegnan
>>> print('a={a}, b={b}, c={c}'.format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    print('a={a}, b={b}, c={c}'.format(a,b,c))
KeyError: 'a'
>>> print('a={}, b={}, c={}'.format(a,b,c))
a=10, b=10.02, c=codegnan
>>> print('a=%d, b=%f, c=%s'%(a,b,c))
a=10, b=10.020000, c=codegnan
