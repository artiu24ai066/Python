class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance=0):
        self.accounts[name] = balance
        print(f"Account created for {name} with balance {balance}")

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
            print(f"Deposited {amount}. New balance: {self.accounts[name]}")
        else:
            print("Account not found.")

    def withdraw(self, name, amount):
        if name in self.accounts:
            if self.accounts[name] >= amount:
                self.accounts[name] -= amount
                print(f"Withdrew {amount}. New balance: {self.accounts[name]}")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

    def check_balance(self, name):
        if name in self.accounts:
            print(f"{name}'s balance: {self.accounts[name]}")
        else:
            print("Account not found.")

def user_input():
    bank = Bank()

    while True:
        print("\nChoose an option:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            name = input("Enter customer name: ")
            balance = float(input("Enter initial balance: "))
            bank.create_account(name, balance)

        elif choice == '2':
            name = input("Enter customer name: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(name, amount)

        elif choice == '3':
            name = input("Enter customer name: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(name, amount)

        elif choice == '4':
            name = input("Enter customer name: ")
            bank.check_balance(name)

        elif choice == '5':
            print("Exiting the bank system...")
            break

        else:
            print("Invalid choice, please try again...")

user_input()
