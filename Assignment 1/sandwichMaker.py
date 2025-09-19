### Data ###
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Apologies, we are out of items")
                return False
            return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        quarters = int(input("How many large dollars?: "))
        dimes = int(input("How many half dollars?: ")) * 0.5
        nickles = int(input("How many quarters?: ")) * 0.25
        pennies = int(input("How many nickel?: ")) * 0.05
        total = quarters + dimes + nickles + pennies
        print(f"You have ${total:.2f} in total.")
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"You have ${change:.2f} of ${coins:.2f}.")
                print("Payment is accepted.")
                return True
        else:
            print("You don't have enough money.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]

#Make an instance of the Sandwich class
machine = SandwichMachine(resources)

#prompt the user for what size sandwich they want small, medium, or large
#Ensure there is sufficient amount of ingredients
while True:
    # use constructor to pass in resources for user's choice
    sandwich_size = (input("What would you like? (small/ medium/ large/ off/ report): "))

    if sandwich_size in recipes:
        sandwich = recipes[sandwich_size]
        ingredients = sandwich["ingredients"]
        cost = sandwich["cost"]

        if machine.check_resources(ingredients):
            payment = machine.process_coins()
            if machine.transaction_result(payment, cost):
                machine.make_sandwich(sandwich_size, ingredients)
                #let user know the sandwich size of choice is ready
                print(f"Here is your {sandwich_size} sandwich. Enjoy!")
    #use else statement and if report print the current resources
    elif sandwich_size == "report":
        print("Current Resources:")
        for item, amount in machine.machine_resources.items():
            print(f"{item}: {amount}")
            #line to separate loop
            print("--------------------")
    #use else to break from loop if user types off
    elif sandwich_size == "off":
        break

