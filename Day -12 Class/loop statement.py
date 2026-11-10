'''
loop can used string, list, tuples, set, dist, range()
'''

#for i in seq:
    #stat


#1)
# s = 'codegnan'
# for i in s:
#     print(i)
'''

c
o
d
e
g
n
a
n

'''


#2)for loop - string
# a = input('Enter the word:')
# for i in a:
#     if i in 'aeiouAEIOU':
#         print(i)

'''
Enter the word:world of word
o
o
o
'''


#3)for loop -list
# list = list(map(int, input().split()))
# for i in list:
#     if i%2 == 0:
#         print(f'It is Even No: {i}')
#     else:
#         print(f'it is odd No: {i}')


'''
12 15 2 4 7 8 
It is Even No: 12
it is odd No: 15
It is Even No: 2
It is Even No: 4
it is odd No: 7
It is Even No: 8

'''

#4)for loop - tuple
# sumoftuple = 0
# a = tuple(map(int, input("Enter the nums: ").split()))
# for i in a:
#     sumoftuple+=i
# print(f'Sum of Tuple is: {sumoftuple}')


'''
Enter the nums: 12 58 65 41
Sum of Tuple is: 176
'''

#5)for loop -set
# max = 0

# set = set(map(int, input("Enter the nos:").split()))
# for i in set:
#     if i>max:
#         max = i

# print(f'max of set is: {max}')


'''
Enter the nos:12 45 84 12 56 2 5 78 91 56
max of set is: 91
'''


#6)for loop -dict
# sum=0
# marks = {'python':89, 'sql':95, 'html':98, 'css':96, 'fastapi':89}
# for i in marks:
#     sum+=marks[i]
#     print(i,marks[i])
# print(f'Total Marks: {sum}')

'''
python 89
sql 95
html 98
css 96
fastapi 89
Total Marks: 467
'''


'''
range : generate sequence of numeric values(intergers value -1 0 +1)
'''
'''
Syntax:
range(start, end+1, steps)

'''


#step -1
# for i in range(0,10,1):
#     print(i)

'''
0
1
2
3
4
5
6
7
8
9
'''

#step-2
# for i in range(0, 10+1, 1):
#     print(i)

'''
0
1
2
3
4
5
6
7
8
9
10
'''


#step-3
# for i in range(1,11):
#     print(i)

'''
1
2
3
4
5
6
7
8
9
10
'''
#step- 4
# for i in range(20,0,-1):
#     print(i)


'''
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
'''

#print tables:


# num = int(input('Enter the Table:'))
# for i in range(1,11):
#     print(f'{num}*{i}={num*i}')

'''
8*1=8
8*2=16
8*3=24
8*4=32
8*5=40
8*6=48
8*7=56
8*8=64
8*9=72
8*10=80

'''


'''
range used - str, tuple, list
'''


# c ='codegnan'
# for i in range(len(c)):
#     print(f'{c[i]}{i}',end='')

'''
c0o1d2e3g4n5a6n7
'''


# problem:[12, 34, 45, 10, 78, 43, 80]
#0+1+

# list = [12, 34, 45, 10, 78, 43, 80]
# sum = 0
# for i in range(len(list)):
#     if list[i]%2 == 0:
#         sum+=i 

# print(sum)


#problem: odd product of index.



# list = [12, 34, 45, 10, 78, 43, 80]
# prod = 1
# for i in range(len(list)):
#     if list[i]%2 == 0:
#         ''
#     else:
#         prod*=i
# print(prod)




'''
-------------------------------------
Break - terminal statement
continue - skipped Statement

-------------------------------------

'''
# for i in range(1,11):
#     if i == 5:
#         break
#     print(i)

'''
1
2
3
4
'''


# print('              ')

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)

'''
1
2
3
4|---skipped 5 
6
7
8
9
10
'''


'''
----------------------------------
Pass - skipped errors
-----------------------------------

'''

# if true:
#     pass

# def func():
#     pass


'''
-----------------------------------------------------
Day-13 class
----------------------------------------------------------

'''

'''
========================================================================
ex: Break statements:
========================================================================
'''

#1)
# pin=12345
# for i in range(5):
#     epin=int(input('enter the pin: '))
#     if epin==pin:
#         print('login successful')
#         break
#     else:
#         print('invalid pin')

# print("max attempts reached! try again after 30 seconds")







#2)
# l=[2,4,6,7,2,450,90,25,34,56,40]
# search=int(input('enter the number: '))
# for i in range(len(l)):
#     if l[i]==search:
#         print(f'{search}, is found at {i}')
#         break
#     else:
#         print(f'{search}, is not found')




# enumerate (index, value)

# c={1,2,43,56,8,48,67,5}
# for i in enumerate(c):     #set         
#     print(i,i[0],i[1])


# c=[1,2,43,56,8,48,67,5]
# for i in enumerate(c):     #list
#     print(i[0],i[1])

# c=(1,2,43,56,8,48,67,5)
# for i in enumerate(c):     #tuple
#     print(i[0],i[1])

# c={'k1':'v1','k2':'v2','k3':'v3'}  # dict
# for i in enumerate(c):
#     print(i[0],i[1])




'''
-------------------------------------------
while loop:
-------------------------------------------

'''

#removing zero element from list

# l=[1,2,0,2,3,3,0,0,0,4,5,0,5,0,5,0,2,0,0,0,7]
# while 0 in l: # membership method
#     l.remove(0)

# print(l)


# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<len(a):
#     if a[i]==5:
#         break
#     print(i,a[i])
#     i+=1



#--------------------------------------------------------------------------
# Day - 14 class
#--------------------------------------------------------------------------

#problem 1
# l = [12,9,3,4,5,10,2,4,5,2,4,5]

# # output: first NO. + Last No.

# i = 0
# j = len(l)-1
# while i < j:              #my method
#     print(l[i]+l[j])
#     i+=1
#     j-=1


# i = 0
# j = len(l)-1
# while i<=j:               #madam Method
#     if i == j:
#         print(l[i])
#     else:
#         print(l[i]+l[j])
#     i+=1
#     j-=1




# bill = 0 

# while True:
#     product = input('Enter the Product name(Stop):')
#     if(product == 'STOP'):
#         print(f'Total Bill: {bill}')
#         break
#     price = int(input('Enter the Price:'))
#     qua = int(input('Enter the quantity:'))
#     bill+=price*qua

'''
Enter the Product name(Stop):ice cream
Enter the Price:12
Enter the quantity:2
Enter the Product name(Stop):shoes
Enter the Price:300
Enter the quantity:2
Enter the Product name(Stop):clothes
Enter the Price:5000
Enter the quantity:2
Enter the Product name(Stop):STOP
Total Bill: 10624
'''


#dict ->key(product) value(price)
#display menu
#pick the item
#user->enter the item
#qua ->enter the quan

#bill

#display -> pro qua pri & total bill

# Menu_card = {'dal_rice':130, 'biryani':250, 'samsoa':80, 'Egg_rice':100}
# bill = 0
# status = 
# while True:
#     print(f'pick the item in the Menu_card:{Menu_card}')
#     Pick_item = input('Enter the Item name(Exit):')
#     if Pick_item == 'Exit':
#         print(f'Products:{Pick_item} quantity: {qua}')
#         print(f'welcome to hotel, Total Bill: {bill}')
#         break
#     qua = int(input('Enter the quantity:'))
#     # bill+=qua*Menu_card[Pick_item]



#product list:
products = {
    'sugar':40,
    'salt':30,
    'cooking oil':120,
    'bread':40,
    'butter':60,
    'milk':30,
    'rice':150,
    'juice':80
}

#display products list:

# print('welcome to the store'.center(50,'-'))
# print('Product Name', 'Price')

#I get out Like this:
'''
---------------welcome to the store---------------
Product Name Price
sugar        : 40
salt         : 30
cooking oil  : 120
bread        : 40
butter       : 60
milk         : 30
rice         : 150
juice        : 80
Enter the Product Name(Exit): sugar
Enter the quantity:3
Enter the Product Name(Exit): milk
Enter the quantity:1
Enter the Product Name(Exit): rice
Enter the quantity:2
Enter the Product Name(Exit): juice
Enter the quantity:1
Enter the Product Name(Exit): exit
'''


# for i in products:
#     print(i.ljust(12,' '),':',products[i])


# #create empty set for add the pick products.
# carts= {}

# while True:
#     cart = input('Enter the Product Name(Exit): ').lower()
#     if cart == 'exit':
#         break
#     qua = int(input('Enter the quantity:'))
#     carts[cart] = qua

# print('Bill'.center(50,'-'))
# print('Product Name Quantity (₹)Price')
# bill = 0
# for i in carts:
#     print(i.ljust(12,' '),str(carts[i]).ljust(12,' '),products[i])
#     bill += carts[i] * products[i]


# print(f'Total Bill: ₹{bill}')
# print('Thanks for Shopping')



'''
Product Name Price
sugar        : 40
salt         : 30
cooking oil  : 120
bread        : 40
butter       : 60
milk         : 30
rice         : 150
juice        : 80
Enter the Product Name(Exit): sugar
Enter the quantity:3
Enter the Product Name(Exit): milk
Enter the quantity:1
Enter the Product Name(Exit): rice
Enter the quantity:2
Enter the Product Name(Exit): juice
Enter the quantity:1
Enter the Product Name(Exit): exit
-----------------------Bill-----------------------
Product Name Quantity (₹)Price
sugar        3            40
milk         1            30
rice         2            150
juice        1            80
Total Bill: ₹530
Thanks for Shopping
'''




'''
---------------------------------------------------------------------
Day - 15 Class (10.11.26)
---------------------------------------------------------------
'''


#Nested Loop
#1)
# for row in range(3): #outer Loop
#     for col in range(5):
#         print(col, end=' ') #inner loop
#     print()


#2)
# for row in range(3): #outer Loop
#     for col in range(5):
#         print(1, end=' ') #inner loop
#     print()

'''
1 1 1 1 1 
1 1 1 1 1 
1 1 1 1 1
'''

#3)
# for row in range(5): #outer Loop
#     for col in range(5):
#         print('*', end=' ') #inner loop
#     print()

'''
columns
|
__
* * * * * 
* * * * * 
* * * * * |->row 
* * * * * 
* * * * *
'''


# for row in range(5):
#     for col in range(5):
#         if (row+col)%2 == 0:
#             print(0, end=' ')
#         else:
#             print(1, end=' ')
#     print()


# for row in range(5):
#     for col in range(5):
#         if (row+col)%2 == 0:  |->simple way : print(int((row+col)%2==0),end=' ')
#             print(0, end=' ')||
#         else:                 |
#             print(1, end=' ')
#     print()



'''
    0 1 2 3 4
0   0 1 0 1 0
1   1 0 1 0 1
2   0 1 0 1 0
3   1 0 1 0 1
4   0 1 0 1 0


'''

# for row in range(5):
#     for col in range(5):
#         print(col%2, end=' ')
#     print()

# c=0
# for row in range(5):
#     for col in range(5):
#         print(c, end='  ')
#         c+=1
#     print()


'''
0  1  2  3  4  
5  6  7  8  9  
10  11  12  13  14  
15  16  17  18  19  
20  21  22  23  24  

'''    

# for row in range(5):
#     for col in range(5):
#         print(row * col, end=' ')
#     print()

'''
0 0 0 0 0 
0 1 2 3 4 
0 2 4 6 8 
0 3 6 9 12 
0 4 8 12 16 

'''

# for row in range(5):
#     for col in range(row+1):
#         print('*', end=' ')
#     print()


'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

# for row in range(5):
#     for col in range(5-row):
#         print('*', end=' ')
#     print()

'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

'''

    *
   **
  ***
 ****
*****

'''



