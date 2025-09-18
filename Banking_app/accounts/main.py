#import the database of accounts
from data import accounts_db

#Menu loop
while True:
    #welcome user to the app and prompt for account number
    print("---Banking Made Easy---")
    account_number = input("Enter you account number:")
    account = accounts_db.get_account(account_number)

    #create menu options
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
