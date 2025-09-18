#import the BankAccount class to inherit
from Bank_Account import BankAccount

#create a subclass that is a savings account with interest
class SavingsAccount(BankAccount):
    #create constructor with two variables routing and account number
    def __init__(self, name, balance, min_balance, routing_number, account_number, interest_rate):
        # call to super to inherit BankAccount attributes
        super().__init__(name, balance, min_balance)
        #assign variables to constructor for calls
        self.routing_number = routing_number
        self.account_number = account_number
        self.interest_rate = interest_rate
    #create a method to add interest to a given account
    def add_interest(self, amount):
        if amount > 0:
            interest = amount * self.interest_rate
            total = amount + interest
            self._balance += total
            print(f"Interest: ${interest:.2f}")
            print(f"New balance: ${self._balance:.2f}")
        else:
            print("Not enough money!")

    #create getter to grab interest rate
    def get_rate(self):
        return self.interest_rate