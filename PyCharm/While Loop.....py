# Series print
def program_1():
    count = 1
    while count<=5:
        print("number", count)
        count += 1

# 1-10 all even number
def program_2():
    i=2
    while i<=10:
        print(i)
        i+=2

# Password until correct
def program_3():
    password=""
    while password!="1234":
        password=input("enter your password: ")
    print("password Correct")

# using break
def program_4():
    i=1
    while i<=10:
        if i==9:
            print("9 found, loop broken")
            break
        print(i)
        i+=1

# Continue using
def program_5():
    i=0
    while i<10:
        i+=1
        if i==3:
            continue
        print(i)


program_5()
