#must create a bank class
class BankAccount:
    #create method for customer name, current balance, and minimum balance
    def __init__(self, name, balance, min_balance):
        self.name = name
        self._balance = balance
        self.min_balance = min_balance
    #create a deposit method that updates the current balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposit successful. New balance: ${self._balance:.2f}")
        #deposit fails
        else:
            print("Deposit Failed.")
    #create a withdrawal method that updates the current balance
    def withdraw(self, amount):
      #ensure that current balance is more than min balance
      if 0 < amount <= self._balance:
          self._balance -= amount
          print(f"Withdraw successful. New balance: ${self._balance:.2f}")
        #withdraw fails
      else:
          print("Withdraw Failed.")

    #create method to display all customer data including class name
    def print_customer_info(self):
        print("----Account Details----")
        print(f"Name: {self.name}")
        print(f"Current Balance: {self._balance}")

    #create getter to grab the balance
    def get_balance(self):
        return self._balance
