'''
-----------------------------
Begineer Problems:
-----------------------------
'''

'''
1. Student Attendance Counter
A college wants to display student attendance numbers from 1 to N using recursion.
Task: Print numbers in ascending order.

'''

# def stu_count(n):
#     if n<1:
#         return 
#     stu_count(n-1)
#     print(n)

# std = int(input('Enter No. of Students: '))
# stu_count(std)

'''
1
2
3
4
5
'''


'''
2. Reverse Attendance Counter
A teacher wants to display student roll numbers from N to 1.
Task: Print numbers in descending order.

'''


# def stu_count(n):
#     if n<1:
#         return 
#     print(n)
#     stu_count(n-1)
    

# std = int(input('Enter No. of Students: '))
# stu_count(std)

'''
5
4
3
2
1
'''


'''
3. Shopping Cart Total
A customer purchases multiple products.
Task: Calculate the sum of all product prices using recursion.

'''

# price = list(map(int, input('Enter the product prices: ').split())) 
# # price = [100, 200, 300]

# def products(n):
#     if len(price)-1<n:
#         return 0
#     return price[n]+products(n+1)
# print(products(0))  

'''
Enter the product prices: 100 200 300
600
'''

'''
4. ATM Transaction Total
A customer performs multiple ATM withdrawals.
Task: Calculate the total withdrawal amount using recursion.
'''

# withdrawal =[1000, 2000, 500]
# # withdrawal = list(map(int,input().split()))

# def ATM(n):
#     if len(withdrawal)-1<n:
#         return 0
#     return withdrawal[n] + ATM(n+1)
# print(ATM(0))

'''
3500
'''


'''
5. Product Quantity Calculation
A shopkeeper has multiple product quantities.
Task: Calculate the total available quantity using recursion.
'''


# product =[10, 20, 30]
# # product = list(map(int,input().split()))

# def quantity(n):
#     if len(product)-1<n:
#         return 0
#     return product[n] + quantity(n+1)
# print(quantity(0))

'''
60
'''



'''
6. Employee Salary Calculation
A company wants to calculate the combined salary of its employees.
Task: Find the total salary using recursion.
'''

# Emp_sal =[15000, 20000, 25000]
# # Emp_sal = list(map(int,input().split()))

# def Total_sal(n):
#     if len(Emp_sal)-1<n:
#         return 0
#     return Emp_sal[n] + Total_sal(n+1)
# print(Total_sal(0))

'''
60000
'''

'''
7. Electricity Meter Units
An electricity company records daily electricity consumption.
Task: Calculate total electricity units consumed over N days.
'''

# Ele_Meter=[10, 20, 30]
# # Ele_Meter = list(map(int,input().split()))

# def electric(n):
#     if len(Ele_Meter)-1<n:
#         return 0
#     return Ele_Meter[n] + electric(n+1)
# print(electric(0))

'''
60
'''

'''

8. Factorial for Event Arrangements
An event organizer wants to calculate a factorial for a mathematical arrangement problem.
Task: Calculate N factorial using recursion.
'''

# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num-1)

# print(factorial(5))


'''
120
'''


'''
9. Sum of Digits in a Transaction ID
A banking application wants to calculate the sum of all digits in a transaction ID.
Task: Find the sum of digits using recursion.
'''

# def banking(num):
#     if num == 0:
#         return 0
#     digit = num % 10
#     mod = num // 10
#     return digit + banking(mod)


# print(banking(12345))


'''
15
'''


'''
10. Count Digits in an Employee ID
An organization wants to find how many digits are present in an employee ID.
Task: Count the digits using recursion.

'''


# def count(num):
#     if num == 0:
#         return 0
#     digit = num%10
#     mod = num//10
#     if digit:
#         return 1+count(mod)

# print(count(123))


'''
3
'''


'''
------------------------------------------
Intermediate Problems:
------------------------------------------
'''

'''
11. Reverse a Customer Name
A website wants to reverse a customer's name.
Task: Reverse a string using recursion.

'''


# string = input('Enter strings: ')

# string = 'Python'
# def reverse(num):
#     if len(string) == num:
#         return
#     reverse(num+1)
#     print(string[num])
# reverse(0)

'''
n
o
h
t
y
P

'''


'''
12. Palindrome Username Checker
A registration system wants to check whether a username is a palindrome.
Task: Check whether a string reads the same forward and backward.

'''


# string = 'Python'
# str = ''
# def reverse(n):
#     if len(string)-1<n:
#         return ''
#     str = str + string[n]
#     reverse(n+1)
# print(str)
# reverse(0)

































