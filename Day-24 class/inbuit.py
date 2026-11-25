#sys
#--------------------------
# import sys

# print(sys.argv)
# print(sys.path)
# print(sys.version)
# sys.exit
# print('hello world')

'''
['inbuit.py']
['C:\\Users\\ursgi\\OneDrive\\Desktop\\Python class\\Day-24 class', 'C:\\Users\\ursgi\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip', 'C:\\Users\\ursgi\\AppData\\Local\\Programs\\Python\\Python313\\DLLs', 'C:\\Users\\ursgi\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 'C:\\Users\\ursgi\\AppData\\Local\\Programs\\Python\\Python313', 'C:\\Users\\ursgi\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']
3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)]
hello world

'''


# platform
#------------------
# import platform
# print(platform.system(), platform.release(), platform.processor(),sep='\n')

'''
Windows
11
Intel64 Family 6 Model 140 Stepping 2, GenuineIntel
'''


#math
#------------------------

# import math

# print(math.pi)
# print(math.e)

# print(math.sqrt(25))
# print(math.sqrt(2))

# print(round(12.32))
# print(round(12.89))

# print(math.floor(12.89))
# print(math.ceil(12.89))

# print(math.factorial(4))
'''
3.141592653589793
2.718281828459045
5.0
1.4142135623730951
12
13
12
13
24
'''

# print(abs(-2))
# print(abs(2))

# print(math.fabs(-2))

'''
2
2
2.0
'''

# map module
#-----------------------------------
# print(math.gcd(12,6))

# print(math.log(2,2))

# print(math.sin(30))

# print(math.cos(30))

# print(math.tan(30))

# print(math.degrees(120))

# print(math.radians(120))

'''
2
2
2.0
6
1.0
-0.9880316240928618
0.15425144988758405
-6.405331196646276
6875.493541569878
2.0943951023931953

'''

#3) random 
#------------------------------------------
import random

# print(random.random()) # 

# print(random.randint(1,20)) # interger value

# print(random.uniform(1,20)) # random give float values


# l = ['Python', 'java', 'javascript']


# print(random.choice(l)) # select one choice 

# print(random.choices(l, k=2)) # select 

# print(l)
# print(random.shuffle(l))
# print(l)


'''
0.7173365458487927
10
13.033581862150355
Python
['java', 'javascript']
['Python', 'java', 'javascript']
None
['java', 'Python', 'javascript']

'''
#----------------------------------------
# print(random.seed(10)) # con
# random.seed(10)
# print(random.randint(1,10))

'''
None
10
'''
#-----------------------------------


#4) collection
#----------------------------------
from collections import Counter, defaultdict, deque
s = 'python programming'


#module 

# print(f'module: {Counter(s)}')


# #normal 
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1

# print(f'normal: {d}')


'''
module: Counter({'p': 2, 'o': 2, 'n': 2, 'r': 2, 'g': 2, 'm': 2, 'y': 1, 't': 1, 'h': 1, ' ': 1, 'a': 1, 'i': 1})
normal: {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}
'''

# d={}
# for i in s:
#     d[i]+=1

# print(d)
        

# d=defaultdict(int)
# for i in s:
#     d[i]+=1
# print(d)

'''
defaultdict(<class 'int'>, {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1})
'''

#deque([])-first in first out


# s = deque([])

# s.append(10)
# s.append(20)
# s.append(30)
# s.append(40)
# s.append(50)

# print(s)
# s.popleft()
# s.popleft()
# s.popleft()
# s.popleft()
# print(s)


'''
deque([10, 20, 30, 40, 50])
deque([50])
'''



# s = deque([])

# s.appendleft(10)
# s.appendleft(20)
# s.appendleft(30)
# s.appendleft(40)
# s.appendleft(50)

# print(s)
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# print(s)

'''
deque([50, 40, 30, 20, 10])
deque([50])
'''




#4) itertools
#--------------------------------

from itertools import combinations, permutations

s = 'abcd'
print([''.join(i) for i in combinations(s,3)])
print([''.join(i) for i in permutations(s,3)])

'''
['abc', 'abd', 'acd', 'bcd']
['abc', 'abd', 'acb', 'acd', 'adb', 'adc', 'bac', 'bad', 'bca', 'bcd', 
'bda', 'bdc', 'cab', 'cad', 'cba', 'cbd', 'cda', 'cdb', 'dab', 'dac', 
'dba', 'dbc', 'dca', 'dcb']
'''









