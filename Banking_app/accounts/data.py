from checking_account import CheckingAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount

#create database and store accounts
accounts_db = {
    #create accounts to verify to store in database
    "67890": SavingsAccount("Devin", 200, 200, "12345", "67890", 0.1),
    "191919": CheckingAccount("Keiron", 345, 345, "454545", "191919", 300),
    "737373": CheckingAccount("Sage", 400, 400, "646464", "737373", 300)
}