print("==================")
print("    RANA'S ATM    ")
print("==================")

input("Please insert your card and press Enter once inserted>>")

correct_pin = 1234
balance = 5000
while True:
    pin = int(input("Enter your PIN:"))
    if pin == correct_pin:
        print("PIN verified successfully")
        break
    else:
        print("Incorrect PIN! Please insert correct PIN")

while True:
    print("\nMain MENU>")
    print("1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Cash")
    print("4. Fund Transfer")
    print("5. Change PIN")
    print("6. Help")
    print("7. Exit")

    option = int(input("Enter your option:"))

    if option == 1:
        print("Your Balance is:",balance)
        input("\nPress Enter to main menu>>")
    elif option == 2:
        amount = int(input("Enter withdrawal amount:"))
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
            print("Your remaining Balance is:",balance)
            input("\nPress Enter to main menu>>")
        else:
            print("Insufficient funds")
            input("\nPress Enter to main menu>>")
    elif option == 3:
        amount = int(input("Enter deposit amount:"))
        balance = balance + amount
        print("Deposit successful")
        print("Your Balance is:",balance)
        input("\nPress Enter to main menu>>")
    elif option == 4:
        account_no = input("Enter recipient account number:")
        transfer_amount = int(input("Enter transfer amount:"))
        if transfer_amount <= balance:
            balance = balance-transfer_amount
            print(f"Transfer successful {transfer_amount} to Account: {account_no}")
            print("Your Your Balance is:",balance)
            input("\nPress Enter to main menu>>")
        else:
            print("Insufficient funds for transfer")
            input("\nPress Enter to main menu>>")
    elif option == 5:
        current_pin = int(input("Enter your current PIN:"))
        if current_pin == correct_pin:
            new_pin = int(input("Enter new 4-digit PIN:"))
            confirm_pin = int(input("Confirm new PIN:"))
            if new_pin == confirm_pin:
                confirm_pin = new_pin
                print("PIN successfully changed")
                input("\nPress Enter to main menu>>")
            else:
                print("New PIN and Confirm PIN are different")
                input("\nPress Enter to main menu>>")
        else:
            print("Incorrect current PIN")
            input("\nPress Enter to main menu>>")
    elif option == 6:
        print("\n--- HELP & SUPPORT ---")
        print("1. Helpline: 16216 / +8809666716216")
        print("2. Daily withdrawal limit: 20000")
        print("3. For card swallowed or transaction issues, contact branch manager immediately")
        print("4. Email: support@ranasatm.com")
        input("\nPress Enter to main menu>>")

    elif option == 7:
        print("Please collect your card")
        print("Thank you for using RANA'S ATM")
        break
    else:
     print("Invalid option")
     input("\nPress Enter to main menu>>")