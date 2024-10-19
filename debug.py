def main(fun):
    if callable(fun):
        fun()
    else:
        print("You passed non-callable argument to main function")
    print("inside caller function")

def disp():
    print("inside disp function")

main(disp)    # works
temp=100
main(temp)    # you won't get TypeError

