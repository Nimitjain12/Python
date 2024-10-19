# # 1)
# string1='hello world'.split()
# m=" ".join(string1[::-1])
# #n=string1.split()[::-1]
# print(m)

# 2)
# mylist=[]
# for i in range(5):
#     n=input("enter names")
#     mylist.append(n)
#
# mylist.sort()
# print(mylist)
# mylist.sort(reverse=True)
# print(mylist)

# 3)
count=0
mystring='internalization'
vowel='aeiou'
for i in mystring:
    if i in vowel:
        count+=1
print(count)



