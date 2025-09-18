#must create a bank class
class BankAccount:
    #create method for customer name, current balance, and minimum balance
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
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

#collect name and balance
name = input("Enter your name: ")
balance = float(input("Enter your balance: "))
