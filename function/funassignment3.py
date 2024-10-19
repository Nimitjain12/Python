# 3)
# def fun1():
#     a=int(input())
#     b=input()
#     c=input()
#     return a,b,c
#
#
# print(fun1())
#----------------------------------------------------
# 4)
# def myfun2():
#    print("my function")
# def myfun3():
#     myfun2()
# myfun3()
#--------------------------------------------------
# 5)
# def myfun():
#     a=int(input())
#     if a>=1:
#         print("number is 1")
#     elif a<0:
#         print("number is -1")
#     else :
#         print("number is 0")
#     return a
# print(myfun())

#--------------------------------------------------
# 6)
# def myfun():
#     a=int(input())
#     if a>=97 and a<=122:
#         a-=32
#         print(chr(a))
#     elif a>=65 and a<=90:
#         a+=32
#         print(chr(a))
#     else :
#         print("wrong input")
#     return a
# trueval=myfun()
# print(chr(trueval))
#----------------------------------------------------------------------------------
# 7)
# def toggle_string(input_string):
#     return input_string.swapcase()
#
# # Example usage:
# user_input = input("Enter a string: ")
# toggled_string = toggle_string(user_input)
# print("Toggled string:", toggled_string)

# -----------------------------------------------------------------------
# 8)
# def validate_string(input_string='', min_length=3, max_length=5):
#     if len(input_string) < min_length or len(input_string) > max_length:
#         return f"Input must be between {min_length} and {max_length} characters."
#     return f"Valid input: '{input_string}'"
#
# # Example usage:
# user_input = input("Enter a string (3 to 5 characters): ")
# result = validate_string(user_input)
# print(result)

# 9)

# def sum_numbers(*args):
#     total_sum = sum(args)
#     return total_sum
#
# result=sum_numbers(1,2,3,4,5)
# print(result)



