create single dimensional array

import numpy as np         #  here "numpy" is a module and "np" is an alias

first=np.array([100,200,300,400])
print(first)

for i in range(0,first.__len__()):
    print(first[i])

print(type(first))
print("dimension of array is\t",first.ndim)
print("\n")
print("shape of array is\t",first.shape)

first[4]=500     #  arrays are fixed
#------------------------------------------------------
# 1.a)
# create single dimensional array
#
# import numpy as np         #  here "numpy" is a module and "np" is an alias
#
# first=np.array((100,200,300,400))
# print(first)
#
# for i in range(0,first.__len__()):
#     print(first[i])
#
# print(type(first))
# print("dimension of array is\t",first.ndim)#they are properties which belong to class
# print("\n")
# print("shape of array is\t",first.shape)
#
# # first[4]=500     #  arrays are fixed
#-----------------------------------------------
# 1.b)
# # create single dimensional array
#
# import numpy as np
#
# # The elements of a NumPy array can also be booleans, strings, or other objects.
#
# first=np.array([100,3.4,"hello",True])
# print(first)
#
# for i in range(0,first.__len__()):
#     print(first[i])
#
# print(type(first))
# print("dimension of array is\t",first.ndim)
# print("\n")
# print("shape of array is\t",first.shape)
#
# # first[4]=500     #  arrays are fixed
#-----------------------------------------------
# 1.c)
# import numpy as k
# #indexing in numpy array
#
# arr1=k.array([10,20,30,40])
# print(arr1)
# print(arr1[0])
# print(arr1[-1])
# print("from the begining")
# for i in range(0,arr1.__len__()):
#     print(arr1[i])
# print("from the end")
# for i in range(-1,-(arr1.__len__()+1),-1):
#     print(arr1[i])



