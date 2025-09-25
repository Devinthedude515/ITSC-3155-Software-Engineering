from fortune import Customer

#create a loop to keep making fortunes
while True:
    # have the user enter their name, age, birth month, and day of week born on
    name = input("What is your name? ")
    age = input(f"How old are you? ")
    month = input("What month were you born? ")
    day = input("What day of the week were you born? ")

    #create object and fill in attributes
    customer = Customer(name, age, month, day)

    #print the fortunes
    # print the customer's month fortune
    customer.print_name()
    print(customer.age_fortune())
    print(customer.month_fortune())
    print(customer.day_of_week())

    choice = input("Would you like to continue? (Y/N): ")
    if choice == "Y" or choice == "y":
        continue
    elif choice == "N" or choice == "n":
        break

