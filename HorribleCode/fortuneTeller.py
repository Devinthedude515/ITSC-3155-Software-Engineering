#import fortune class to use
from fortune import Customer

#have the user enter their name, age, birth month, and day of week born on
name = input("What is your name? ")
age = input(f"How old are you? ")
month = input("What month were you born? ")
day = input("What day of the week were you born? ")

#create customer object with gathered data
customer = Customer(name, age, month, day)

#print the customer's month fortune
print(customer.print_name())
print(customer.age_fortune())
print(customer.month_fortune())
print(customer.day_of_week())

