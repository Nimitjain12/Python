# multiple Pythonbynimit

class Base1:
    def __init__(self,num1):
        self.num1=num1
        print("Base1 class constructor  ",self.num1)
    def disp1(self):
        print("Base1 disp1")

class Base2:
    def __init__(self,num2):
        self.num2=num2
        print("Base1 class constructor   ",self.num2)
    def disp2(self):
        print("Base2 disp2")

class Sub(Base1,Base2):
    def __init__(self):
        print("Sub class constructor")
    def disp3(self):
        print("Sub disp3")


s1 = Sub()
s1.disp1()
s1.disp2()
s1.disp3()
