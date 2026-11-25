# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print(' '*(j+1),'*'*(n-j), end=' ')
#     print()


# for row in range(n):
#     for sp in range(n-1-row):
#         print(' ',end=' ')
#     for col in range(row+1):
#         print('*',end=' ')

#     print()


# for row in range(n):
#     for sp in range(row):
#         print(' ', end=' ')
#     for col in range(n-row):
#         print('*',end=' ')
#     print()

'''
5
* * * * * 
  * * * * 
    * * * 
      * * 
        *
'''

# len_col = int(n/2)
# for i in range(n):
#     for col in range(i-(len_col+1)):
#         print('*', end=' ')
#     for col in range(len_col-i):
#         print(' ', end=' ')
#     print()


# m = n//2
# for row in range(n):
#     if row <=m:
#         for col in range(row+1):
#             print('*', end=' ')
#     else:
#         for col in range(n-row):
#             print('*', end=' ')
#     print()


'''

9
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
* 
'''


#above pattern simply pattern:

# m = n/2
# for row in range(n):          
#     if row <=m:
#         print('* '*(row+1))   #--|
#     else:                     #  |-->print('* '*(row+1) if row<=m else '* '*(n-row))   
#         print('* '*(n-row))   #--|


'''

9
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''


# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1:
#             print('*', end= ' ')
#         else:
#             print(' ', end= ' ')
#     print()

'''
5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''
# m = n//2
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1 or i == m or j == m:
#             print('*', end= ' ')
#         else:
#             print(' ', end= ' ')
#     print()

'''
5
* * * * * 
*   *   * 
* * * * * 
*   *   * 
* * * * * 

'''

# m = n//2
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1 or i==j or (j+i)==(n-1):
#             print('*', end= ' ')
#         else:
#             print(' ', end= ' ')
#     print()

'''
5
* * * * * 
* *   * * 
*   *   * 
* *   * * 
* * * * *


10
* * * * * * * * * * 
* *             * * 
*   *         *   * 
*     *     *     * 
*       * *       * 
*       * *       * 
*     *     *     * 
*   *         *   * 
* *             * * 
* * * * * * * * * * 
'''



# m = n//2
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1:
#             print('*', end= ' ')
#         elif (j+i)==(n-1) or m ==i or n == j or i==j:
#             print('A', end = ' ')
#         else:
#             print(' ', end= ' ')
#     print()



# m =n//2
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == n-1 or (i==n-1 and i>=m) or (j==m and j>=m) or i==n-1:
#             print('*', end = ' ')
#         else:
#             print(' ',end = ' ')
#     print()


# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == m or (i == n-1 and j<=m) or (j==0 and i>=m):
#             print('*', end=' ')
#         else:
#             print(' ',end=' ')
#     print()

'''

8
* * * * * * * * 
        *       
        *       
        *       
*       *       
*       *       
*       *       
* * * * *  
'''


# m=n//2
# for i in range(n):
#     for j in range(n):
#         if j == 0 or j == n-1 or (i==j and i<=m) or (j+i==n-1 and i<=m):
#             print('*', end=' ')
#         else:
#             print(' ',end=' ')
#     print()


'''

8
*             * 
* *         * * 
*   *     *   * 
*     * *     * 
*     * *     * 
*             * 
*             * 
*             * 
'''


####################################################################################
'''
Patterns
'''
####################################################################################

'''
  0 1 2 3 4 
0   * * *
1 *       *
2 * * * * *     
3 *       *
4 *       *    

'''
# n = int(input())
# m = n//2
# for i in range(n):
#     for j in range(n):
#         if (j==0 and i!=0) or ((j==n-1) and i!=0) or m==i or (i == 0 and 1 <= j <= n-2):
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()



'''
  0 1 2 3 4 
0 * * * * 
1 *       *
2 * * * *      
3 *       *
4 * * * *   

'''

# n = int(input())
# m = n//2
# for i in range(n):
#     for j in range(n):
#         if (i==0 and 0<=j<=n-2) or (i==n-1 and 0<=j<=n-2) or (i==m and 0<=j<=n-2) or j==0 or (j==n-1 and 1<=i<m) or (j==n-1 and m<i<n-1):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


'''
  0 1 2 3 4 
0   * * * *
1 *      
2 *      
3 *       
4   * * * *  

'''

# n = int(input())
# m = n//2
# for i in range(n):
#     for j in range(n):
#       if (i==0 and 1<=j<n) or (i==n-1 and 1<=j<n) or (j==0 and 1<=i<n-1):
#          print('*', end=' ')
#       else:
#          print(' ',end=' ')
#     print()



'''
  0 1 2 3 4 
0 * * * * 
1 *       *
2 *       *
3 *       *
4 * * * *   

'''


# n = int(input())
# m = n//2
# for i in range(n):
#     for j in range(n):
#         if (i==0 and j<n-1) or (i==n-1 and j<n-1) or j==0 or (j==n-1 and 1<=i<n-1):
#             print('*', end=' ')
#         else:
#             print(' ',end=' ')
#     print()


'''
  0 1 2 3 4 
0 * * * * *
1 *       
2 * * * * *      
3 *       
4 * * * * *   

'''

# n = int(input())
# m = n//2
# for i in range(n):
#     for j in range(n):
#         if (i==0 or i==m or i==n-1) or (j==0 and j<n):
#           print('*', end=' ')
#         else:
#           print(' ', end=' ')            
#     print()


'''
  0 1 2 3 4 
0 * * * * *
1 *       
2 * * * * *      
3 *       
4 *  

'''

n = int(input())
m = n//2
for i in range(n):
  for j in range(n):
    if i==0 or j==0 or m==i:
      print('*',end=' ')
    else:
      print(' ',end=' ')
  print() 







