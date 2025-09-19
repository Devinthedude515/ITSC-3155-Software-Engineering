from Assignment2 import data
from cashier import Cashier
from sandwich_maker import SandwichMaker

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    while True:
        # use constructor to pass in resources for user's choice
        sandwich_size = (input("What would you like? (small/ medium/ large/ off/ report): "))
        #check that the size is in recipes
        if sandwich_size in recipes:
            #assign values from data file
            sandwich = recipes[sandwich_size]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]
            #make sure that we have enough resources ad process payment
            if sandwich_maker_instance.check_resources(ingredients):
                payment = cashier_instance.process_coins()
                #print the result of the transaction and deliver the sandwich
                if cashier_instance.transaction_result(payment, cost):
                    sandwich_maker_instance.make_sandwich(sandwich_size, ingredients)
                    # let user know the sandwich size of choice is ready
                    print(f"Here is your {sandwich_size} sandwich. Enjoy!")
        # use else statement and if report print the current resources
        elif sandwich_size == "report":
            print("Current Resources:")
            #check resources quantity in sandwich instance
            for item, amount in sandwich_maker_instance.machine_resources.items():
                print(f"{item}: {amount}")
                # line to separate loop
                print("--------------------")
            # use else to break from loop if user types off
        elif sandwich_size == "off":
            #say goodbye
            print("Goodbye! Thank you!")
            break
if __name__ == "__main__":
    main()