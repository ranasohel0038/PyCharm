print("==================")
print("    RANA'S ATM    ")
print("==================")

correct_pin = 1234
balance = 5000

pin=int(input("Enter your pin:"))
if pin == correct_pin:
 while True:
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Cash")
    print("4. Exit")

    option = int(input("Enter your option:"))

    if option == 1:
        print("Your Balance is:",balance)
        input("\nPress Enter to main menu")
    elif option == 2:
        amount = int(input("Enter withdrawal amount:"))
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
            print("Your remaining Balance is:",balance)
        else:
            print("Insufficient funds")
            input("\nPress Enter to main menu")
    elif option == 3:
        amount = int(input("Enter deposit amount:"))
        balance = balance + amount
        print("Deposit successful")
        print("Your Balance is:",balance)
        input("\nPress Enter to main menu")
    elif option == 4:
        print("Thank you for using RANA'S ATM")
        break
    else:
     print("Invalid option")
     input("\nPress Enter to main menu")
else:
    print("Wrong Pin")