#int float str bool list tuple set dict
#int float str bool set->inmutable(pass by value)
#list set dict -> mutable(pass by Reference)
# 
#    

'''
-----------------------------------------
call by value & call by Reference:
---------------------------------------------
'''

# def display(n):
#     n+=10
#     print('Inside the function',n)

# n = 10
# display(n)
# print(f"Outside function: {n}")

'''
Inside the function 20
Outside function: 10
'''


# def display(n):
#     n+=10.3
#     print('Inside the function',n)

# n = 10.3
# display(n)
# print(f"Outside function: {n}")


'''
Inside the function 20.6
Outside function: 10.3

'''



# def display(n):
#     n+='Programming'
#     print('Inside the function',n)

# n = 'Python'
# display(n)
# print(f"Outside function: {n}")

'''
Inside the function PythonProgramming
Outside function: Python
'''

# def display(n):
#     n=True
#     print('Inside the function',n)

# n = False
# display(n)
# print(f"Outside function: {n}")



'''
Inside the function True
Outside function: False
'''


# def display(n):
#     n+=(5,6)
#     print('Inside the function',n)

# n = (1,2,3,4)
# display(n)
# print(f"Outside function: {n}")

'''
Inside the function (1, 2, 3, 4, 5, 6)
Outside function: (1, 2, 3, 4)

'''

'''
-------------------------------------------------------------------
'''

# def display(n):
#     n+=[4,5]
#     print('Inside the function',n)

# n = [1,2,3,4]
# display(n)
# print(f"Outside function: {n}")

'''
Inside the function [1, 2, 3, 4, 4, 5]
Outside function: [1, 2, 3, 4, 4, 5]
'''

# def display(n):
#     n+={4,5}
#     print('Inside the function',n)

# n = {1,2,3}
# display(n)
# print(f"Outside function: {n}")





'''
---------------------------------------------------------------------
local scope: it is variable declared in function and we cannot access
vaiable outside.

global scope: it is declared outside of function and any where 
we access the variable.

global keyword: it is used to access inside local avriable to the outside any where
use 'global before variable'
---------------------------------------------------------------------
'''

#local scope

# def display():
#     n=10
#     print('inside',n)

# display()
# print('outside', n)


'''
inside 10

    print('outside', n)
                     ^
NameError: name 'n' is not defined

'''
#----------------------------------------------
#global scope

# n=10
# def display():
  
#     print('inside',n)

# display()
# print('outside', n)


'''
inside 10
outside 10
'''
#-----------------------------------
#global keyword:

# def display():
#     global n
#     n=10
#     print('inside',n)

# display()
# print('outside', n)

'''
inside 10
outside 10
'''

'''
GLOBAL
Module → Function

A function wants to modify a variable defined outside all functions.

NONLOCAL
Outer function → Inner function

An inner function wants to modify a variable in its enclosing function.
'''


# def display():
#     course = 'jps'
#     print('starting..:',course)
#     def update():
#         course = 'pfs'
#         print('Update:', course)
#     update()
#     print('final', course)
# display()

'''
starting..: jps
Update: pfs
final jps
'''


# def display():
#     course = 'jps'
#     print('starting..:',course)
#     def update():
#         global course
#         course = 'pfs'
#         print('Update:', course)
#     update()
#     print('final', course)
# display()


'''
starting..: jps
Update: pfs
final jps
'''

# def display():
#     course = 'jps'
#     print('starting..:',course)
#     def update():
#         nonlocal course
#         course = 'pfs'
#         print('Update:', course)
#     update()
#     print('final', course)
# display()

'''
starting..: jps
Update: pfs
final pfs

'''

'''
-----------------------
Note:
---------
inbulit function never declare variable. if declare it is working variable,
not inbulit function.
'''

# s = 'helloworld'
# max=20 # it is variable, not function anymore.
# print(max(s)) # it is function


#-----------------------------------------------------------------------

'''
recursion ->itself call function
'''




