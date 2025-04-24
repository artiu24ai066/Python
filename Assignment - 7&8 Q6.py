class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")



    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

def user_input():
    account_number = input("Enter your account number: ")
    account = BankAccount(account_number)

    while True:
        print("\nChoose an option:")
        print("1. Deposit funds")
        print("2. Withdraw funds")
        print("3. Display account details")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)

        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)

        elif choice == '3':
            account.display()

        elif choice == '4':
            print("Exiting the Bank Account system.")
            break
        
user_input()
