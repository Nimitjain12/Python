def add():
    print("will add")
def modify():
    print("will modify")
def delete():
    print("will delete")
a=int(input("enter the no"))
print(a)
match a:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
    case _ :
        print("wrong call")





