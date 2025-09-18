#import the BankAccount class to inherit
from Bank_Account import BankAccount

#create a subclass that is a Checking account with transfer limitations
class CheckingAccount(BankAccount):
    # create constructor with two variables routing and account number
    def __init__(self, name, balance, min_balance, routing_number, account_number, transfer_limit):
        #call to super to inherit BankAccount attributes
        super().__init__(name, balance, min_balance)
        # assign variables to constructor for calls
        self._routing_number = routing_number
        self.__account_number = account_number
        self.__transfer_limit = transfer_limit

    #create method to check that amount is within limit
    def transaction_limit(self, amount):
        while not (0 < amount <= self.__transfer_limit):
            print(f"Invalid transfer amount. Please try again")
            amount = float(input("Enter amount $(0 - 300): "))
        return amount
