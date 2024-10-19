# def square(num):
#     mysquare =lambda x : x ** 2
#     return mysquare(num)
# ans=square(2)
# print(ans)
from cProfile import label

from django.template.base import kwarg_re

#-------------------------------------------

# def name():

# myname = lambda :print("hello world")
#  # return myname
# sum = lambda x,y : x+y
# # newname=name()
# myname()
# sum1=sum(2,3)
# print(sum1)

#---------------------------------------------------------------------------------------------------------------
# 3)
# args=lambda x,y=20 : print(f"{x},{y}")
# args(10)

# def display_arguments(arg1, arg2="default argument"):
#     print("First argument:", arg1)
#     print("Second argument:", arg2)
#
# # Example usage
# display_arguments("Hello")  # Uses the default value for the second argument
# display_arguments("Hello", "Custom value")
#----------------------------------------------------------------------
# 4)
# args1= lambda **kargs1 :[print(i, j) for i,j in kargs1.items()]
# args1(name='abc',age=102,height=203,ram=20,rohit=30,rahul=30)


# def display_arguments(*args):
#     for i in args:
#         print(i)
# display_arguments("Hello", 42, 3.14, "Python", True)

r=lambda *kwargs: sum(kwargs)
result=r(93,3,5,5)
print(result)
