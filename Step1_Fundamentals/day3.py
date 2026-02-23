name = input("Enter your name: ")
balance =2000

print("/n Welcome to the bank, " + name + "!")

while True:
    print("\nWhat would you like to do?")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ${balance}")
    elif choice == "2":
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"You have deposited ${amount}. Your new balance is: ${balance}")
    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"You have withdrawn ${amount}. Your new balance is: ${balance}")
    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")