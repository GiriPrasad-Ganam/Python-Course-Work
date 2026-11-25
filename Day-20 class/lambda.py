# syntax:

# function Name = lambda parameter : operation(statements)



# sot = lambda a,b,c : a+b+c
# print(sot(10,20,30))

'''
60
'''

# gst = lambda price: price + price *0.18

# print(gst(20))
'''
23.6
'''

# avg = lambda l: sum(l)/len(l)

# l = [10,20,30]

# print(avg(l))

'''
20.0
'''

# iseven = lambda num: 'Even' if num%2 == 0  else 'Odd'

# print(iseven(15))

'''
Odd
'''

# isvowel=lambda ch:'vowel' if ch in 'aeiouAEIOU' else 'constant'

# print(isvowel('x'))

'''
constant
'''

'''
-------------------------------------
Nested condition-lambda
-------------------------------------
'''


# check = lambda data, pro: (f'stock Available :{data[pro]['price']}'if data[pro]['stock']>0 else 'Out of Stock')if pro in data else "Product Not Available"


# data = {

#     'apple': {'stock': 10, 'price':150},
#     'custard':{'stock':0, 'price':120},
#     'sapota':{'stock':5, 'price':160}
# }
# print(check(data,'xyz'))


'''
stock Available :150

Out of Stock

Product Not Available
'''

'''
---------------------------------
loop - lambda
---------------------------------
'''


#normal code

# def domain(d):
#     for i in range(len(d)):
#         d[i] = (d[i].split('@')[1]).split('.')[0]
#     return d
# d = ['xyz@codegnan.com', 'abc@gmail.com', 'pqr@yahoo.com']

# print(domain(d))


#lambda code

#my Method:
#----------------------
# domain = lambda d: [(d[i].split('@')[1]).split('.')[0] for i in range(len(d))]


# d = ['xyz@codegnan.com', 'abc@gmail.com', 'pqr@yahoo.com']

# print(domain(d))

'''
----------------------------
list-lambda
----------------------------
'''


#madam Method:
#------------------------
# d = ['xyz@codegnan.com', 'abc@gmail.com', 'pqr@yahoo.com']
# domain = list(map(lambda i : (i.split('@')[1]).split('.')[0],d))
# print(domain)


'''
['codegnan', 'gmail', 'yahoo']
'''

# c = ['sjhsj','asbdj','ddjvjd']

# convert = list(map(lambda i: i.upper(),c))
# print(convert)

'''
['SJHSJ', 'ASBDJ', 'DDJVJD']
'''


'''
------------------
Dict -  lambda
------------------
'''


# d = {'a':20,'b':30, 'c':1000, 'd':5000, 'e':2000}

# gst = dict(map(lambda i:(i[0],i[1]+i[1]*0.18),d.items()))
# #i[0]-> in tuple we access keys use 'i[0]'
# #i[1]->in tuple we access value use 'i[1]'
# #d.items -> it is return a both 'key and values'


# print(gst)

'''
{'a': 23.6, 'b': 35.4, 'c': 1180.0, 'd': 5900.0, 'e': 2360.0}
'''

#########################################
'''
------------------------------------------
map - is update values
filter - update in condition based on values
----------------------------------------------
map() – Changes every element in a collection.

filter() – Selects only the elements that satisfy a condition.


'''
################################################


# l = [1,2,3,45,23,1,67,3,2,7,9]
# even = list(filter(lambda i: i%2==0,l))

# print(even)

'''
[2, 2]
'''

###########################
'''
----------------
reduce- it is combine multiple elements into a single result
----------------
'''
###########################


from functools import reduce

# l = [1,2,3,45,23,1,67,3,2,7,9]

# sumof = reduce(lambda sum,i: sum+i,l)

# print(sumof)

'''
163
'''

# l = [1,2,3,45,23,1,67,3,2,7,9]

# maxof = reduce(lambda max,i:max if max>i else i,l)

# print(maxof)

'''
67
'''

'''
-------------------------------
Dict- lambda
######################
filter - check the element based on condition
map - update each and every element.
-------------------------------
'''

# s = {'s1':True, 's2':False, 's3': True, 's4':False, 's5':False}

# booked = dict(filter(lambda i : i[1] == True,s.items()))
# unbooked = dict(filter(lambda i : i[1] != True,s.items()))
# print(booked)
# print(unbooked)

'''
{'s1': True, 's3': True}

{'s2': False, 's4': False, 's5': False}
'''


d = {'laptop':90000, 'keyboard':52600, 'camera':15000, 'mouse':18000}

print(dict(sorted(d.items()))) #sorted a ascending order based on keys

print(dict(sorted(d.items(), reversed=True))) #descending order


print(dict(sorted(d.items(), key=lambda i:i[1]))) #sorted ascending order based on values

print(dict(sorted(d.items(), key=lambda i:i[1], reverse=True)))

'''
{'mouse': 18000, 'laptop': 90000, 'keyboard': 52600, 'camera': 15000}
{'camera': 15000, 'mouse': 18000, 'keyboard': 52600, 'laptop': 90000}
{'laptop': 90000, 'keyboard': 52600, 'mouse': 18000, 'camera': 15000}

'''



















