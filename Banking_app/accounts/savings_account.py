#import the BankAccount class to inherit
from Bank_Account import BankAccount

#create a subclass that is a savings account with interest
class SavingsAccount(BankAccount):
    #create constructor with two variables routing and account number
    def __init__(self, name, balance, min_balance, routing_number, account_number, interest):
        # call to super to inherit BankAccount attributes
        super().__init__(name, balance, min_balance)
        #assign variables to constructor for calls
        self._routing_number = routing_number
        self.__account_number = account_number
        self.__interest = interest
    #create a method to add interest to a given account
    def add_interest(self, interest):
        self._balance += self._balance * self.interest_rate
        return self._balance


