# n = int(input()) 

# for i in range(1,n+1):
#   if n%i == 0:
#     print(i)

# n = int(input()) 
# sum = 0
# for i in range(1,n):
#   if n%i == 0:
#     sum = sum+i
# if sum == n :
#     print('Perfect number')
# else:
#    print('No perfect Number')      


# 5-1,2,3,4,5,
# 4 -2
# n = int(input()) 
# m = n//2
# for i in range(2,m+1):
#     if n%i == 0:
#         print('Not Prime')
#         break
#     print('prime')


n = 100
# r = []
# for i in range(1,n+1):
#     c = 0
#     for j in range(1,i+1):
#         if i%j == 0:
#            c+=1 
#     if c==2:
#         r.append(i)        

# print(r)


# prime = [i for i in range(1,n+1) if len([i for j in range(1,i+1) if i%j == 0]) == 2]
# print(prime)