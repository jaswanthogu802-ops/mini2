balance = 10000
pin = 1234

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Please collect your cash")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Amount deposited successfully")
        print("Updated balance:", balance)

    elif choice == 4:
        print("Thank you! Visit again")

    else:
        print("Invalid choice")

else:
    print("Wrong PIN")
