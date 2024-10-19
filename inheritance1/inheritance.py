# 1)
# class grandfather:
#     def __init__(self):
#         super().__init__()
#         print('grandfather')
# class father(grandfather):
#     def __init__(self):
#         super().__init__()
#         print('father')
# class child(father):
#     def __init__(self):
#         super().__init__()
#         print('child')
#
# child()
# 2)
# class vehicle:
#     def start(self):
#         print('vehicle is starting')
# class fourwheeler(vehicle):
#     def start(self):
#         print('fourwheeler is stopped')
# myvehicle=fourwheeler()
# myvehicle.start()
from tkinter.font import names


# 3)
# class car:
#     def __init__(self):
#         print('parent class')
# class bmw(car):
#     def __init__(self):
#         super.__init__()
#         print('child class bmw')
# class mercedez(car):
#     def __init__(self):
#         super().__init__()
#         print('child class merc')
# # obj1=car()
# obj2=mercedez()

# 4)
# class top1:
#     def disp1(self):
#         print('parent class')
# class bottom1(top1):
#     def disp1(self):
#         print('child class 1')
# class bottom2(top1):
#     def disp1(self):
#         print('child class 2')
# class bottom3(top1):
#     def disp1(self):
#         print('child class 3')
# def perform(obj : top1):
#     obj.disp1()
# b1=bottom1()
# b2=bottom2()
# b3=bottom3()
# perform(b1)
# perform(b2)
# perform(b3)

# 5)
# class car():
#     def __init__(self,value):
#         self.value=value
#         print('parent class')
# class bmw(car):
#    def __init__(self,value,extra):
#     super.__init__(value)
#     self.extra = extra
#     print('child class')
# class audi(car):
#     def __init__(self):
#         super().__init__()
#     print('audi')

# substring=bmw(10,20)


# class Base:
#     def __init__(self, value):
#         self.value = value
#         print(f"Base class constructor called with value: {self.value}")
#
# class Sub(Base):
#     def __init__(self, value, extra):
#         super().__init__(value)  # Invoking the Base class constructor
#         self.extra = extra
#         print(f"Sub class constructor called with extra: {self.extra}")
#
# # Creating an instance of Sub class
# sub_instance = Sub(10, 20)

# 2)
# class vehicle():
#     def start(self):
#         print('parent class')
# class fourwheeler(vehicle):
#     def start(self):
#         print('child class')
# obj=fourwheeler()
# obj.start()

# 3)
# class base():
#     def __init__(self):
#         print('parent class')
# class sub1(base):
#     def __init__(self):
#         super().__init__()
#         print('child class 1')
# class sub2(base):
#     def __init__(self):
#         super().__init__()
#         print('child class 2')
# obj=sub2()
# # print(obj)
# obj1=sub1()
# print(obj1)

# 5)
# class base:
#     def __init__(self,name):
#         self.name=name
#         print('base class constructor')
# class sub(base):
#     def __init__(self,name,age):
#         self.age=age
#         self.name=name
#         print('sub class constructor')
#     def __str__(self):
#         return self.name + str(self.age)
# obj1=sub('nimit',23)
# print(obj1)



#-------------------------
# class students:
#     def __init__(self,name,age):
#           self.name=name
#           self.age=age
#     def __str__(self):
#         return " "+ self.name+ " "+str(self.age)
#
#     def.getname(self):
#          return self.name
#     def.getage(self):
#          return self.age
#
#
# s1=students('Nimit',23)
# s2=students('shubham',32)
# s3=students('anand',43)
#
# print(s1)
# print(s2)
# print(s3)



class students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('base class constructor')
    def __str__(self):
        return self.name +'\t'+ str(self.age)

    def getname(self):
        return self.name
    def getage(self):
        return self.age

s1=students('nimit',23)
print(s1)























