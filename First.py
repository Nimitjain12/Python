# using normal functions
"""
def caller(fun,num):
    print("inside caller")
    fun(num)

def disp(var):
    print("inside disp\t",var)

caller(disp,10)
"""

# using lambda

caller=lambda fun,num: [print("inside caller lambda"), fun(num)]
disp=lambda var:print("inside disp lambda\t",var)

caller(disp,200)
