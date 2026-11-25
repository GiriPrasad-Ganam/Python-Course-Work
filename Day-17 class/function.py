#def function name():
    #statements

# def numbers():
#     for i in range(0,11):
#         print(i)

# numbers()  

# numbers() 

# numbers() 

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


#find whether number is prime number or not.

# def factor(n):
#     c=0
#     for i in range(1,n+1):
#         if i%2==0:
#             c+=1
#     if c>2:
#         print('It is Not Prime No.')
#     else:
#         print('It is Prime No.')

# factor(int(input('Enter the Number: ')))


'''
Enter the Number: 5
It is Prime No.



Enter the Number: 8
It is Not Prime No.
'''



#simplicity prime number code:

# def isprime(n):
#     for i in range(2,n//2+1): #where prime number and non - prime have a 1 .so, remove 1->start with 2 
#         if n%i==0:
#             return "It is Not Prime No."
  
#     return "It is Prime No."

# print(isprime(int(input('Enter the Number: '))))



# def sum(n):
#     for i in range(n):
#         print(i)


# sum(input('Enter Number:').split())


# def sumofdigit(n):
#     sum = 0
#     while n>0:  #the number less than zero end the loop
#         sum+=n%10 #To find the remainder
#         n//=10  #to find the module division
#     return sum


# print(sumofdigit(int(input('Enter the number: '))))


'''
Enter the number: 1234
10
'''



# def rev_num(n):
#     sum = 0
#     while n>0:
#         sum = (sum*10) + n%10  # 0 *10 + 6 => 6 , 6 *10 + 4 => 64
#         n//=10                 # n = 1254
#     return sum

# print(rev_num(int(input('Enter the Number: '))))

'''
Enter the Number: 12546
64521
'''

'''
--------------------------------------------
type of Arugments
--------------------------------------------
'''


#Position arugment
#-----------------------------
# def display(name, email, password):
#     print('Name:', name)
#     print('Email:',email)
#     print('Password:', password)

# display('abc','abc@gmail.com','abc1234')
# display('abc@gmail.com','abc','abc1234') #not position arugments
# display('abc','abc1234','abc@gmail.com') #not position arugments

'''
Name: abc
Email: abc@gmail.com
Password: abc1234

Name: abc@gmail.com
Email: abc
Password: abc1234

Name: abc
Email: abc1234
Password: abc@gmail.com
'''


#keyword arugments: 
#----------------------------

# def display(name, email, password):
#     print('Name:', name)
#     print('Email:',email)
#     print('Password:', password)

# display(name='abc',email='abc@gmail.com',password='abc1234')
# display(email='abc@gmail.com',name='abc',password='abc1234') #not position arugments
# display(name='abc',password='abc1234',email='abc@gmail.com')

'''

Name: abc
Email: abc@gmail.com
Password: abc1234

Name: abc
Email: abc@gmail.com
Password: abc1234

Name: abc
Email: abc@gmail.com
Password: abc1234
'''

#default arugment:
#----------------------------
# def display(name, email, password, phone_no=None):
#     print('Name:', name)
#     print('Email:',email)
#     print('Password:', password)
#     print('Phone No:', phone_no)

# display(name='abc',email='abc@gmail.com',password='abc1234')
# display(name='abc',email='abc@gmail.com',password='abc1234', phone_no=123455678)

'''
Name: abc
Email: abc@gmail.com
Password: abc1234
Phone No: None

Name: abc
Email: abc@gmail.com
Password: abc1234
Phone No: 123455678
'''

#Variable-length positional arguments (*args):
#-----------------------------------------------

# def display(*n): #variable length 
#     print(n)

# display(1,2,3)
# display(1,2,3,4)
# display(1,2,3,4,5,6)

'''
(1, 2, 3)
(1, 2, 3, 4)
(1, 2, 3, 4, 5, 6)
'''


#Variable-length keyword arguments (**kwargs):
#--------------------------------------------------

# def display(**n):  
#     print(n)

# display(n1=1,n2=2,n3=3,n4=4)
# display(n1=1,n2=2)
# display(n1=1,n2=2,n3=3)

'''
{'n1': 1, 'n2': 2, 'n3': 3, 'n4': 4}
{'n1': 1, 'n2': 2}
{'n1': 1, 'n2': 2, 'n3': 3}

'''


#dict store name, marks
#list ->dict
#max=0 ->max(list[1]['marks'])


# def highestmark(data):
#     max = 0
#     res = ''
#     for i in data:
#         if data[i]>max:
#             max = data[i]
#             res = i

#     print(f'Highest marks {res}:{max}')


# def lowestmarks(data):
#     min = float('inf')
#     res = ''
#     for i in data:
#         if data[i]<min:
#             min = data[i]
#             res = i

#     print(f'Lowest marks {res}:{min}')



# data = {}
# for i in range(3):
#     name = input('Enter Your Name: ')
#     marks = int(input('enter your Marks: '))
#     data[name]=marks


# highestmark(data)

# lowestmarks(data)



#remove duplicate elements.
# list1 = list(map(int,input('Enter numbers: ').split()))
# list2 = []
# c = 0
# for i in range(len(list1)):
#     if list1[i] in list2:
#         list2.remove(list1[i])
#     else:
#         list2.append(list1[i])

# print(list2)














