'''1.Bank Account Management System
You are tasked with creating a simple bank account management system in Python.
Implement a class called BankAccount with the following specifications:
The class should have private instance variables for account number, account holder
name, and balance.
Include a constructor to initialize these variables.
Implement getter and setter methods for each instance variable to ensure encapsulation.
Implement methods to deposit and withdraw money from the account.
Ensure that the withdraw method checks if the account has sufficient balance before
allowing withdrawal.
Write a Python program to demonstrate the functionality of the BankAccount class by
creating instances, depositing and withdrawing money, and displaying account
information.'''

class BankAccount:
    # Constructor
    def __init__(self, account_number, account_holder_name, balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = balance

    # Getters
    def get_account_number(self):
        return self.__account_number

    def get_account_holder_name(self):
        return self.__account_holder_name

    def get_balance(self):
        return self.__balance

    # Setter
    def set_account_holder_name(self, name):
        self.__account_holder_name = name

    # Deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    # Withdraw
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    # Display info
    def display_info(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.__account_number)
        print("Account Holder:", self.__account_holder_name)
        print("Balance:", self.__balance)


# -------- Main Program --------
print("=== Bank Account System ===")
acc_no = int(input("Enter account number: "))
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(acc_no, name, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Details")
    print("4. Change Name")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)
    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif choice == "3":
        account.display_info()
    elif choice == "4":
        new_name = input("Enter new name: ")
        account.set_account_holder_name(new_name)
        print("Name updated")
    elif choice == "5":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice, try again")
