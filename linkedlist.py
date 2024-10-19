class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last=None
    def add(self,data):
        ref=Node(data)
        if self.head==None:
            self.head=ref
            self.last=ref
        else:
            self.last.next=ref
            self.last=ref
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
    def sort(self):
        temp=0
        prev=self.head
        cur=self.head.next

        while(prev is not self.last):
            while(cur is not None):
                if(prev.data>cur.data):
                    temp=prev.data
                    prev.data=cur.data
                    cur.data=temp
                cur=cur.next
            prev=prev.next
            cur=prev.next
    def insert(self,data):
        ref=Node(data)
        if(ref.data<self.head.data):
            ref.next=self.head
            self.head=ref
        elif(ref.data>self.last.data):
            self.last.next=ref
            self.last=ref
        else:
            prev=self.head
            cur=self.head
            while(ref.data>cur.data):
                prev=cur
                cur=prev.next
            ref.next=cur
            prev.next=ref
    def delete(self,data):
        if(data==self.head.data):
            cur=self.head
            self.head=cur.next
            cur=None
        else:
            cur=self.head
            while(cur is not None):
                prev=cur
                cur=prev.next
                if(data==cur.data):
                    if(cur==self.last):
                        self.last=prev;
                        prev.next = None
                        cur=None
                    else:
                        prev.next=cur.next
                        cur=None



mylist=LinkedList()
mylist.add(45)
mylist.add(34)
mylist.add(55)
mylist.add(5)

mylist.display()
# mylist.sort()
# print("let's print sorted data")
# mylist.display()
# mylist.insert(40)
# print("after inserting")
# mylist.display()
# mylist.delete(40)
# print("after deleting in between node")
# mylist.display()
# mylist.delete(5)
# print("after deleting first node")
# mylist.display()
# mylist.delete(55)
# print("after deleting last node")
# mylist.display()
