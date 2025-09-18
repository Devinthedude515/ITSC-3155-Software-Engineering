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

        #create method to withdraw from account if limit is not reached
        def withdraw(self, amount):
            while True:
                if amount is None:
                    amount = float(input("Enter withdrawal amount: "))
        #create method to discern if user has enough to withdraw
        if 0 <= amount <= self.overdraft_limit:
            if self.balance - amount >= -self.__transfer_limit:
                self._balance -= amount
                print(f"Withdrawal of ${amount:.2f} successfully!")
                print(f"New balance of account {self.name} is: ${self.balance:.2f}")
            else:
                print("Transaction cancelled! Withdrawal limit reached.")
        else:
            print("Transaction cancelled! Withdrawal limit reached.")
        #prompt user to enter again
        amount = float(input("Enter withdrawal amount: "))