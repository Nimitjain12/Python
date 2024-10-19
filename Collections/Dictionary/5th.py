list1= ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list2=[1, 2, 2, 3]

newdict={}
# d={1:2}
newdict1={}

for i,j in zip(list1,list2):
    # print(j)
    a={j}
    newdict={i:a}
    newdict1.update(newdict)
print(newdict1)

