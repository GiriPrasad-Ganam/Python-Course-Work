# def reels():
#     res = ('101-200','201-300','301-400','401-500')
#     yield res[0]
#     yield res[1]
#     yield res[2]
#     yield res[3]


# feed = reels()
# print(feed)
# print(next(feed))
'''
<generator object reels at 0x0000011F1DDEB700>
101-200

'''
# print(next(feed))
# print(next(feed))
# print(next(feed))

'''
<generator object reels at 0x000001BD05CCB700>
101-200
201-300
301-400
401-500
'''

# def reels():
#     res = ('101-200','201-300','301-400','401-500')
#     for i in res:
#         yield i


# feed = reels()
# print(feed)
# print(next(feed))
# print(next(feed))
# print(next(feed))
# print(next(feed))

'''
101-200
201-300
301-400
401-500
'''

'''

feed = reels()
print(feed)             #for i in feed:
print(next(feed))       #   print(i)
print(next(feed))
print(next(feed))
print(next(feed))



'''


# def factorial(num):
#     for i in range(1, num+1):
#         if num%i == 0:
#             yield i

# fact = factorial(12)

# for i in fact:
#     print(i)

'''
1
2
3
4
6
12
'''


# def primes(n):
#     for i in range(2,n+1):
#         for j in range(2,i//2+1):
#             if i%j==0:
#                 break
#         else:
#             yield i        



# result = primes(20)

# for i in result:
#     print(i)

'''
2
3
5
7
11
13
17
19
'''

# def fibonacci(num):
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     for i in range(1,num):
#         c = a+b
#         print(c)
#         a = b
#         b = c




# fib = fibonacci(6)

'''
0
1
1
2
3
5
8

'''

# def fibonacci(num):
#     if num == 1:
#         yield 0
#     elif num>=2:
#         a = 0
#         b = 1
#         yield 0
#         yield 1
        
#     else:
#         yield 'not accepted negative value'
#     for _ in range(1,num):
#         c = a+b
#         a = b
#         b = c
#         yield c




# fib = fibonacci(6)

# for i in fib:
#     print(i)

'''
0
1
1
2
3
5
8
'''







































