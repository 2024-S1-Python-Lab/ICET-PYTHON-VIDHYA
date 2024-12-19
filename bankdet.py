class Bank:
    def __init__(self, accno, name, acctype, balance=0):
        self.acc = accno
        self.na = name
        self.acctype = acctype
        self.bal = balance

    def deposit(self, amount):
        if amount > 0:
            self.bal += amount
            print(f"Deposit successful. New balance: {self.bal}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.bal:
                self.bal -= amount
                print(f"Withdrawal successful! New balance: {self.bal}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def display(self):
        print(f"\nAccount Number: {self.acc}")
        print(f"Account Holder Name: {self.na}")
        print(f"Account Type: {self.acctype}")
        print(f"Balance: {self.bal}")
        print("\n*** Menu ***")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display")
        print("4. Exit")
b1 = Bank(1002, "Win", "Savings", 0)
b1.display()
while True:
    choice = int(input("\nEnter your choice (1-4): "))
    if choice == 1:
        d = int(input("\nEnter amount to be deposited: "))
        b1.deposit(d)
    elif choice == 2:
        w = int(input("Enter amount to withdraw: "))
        b1.withdraw(w)
    elif choice == 3:
        b1.display()
    elif choice == 4:
        print("Exiting... Thank you!")
        break
    else:
        print("Enter a valid choice.")
