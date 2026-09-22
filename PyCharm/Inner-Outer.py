def outer():
    print("HI") #1st execute
    def inner():
        print("HELLO") #3rd execute
    print("BYE") #2nd execute
    return inner
outer()()