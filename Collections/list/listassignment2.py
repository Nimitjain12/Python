# def sum_values(*args):
#
#     total = sum(args)
#     return total
# print(sum_values(1,2))

#---------------------------------------------------
# list_assignment2
# ans1)
# list1=[1,2,3,4,5,6,7,8,9,10]
# v=int(input())
# list2=[]
# for i in list1:
#     if i>v:
#         list2.append(i)
# print(list2)

# 2)
# word_list = ['apple', 'banana', 'kiwi', 'grapefruit', 'mango', 'pineapple']
# n = 5
# ans = [i for i in word_list if len(i) > n]
# ans

# 3)
# mylist=[1,2,3,4,5,6,7,8,9]
# print(max(mylist))

# 4)
# lst = ['abc', 'xyz', 'aba', '1221']
# ans = [i for i in lst if len(i) >= 2 and i[0] == i[-1]]
# print(ans)

# 5)
# lst = [1,2,3,4,5,6,7,8,9,10]
# lst = [i*i for i in lst]
# print(lst)

# 6)
# lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# ans = [lst[i] for i in range(len(lst)) if i not in [0,4,5]]
# print(ans)

# 7)
# lst = [1,2,3,4,5,6,7,8,9,10]
# ans = [i for i in lst if i%2!=0]
# print(ans)

# 8)
# lst = [10, 20, 30, 40, 50]
# for i in range(len(lst)):
#     print(i, ':', lst[i], end='\t ')

# 9)
# mylist=[]
# if len(mylist)==0:
#       print('list is empty')
# else:
#       print('not empty')

# 10)
# mylist=[1,2,3,5,6,7,84,56]
# if mylist[5]!=0:
#     print("it exist")

# 11)
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = int(input('Enter a index'))
# if n > 0 and n < len(lst):
#     print('Exists')
# else:
#     print('Doesnt exist')

# 12)
# list1= ["Black", "Red", "Maroon", "Yellow"]
# list2=["#000000", "#FF0000", "#800000", "#FFFF00"]
# mydict=dict(zip(list1,list2))
# print(mydict)

# 13)
# Write a Python program to find the index of an item in a specified list.
#
# mylist=[1,2,3,4,5,6,7,8,9]
# num=int(input())
# for i in range(len(mylist)):
#  if mylist[i]==num:
#     print('it exist')
#     break
#  else :
#     print('not exist')

# 14)
# lst= [1,2,3,4]
# string ='emp'
# lst1= [string+str(i) for i in lst]
# print(lst1)

# 15)
# lst1= [0, 1, 2, 3,4,5,6, 7, 8, 9]
# lst2= [9, 8, 7, 6,5,4,3, 2, 1, 0]
# for i,j in zip(lst1,lst2):
#  print(i,j)

 # 16)
# mylist=[[1,3,4],[1,23,4],[5,6,8]]
# for i in mylist:
#      print(i)

# 17)
# mylist=[1,2,3,4,5,6,7,8,9,4,4,5,6,7,7,7]
# mynewlist=[]
# for i in mylist:
#     if i not in mynewlist:
#         mynewlist.append(i)
# print(mynewlist)

# 18)

# mylist=[1,3,5,7,9]
# mylist1=[2,4,6,8]
# mylist.extend(mylist1)
# print(mylist)

# 19)
# mylist=[1,2,3,4,5,6]
# mylist1=[6,7,8,9,0]
# def fun(mylist,mylist1):
#   for i in  mylist:
#     if i in mylist1:
#         return True
#
#   return False
# result=fun(mylist,mylist1)
# print(result)
