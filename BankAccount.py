#must create a bank class
class BankAccount:
    #create method for customer name, current balance, and minimum balance
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = balance
    #create a deposit method that updates the current balance
    def deposit(self, amount):
        self.balance += amount
    #create a withdraw method that updates the current balance
    def withdraw(self, amount):
      #ensure that current balance is more than min balance
      if self.balance - amount < self.min_balance:
          print("Not enough money!")
      else:
          self.balance -= amount
          print(f"Withdrew ${amount}. Money ${self.balance}")
    #create method to display all customer data including class name
    def print_customer_info(self):
        print("----Give Me Your Money United----")
        print(f"Name: {self.name}")
        print(f"Current Balance: {self.balance}")
#create a subclass that is a savings account with interest
class SavingsAccount(BankAccount):
    #create constructor with two variables routing and account number
    def __init__(self, routing_number, account_number, interest):
        #assign variables to constructor for calls
        self._routing_number = routing_number
        self.__account_number = account_number
        self.__interest = interest

#create a subclass that is a Checking account with transfer limitations
class CheckingAccount(BankAccount):
    # create constructor with two variables routing and account number
    def __init__(self, routing_number, account_number, transfer_limit):
        # assign variables to constructor for calls
        self._routing_number = routing_number
        self.__account_number = account_number
        self.__transfer_limit = transfer_limit

#collect name and balance
name = input("Enter your name: ")
balance = float(input("Enter your balance: "))

#create an account with data
account = BankAccount(name, balance, min_balance=balance)
account1 = BankAccount(name, balance, min_balance=balance)

#Menu loop
while True:
    #create menu options
    print("Account 1")
    print("Enter your choice:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Account Info")
    print("4. Exit")
    choice = int(input())
    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter withdraw amount: "))
        account.withdraw(amount)
    elif choice == 3:
        account.print_customer_info()
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")

#Menu loop
while True:
    #create menu options
    print("Account 1")
    print("Enter your choice:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Account Info")
    print("4. Exit")
    choice = int(input())
    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        account1.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter withdraw amount: "))
        account1.withdraw(amount)
    elif choice == 3:
        account1.print_customer_info()
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")

