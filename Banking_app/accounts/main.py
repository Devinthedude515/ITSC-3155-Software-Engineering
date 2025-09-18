#import the database of accounts
from Bank_Account import BankAccount
from checking_account import CheckingAccount
from savings_account import SavingsAccount
from data import accounts_db

#Menu loop
while True:
    #welcome user to the app and prompt for account number
    print("---Banking Made Easy---")
    account_number = input("Enter you account number:")
    account = accounts_db.get(account_number)

    #if account number not found
    if not account:
        print("Invalid account number")
        continue

    #create menu options
    print("Enter your choice:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Account Info")
    print("4. Apply Interest (Savings only)")
    print("5. Exit")
    choice = int(input())
    if choice == 1:
        amount = float(input("Enter deposit amount $(0 - 300): "))
        #ensure this is a checking account
        if isinstance(account, CheckingAccount):
            #validate the amount is within transfer limit
            validate = account.transaction_limit(amount)
            account.deposit(validate)
        else:
            #must be checking
            print("Invalid account type. Must be checking")
    elif choice == 2:
        amount = float(input("Enter withdraw amount $(0 - 300): "))
        # validate the amount is within transfer limit
        if isinstance(account, CheckingAccount):
            validate = account.transaction_limit(amount)
            account.withdraw(validate)
        else:
            #must be checking
            print("Invalid account type. Must be checking")
    elif choice == 3:
        account.print_customer_info()
    elif choice == 4: #apply interest to savings account
        #Ensure this is a savings account
        if isinstance(account, SavingsAccount):
           rate = account.get_rate()
           print(f"Interest rate: {rate*100:.2f}%")
           #prompt user to enter amount to add and apply interest
           amount = float(f"Enter amount to apply interest and deposit: ")
           # validate the amount is within transfer limit
           account.add_interest(amount)
        else:
            print("Option only available for savings accounts")
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
