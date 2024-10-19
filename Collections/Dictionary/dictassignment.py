# my_dict = {
#     'x': list(range(11, 20)),
#     'y': list(range(21, 30)),
#     'z': list(range(31, 40))
# }
#
#
# print(my_dict['x'][4])
# print(my_dict['y'][4])
# print(my_dict['z'][4])

# mydict={
#     'x':list(range(11,20)),
#     'y':list(range(11,20)),
#     'z':list(range(11,20))
# }
# print(mydict['x'][4])

# dict={0: 10, 1: 20}
# dict[2]=dict.get(0)+dict.get(1)
# print(dict)

# 2)
# mydict={0:10,1:20}
# mydict[2]=40
# print(mydict)

# 3)
# mydict={0: 10, 1: 20, 2: 30}
# key=int(input())
# for i in mydict.keys():
#     if key in mydict:
#         print('it exist')
#         break
#     else:
#         print('not exist')
#         break
# 4)
# count=0
# Sample_data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# for i in Sample_data:
#     if i['success'] == True:
#         count+=1
# print(count)
# 5)
# l1= ['Class-V', 'Class-VII', 'Class-VII', 'Class-VIII',]
# l2=[1, 3, 2, 4,]
# dict={}
# for i,j in zip(l1,l2):
#     dict[i]=j
# print(dict)



# 6)
# mydict={}
# print(len(mydict))

# 7)
# from collections import Counter
#
# # Sample dictionaries
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
#
# # Combine the dictionaries using Counter
# combined_counter = Counter(d1) + Counter(d2)
#
# # Print the resulting counter
# print(combined_counter)

# 7)
# mydict = {}
#
# for key in d1:
#     mydict[key] = d1[key]
#
# for key in d2:
#     if key in combined_dict:
#         mydict[key] += d2[key]
#     else:
#         mydict[key] = d2[key]
#
# print(mydict)

# 8)
# dict1={'Names':['Rohit','Ganesh','SRK','Akshay'],'age':40,'addresses':['Mumbai','Delhi','Kolkara','Banglore'],'emails':['actor.gmail.com','movie.gmail.com']}
#
#
# count=0
# for i in dict1.values():
#     if isinstance(i, list):
#         count=count+len(i)
#
# print(count)

# 9)

# str1='w3resource'
# dict1={}
#
# for i in str1:
#     if i in dict1:
#         dict1[i]+=1
#     else:
#         dict1[i]=1
#
# print(dict1)

# 10)
# mydictionary={1:'xyz',3:'abc',5:'pqr',2:'xzz'}
# print(mydictionary.keys())
# print(mydictionary.values())
# print(mydictionary.items())

# 11)
# mydictionary = {1: 'xyz', 3: 'abc', 5: 'pqr', 2: 'xzz'}
# a=max(mydictionary.values())
# b=min(mydictionary.keys())
# print(a,b)

# 12)
# prnnos=[1,2,3,4,5,6]
# names=['abc','def','pqr','lmn','xyz','uvw']
# # newdict={}
# newdict=dict(zip(prnnos,names))
# print(newdict)

# 13)
# dictx = {'key1': 1, 'key2': 3, 'key3': 2}
# dicty = {'key1': 1, 'key2': 2}
#
# for i in dictx:
#     if i in dicty and dictx[i] == dicty[i]:
#         print(f"{dictx[i]}")
# 14)
# Players={'Rohit':{'runs':10000,'centuries':15},
#          'Virat':{'runs':12000,'centuries':18}}
# for i,j in Players.items():
#     print(i)
#     for key,value in j.items():
#         print(key,value)
# or

# players = {
#     'Rohit': {'runs': 10000, 'centuries': 15},
#     'Virat': {'runs': 12000, 'centuries': 18}
# }

# Print the dictionary line by line
# for player, stats in players.items():
#     print(f"Player: {player}")
#     for stat, value in stats.items():
#         print(f"  {stat}: {value}")
#     print()  # Print a newline for better readability

# 15)
# dict1={1: 'abc', 2: 'def', 3: 'pqr', 4: 'lmn', 5: 'xyz', 6: 'uvw'}
# n=int(input())
# if n in dict1.keys():
#     dict1.pop(n)
# print(dict1)

# 16)
# dict1={'d 01':'Abc','d 0 2':'Xyz','d0 3':'Pqr'}
# dict2={}
# for i, value in dict1.items():
#     new_key=i.replace(' ' , '')
#     dict2[new_key]=value
# print(dict2)

# 17)

# s=0
# k=0
# dict1={0: 10, 1: 20, 2: 30, 3:40, 4:50, 5:60}
# for i,j in dict1.items():
#     s+=i
#     k+=j
# print(s,k)

# 18)
# mydict1={1:1,2:4,3:9,4:16,5:25,6:36}
# mydict2={7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}
# result={}
# result.update(mydict1)
# result.update(mydict2)
# print(result)

# 19)
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# result={}
# result=dic1.copy()
# result.update(dic2)
# result.update(dic3)
# print(result)
