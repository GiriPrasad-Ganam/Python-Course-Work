# import logic

# print(logic.add(20,30))
# print(logic.mul(20,30))
# print(logic.sub(20,30))
# print(logic.div(20,30))
# print(logic.mod(20,30))
# print(logic.pow(20,30))


'''
50
600
-10
0.6666666666666666
20
1073741824000000000000000000000000000000

'''

# 'as' keyword is use long file into short term :
#---------------------------------------------------------
# import logic as lg

# print(lg.add(20,30))
# print(lg.mul(20,30))
# print(lg.sub(20,30))
# print(lg.div(20,30))
# print(lg.mod(20,30))
# print(lg.pow(20,30))


'''
50
600
-10
0.6666666666666666
20
1073741824000000000000000000000000000000

'''


# '*' it is import entire file including variables and functions and others.
#-------------------------------------------------------------------------

# from logic import *

# print(add(20,30))  # without defined import name before function name.
# print(mul(20,30))
# print(sub(20,30))
# print(div(20,30))
# print(mod(20,30))
# print(pow(20,30))

'''
50
600
-10
0.6666666666666666
20
1073741824000000000000000000000000000000
'''

# import specific function and varibale use this:
#----------------------------------------------------
from logic import add, mul

print(add(20,30))  
print(mul(20,30))

'''
50
600
'''

