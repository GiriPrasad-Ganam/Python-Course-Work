#1)
# Product = input("Enter the product:")

# bestseller = eval(input("Enter the status:"))

# if bestseller:
#     print(f'{Product} is best seller.')


'''this is realtime application example of simple if'''
# #2)
# Battery = int(input("Enter the Battery:"))
# if Battery<20:   #Enter the Battery:60   #Enter the Battery:10
#                 #Battery is low: 10, charge your phone.
#     print(f'Battery is low: {Battery}, charge your phone.')

#3
# bill = int(input("Enter the bill:"))
# status = eval(input("Is it raining?True/False: "))

# if status:
#     bill+=30
#     print("Extra delivery Charges Applied")

'''
Enter the bill:25
Is it raining?True/False: False
Final Bill: 25


Enter the bill:12
Is it raining?True/False: True
Extra delivery Charges Applied
Final Bill: 42

'''    

# print(f'Final Bill: {bill}')


'''---------------------------------------------
Day-12 class (03.11.26)
---------------------------------------------'''
#If else  Problems:
# 
#1)
# data = ('admin@gmail.com', 'admin@123') 

# Email = input('Enter the email Id:')
# Password = input('Enter the password:')

# if(Email,Password) == data:
#     print('Successfully Login')
# else:
#     print('Invalid login')

'''
output :

Enter the email Id:admin@gmail.com
Enter the password:admin@123
Successfully Login
'''


#2)

# seats = {
#     's1':'Booked',
#     's2':'Avaliable',
#     's3':'Avaliable',
#     's4':'Avaliable',
#     's5':'Avaliable',
#     's6':'Booked',
#     's7':'Avaliable'
# }

# seatno = input('Enter the seatno(sn):')

# if seatno in seats and seats[seatno] == 'Avaliable':
#     seats[seatno]= 'Booked'
#     print(f'{seatno} is Booked successfully')
#     print(seats)
# else:
#     print(f'{seatno} is already booked')

'''
Enter the seatno(sn):s2
s2 is Booked successfully
{'s1': 'Booked', 's2': 'Booked', 
's3': 'Avaliable', 's4': 'Avaliable', 
's5': 'Avaliable', 's6': 'Booked', 's7': 'Avaliable'}
'''

#3)
# Products = {
#     'laptop':{'price': 50000, 'stock': 10},
#     'mobile':{'price': 20000, 'stock': 20}, 
#     'keyboard':{'price': 2000, 'stock': 30},
#     'mouse':{'price': 1000, 'stock': 0},
#     'headphone':{'price': 5000, 'stock': 5},
# }

# search = input('Enter the product name:')
# if search in Products and Products[search]['stock'] > 0:
#     print(f'you can buy {search} at this price ₹ {Products[search]["price"]}')
# else:
#     print(f'{search} is not available or out of stock.')

'''
Enter the product name:laptop
you can buy laptop at this price ₹ 50000

Enter the product name:mouse
mouse is not available or out of stock.

'''


'''
--------------------------------------------------------
else if ladder:
---------------------------------------------------------

'''

# print('Welcome to the weekend Planner')

# budget = int(input('Enter the Budget: '))

# print('you can go for', end=' ')

# if budget > 10000:
#     print('Trip')
# elif budget > 5000:
#     print('Resort')
# elif budget > 2000:
#     print('cafe')
# elif budget > 1000:
#     print('movie')
# elif budget > 5000:
#     print('street shopping')
# else:
#     print('sleep')

'''
Welcome to the weekend Planner
Enter the Budget: 5000
you can go for cafe


Welcome to the weekend Planner
Enter the Budget: 5500
you can go for Resort

'''




'''
---------------------------------------------------------------
Nested 
----------------------------------------------------------------
'''

# data = {
#     'praveen':{'status':True, 'python':96, 'mysql':94, 'fastapi':87},
#     'krishna':{'status':True, 'python':84, 'mysql':77, 'fastapi':74},
#     'teja':{'status':True, 'python':77, 'mysql':74, 'fastapi':69},
#     'Raju':{'status':False, 'python':None, 'mysql':None, 'fastapi':None},
#     'Manju':{'status':True, 'python':35, 'mysql':54, 'fastapi':41},
# }

# name = input('Enter the Name:')

# if name in data:
#     if data[name]['status']:
#         total = data[name]['python']+data[name]['mysql']+data[name]['fastapi']
#         avg = total/3
#         if avg > 80:
#             print(f'{name}, congrates you got the first grade')
#         elif avg >60:
#             print(f'{name}, good workhard next time')
#         elif avg >40:
#             print(f'{name}, better luck next time')
#         elif avg >35:
#             print(f'{name}, you just passed')
#         else:
#             print(f'{name}, you Failed, get your Parents')
#     else:
#         print(f'{name}, didnt attend the exam. bring your parents')

# else:
#     print('f{name}, Not found in the Data')        



# '''
# PS C:\Users\ursgi\OneDrive\Desktop\Python class\Day-10 class> py "Conditional statement.py"
# Enter the Name:teja
# teja, good workhard next time

# PS C:\Users\ursgi\OneDrive\Desktop\Python class\Day-10 class> py "Conditional statement.py"
# Enter the Name:manju
# f{name}, Not found in the Data

# PS C:\Users\ursgi\OneDrive\Desktop\Python class\Day-10 class> py "Conditional statement.py"
# Enter the Name:Manju
# Manju, better luck next time

# PS C:\Users\ursgi\OneDrive\Desktop\Python class\Day-10 class> py "Conditional statement.py"
# Enter the Name:Raju
# Raju, didnt attend the exam. bring your parents
# '''



