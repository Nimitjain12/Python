# 1)
# def mytuple1(elements):
#     count=0
#     for i in elements:
#       if isinstance(elements,tuple):
#        break
#     count+=1
#     return count
#
#
#
#
# 1)
# mylist=[10, 20, 30, 70,(40,50), 60]
# # result =mytuple1(mylist)
# # print(result)
# count=0
# for i in mylist:
#     if (type(i)==tuple):
#         break
#     else:
#         count+=1
# print(count)
# 2)
# mylist=(10,20,30,40,50,60)
# mylist.sort()
# print(mylist)


# mylist=Collections(mytuple)
# mylist.sort()
# print(mylist)
# mylist=tuple(mytuple)

# mytuple = (10, 20, 30, 90,50 ,60)
# mylist=Collections(mytuple)
# mylist.sort(reverse=True)
#
# mytuple = tuple(mylist)
# print(mytuple)

# 3)
import random
tuple=tuple(random.randint(1,10) for _ in range(1,10))
list1=list(tuple)
print(list)
repeated=[]
present=[]
for i in list1:
     if i in repeated:
         present.append(i)
     repeated.append(i)
print(present)

