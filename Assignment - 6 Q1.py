class PasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        if self.old_passwords:
            return self.old_passwords[-1]
        else:
            return None

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("Password changed successfully!")
        else:
            print("Error: The new password must be different from all previous passwords")

    def is_correct(self, password_to_check):
        return password_to_check == self.get_password()

password_manager = PasswordManager()

while True:
    print("\nPassword Manager")
    print("1. Set a new password")
    print("2. Get the current password")
    print("3. Check if a password is correct")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        new_password = input("Enter a new password: ")
        password_manager.set_password(new_password)
    
    elif choice == "2":
        current_password = password_manager.get_password()
        if current_password:
            print(f"The current password is: {current_password}")
        else:
            print("No password set yet.")
    
    elif choice == "3":
        password_to_check = input("Enter the password to check: ")
        if password_manager.is_correct(password_to_check):
            print("Password is correct!")
        else:
            print("Incorrect password.")
    
    elif choice == "4":
        print("Exiting Password Manager.")
        break
    
    else:
        print("Invalid choice, please try again.")
