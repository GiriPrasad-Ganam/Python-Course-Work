'''
list comprision:
--------------------------
'''

# res = [i for i in range(1,11)] # [declaration iteration updates]
#                                # i - declaration, for i in range(1,11)-iteration, update - i*i 
# print(res)


# n = 16
# fact = [i for i in range(1,n+1) if n%i == 0]
# print(fact)         # declaration - 'i', iteration - 'for i in range(1,n+1)', update- 'if n%i== 0'


# names = ['swamy', 'raju', 'swathi']
# resn = [i for i in names if i.startswith('s')]
# #       |      |                |
# #declaration  iteration       updation
# #
# print(resn)
'''

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 4, 8, 16]
['swamy', 'swathi']

'''

# print('-------------------end--------------------')
'''
set comprision : just replace [] to { }
------------------------------
'''

# res = {i for i in range(1,11)} # [declaration iteration updates]
#                                # i - declaration, for i in range(1,11)-iteration, update - i*i 
# print(res)


# n = 16
# fact = {i for i in range(1,n+1) if n%i == 0}
# print(fact)


# names = ['swamy', 'raju', 'swathi']
# resn = {i for i in names if i.startswith('s')}
# #       |      |                |
# #declaration  iteration       updation
# #
# print(resn)


'''
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
{1, 2, 4, 8, 16}
{'swathi', 'swamy'}

'''


#-----------------------------------------------------------------
# tuple is not working because it is immutable. we cannot update.
#-----------------------------------------------------------------


'''
dict comprision:
'''

# res = {i:i*10 for i in range(1,11)} # [declaration iteration updates]
#                                # i - declaration, for i in range(1,11)-iteration, update - i*i 
# print(res)

'''
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90, 10: 100}
'''

n = 10
m = n // 2
for i in range(n):
    for j in range(n):
        Tandb = (i == 0 and m-1<=j<=m) or (i == n-1 and m-1<=j<=m)
        nxtTandb = (i == 1 and (j==1 or j==n-2)) or (i == n-2 and (j==1 or j==n-2))
        middle = (m-1<=i<=m and j == 0) or (m-1<=i<=m and j == n-1)
        if Tandb or nxtTandb or middle:
            print('* ', end='')
        else:
            print(' ', end='')

    print()

'''
  0 1 2 3 4 5 6 7
0       * *  
1   *         *  
2               
3 *             *
4 *             *
5
6   *         * 
7       * *
'''
