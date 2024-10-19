# # # print(dir(__builtins__))        #   built-in namespace
# # # print("\n\n")
# # # print("Type of builtins namespace is\t",type(__builtins__))
# # #
# # # k=100           # global for everyone
# # # def disp():
# # #     k=30        # local for disp but enclosing for inner
# # #     r=60
# # #     def inner():
# # #         k=60    # local for inner
# # #         print("inside inner")
# # #         print("let's access 'r' from enclosing scope\t",r)
# # #         print("let's access 's' from enclosing scope\t",s) # no problem even if 's' is defined below
# # #         print("local namespace for inner\t",locals())    # not only "k" but "r" also
# # #     print("hello")
# # #     print("local namespace for disp\t",locals())
# # #     print("\n")
# # #     print("Type of local namespace is\t",type(locals()))
# # #     s=800
# # #     inner()
# # #     # s=800
# # #
# # # num1=200
# # # print("\n\n\n")
# # # print(globals())
# # # print("\n\n")
# # # print("Type of global namespace is\t",type(globals()))
# # # print("\n\n")
# # # disp()
# #
# # # import time
# # # i=0
# # # start=time.time()
# # # name=input("enter your name")
# # # age=int(input("enter your age"))
# # # message="Name is {} and Age is {}"
# # # print(message.format(name,age))
# # # print("This program took\t",time.time()-start,"\tseconds")
# # #
# # # age=int(input("what is your age?"))
# # # print("Hello , I am {} years old".format(age))
# # #
# # # message="My name is {}"
# # # name=input("Enter your name")
# # # print(message.format(name))
# #
# # # name=input("enter your name")
# # # technology=input("enter technology name")
# # # preference=input("enter 'first' or 'second' as a preference")
# # # message="{} is {}'s {} preference"
# # # print(message.format(technology,name,preference))
# #
# # # print("{} loves {}!!".format("Everyone",
# # #                              "Python"))
# # #
# # # print("Python is {1}  {0} {2}  {3}"
# # #       .format("independent", "platform", "programming",
# # #               "language"))
# # #
# # # print("Every {3} should have {0} in order to {1} {2}"
# # #       .format("PVM", "execute", "Python", "Operating Systems"))
# #
# # # class Test:
# # #     x=10
# # #     def __init__(self,a,b):
# # #         self.a=a
# # #         self.b=b
# # #
# # # ref=Test   #  "ref"  refers to class object
# # # print(dir(ref))    #  observe that "x" is a member of class object because it's a static member
# # # ref1=Test  #  "ref1" refers to class object
# # # print("\n")
# # # print(id(ref)==id(ref1))   # true , as class object is one only and both "ref" and "ref1" refer to the same class object
# # # t1=Test(10,20)  # instance object
# # # t2=Test(30,40)  # instance object
# # # print("\n")
# # # print(dir(t1))   #  a and b also will be displayed
# # # print("\n")
# # # print(id(t1)==id(t2))   #  false
# #
# #
# # class Account:
# #     rate = 9  # class variable
# #
# #     def __init__(self, accid, name, balance):
# #         self.accid = accid
# #         self.name = name
# #         self.balance = balance
# #
# #     def getAccid(self):  # instance method
# #         return self.accid
# #
# #     def getName(self):  # instance method
# #         return self.name
# #
# #     def getBalance(self):  # instance method
# #         return self.balance
# #
# #     @classmethod
# #     def getRate(cls):
# #         return cls.rate
# #
# #     @staticmethod
# #     def calculateEMI(no_of_years, load_amt):
# #         return "calculated EMI per month"
# #
# #
# # c1 = Account(1, "Abc", 40000)  # instance object
# # c2 = Account(2, "Xyz", 70000)  # instance object
# #
# # print(c1.getAccid(), "\t", c1.getName(), "\t", c1.getBalance())
# # print(c2.getAccid(), "\t", c2.getName(), "\t", c2.getBalance())
# #
# # print(Account.getRate())
# #
# # print(Account.calculateEMI(10, 200000))
# # print(c1.__dict__)
# # temp = Account  # class object
# # print(temp.__dict__)
#
#
# # def sum_numbers(*args):
# #     total_sum = sum(args)
# #     return total_sum
# #
# # result=sum_numbers(1,2,3,4,5)
# # print(result)
#
# # create single dimensional array
#
# # import numpy as np         #  here "numpy" is a module and "np" is an alias
# #
# # first=np.array((100,200,300,400))
# # print(first)
# #
# # for i in range(0,first.__len__()):
# #     print(first[i])
# #
# # print(type(first))
# # print("dimension of array is\t",first.ndim)#they are properties which belong to class
# # print("\n")
# # print("shape of array is\t",first.shape)
#
# # first[4]=500     #  arrays are fixed
# #
# # # concate and stack 2d arrays with axis=0
# # # axis=0 means from top to bottom
# #
# # import numpy as np
# # arr1=np.array([[1,2,3],[4,5,6]])
# # arr2=np.array([[7,8,9],[10,11,12]])
# # arr3=np.concatenate((arr1,arr2),axis=0) #  keep arr1 and arr2 one below other,and create 2d array
# # print("output of concat")
# # print(arr3)
# #
# # """
# # [[ 1  2  3]
# #  [ 4  5  6]
# #  [ 7  8  9]
# #  [10 11 12]]
# #
# # """
# # print("dimension of new array after concat function is\t",arr3.ndim)
# # print("shape of new array after concat function is\t",arr3.shape)
# # print()
# # print()
# # print("output of stack")
# # arr4=np.stack((arr1,arr2),axis=0)    #  keep arr1 and arr2 one below other,and create 3d array
# # print(arr4)
# #
# # """
# # [[[ 1  2  3]
# #   [ 4  5  6]]
# #
# #  [[ 7  8  9]
# #   [10 11 12]]]
# #
# # """
# # print("dimension of new array after stack function is\t",arr4.ndim)
# # print("shape of new array after stack function is\t",arr4.shape)
#
#
# # concate and stack 2d arrays with axis=0
# # axis=0 means from top to bottom
#
# import numpy as np
# arr1=np.array([[1,2,3],[4,5,6]])
# arr2=np.array([[7,8,9],[10,11,12]])
# arr3=np.concatenate((arr1,arr2),axis=0) #  keep arr1 and arr2 one below other,and create 2d array
# print("output of concat")
# print(arr3)
#
# """
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
#
# """
# print("dimension of new array after concat function is\t",arr3.ndim)
# print("shape of new array after concat function is\t",arr3.shape)
# print()
# print()
# print("output of stack")
# arr4=np.stack((arr1,arr2),axis=0)    #  keep arr1 and arr2 one below other,and create 3d array
# print(arr4)
#
# """
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]
#
# """
# print("dimension of new array after stack function is\t",arr4.ndim)
# print("shape of new array after stack function is\t",arr4.shape)
#
#
# import numpy as np
#
# arr = np.array([5,8,9,11,12,16])
# print(arr)
#
# print(arr%4==0)  #  it prints  [False  True False False  True  True]
#
# print(arr[(arr%4==0)]) # it's like arr[[False  True False False  True  True]]
#
# print(arr[(arr>=9) & (arr<=15)])
#
# print(arr[(arr%3==0) | (arr%11==0)])
#
# #filter for values that are equal to 2, 3, 5, or 12
# print(np.isin (arr,[2, 3, 5, 12]))
# print("*****************")
#
# print(arr[np.isin(arr,[2, 3, 5, 12])])



import numpy as np

# axis=0 top to bottom

# axis=1 left to right

# a = np.arange(12).reshape((3, 4))
# print(a)
# print("***************")
"""
np.all() method return True if all the values fulfills the condition. 
This return value maps with the original array to give the filtered values

: means all rows
# """
# print(a[:, np.all(a < 10, axis = 0)])
# print("*********************")

""" np.any() method return true if any of the values fulfill the condition. 
 This return value maps with the original array to give the filtered values. 
 : means all the rows
 """
# print(a[:,np.any(a < 10, axis = 0)])
# print("*******************")

# from multipledispatch import dispatch
#
# @dispatch(int,int)
# def disp(val1,val2):
#     print("Inside int method\t",val1,"\t",val2)
#
# @dispatch(str,str)
# def disp(val1,val2):
#     print("Inside str method\t",val1,"\t",val2)
#
# disp("hello","world")
# disp(100,200)
# n = 5
#
# # Loop to print the pattern
# for i in range(5, n - 1):
#     print('* ' * i)

# n=7
# for i in range(1,n-1):
#     print(' ' * (n-i) + '*' * i )

# When a function decorated with @dispatch is called,
# the library inspects the arguments passed to the function
# and dispatches the call to the appropriate implementation
# based on the type and number of arguments.

# from multipledispatch import dispatch
#
#
# # passing two parameters
# @dispatch(int, int)
# def product(first, second):
#     result = first * second
#     print(result)
#
#
# # passing three parameters
# @dispatch(int, int, int)
# def product(first, second, third):
#     result = first * second * third
#     print(result)
#
#
# # you can also pass data type of any value as per requirement
# @dispatch(float, float, float)
# def product(first, second, third):
#     result = first * second * third
#     print(result)
#
#
# # calling product method with 2 arguments
# product(20, 4)
# product(2, 3, 2)
# product(2.2, 3.4, 2.3)

# how to read from a file


with open("details.json","r") as f:
    data=f.read()
    print(data)

print("Done")



