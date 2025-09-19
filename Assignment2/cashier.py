class Cashier:
    def __init__(self):
        pass

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
