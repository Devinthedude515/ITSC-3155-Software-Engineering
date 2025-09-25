class Customer:

    def __init__(self, name, age, birth_month, birth_day):
        self.name = name
        self.age = age
        self.birth_month = birth_month
        self.birth_day = birth_day


    #create a method that gets the user's birth month
    def get_month(self):
        return self.birth_month
    #create method that gets the users day of the week born on
    def get_day(self):
        return self.birth_day
    #create method to get the name
    def get_name(self):
        return self.name
    #create method to get the age
    def get_age(self):
        return self.age

    #create method to print out a fortune based on zodiac sign
    def month_fortune(self):
        zodiac = self.get_month()
        zodiac = zodiac.lower()
        #create if/else chain of all zodiac signs and associated fortunes
        if zodiac == "january":
            return "You’ll find energy for new challenges today."
        elif zodiac == "february":
            return "Patience will reward you soon."
        elif zodiac == "march":
            return "Communication opens a new door for you."
        elif zodiac == "april":
            return "Stay close to family, they bring comfort."
        elif zodiac == "may":
            return "Your confidence will inspire others."
        elif zodiac == "june":
            return "Focus on details, success lies there."
        elif zodiac == "july":
            return "Balance will bring peace to your decisions."
        elif zodiac == "august":
            return "Intense focus will lead you forward."
        elif zodiac == "september":
            return "Adventure is calling — embrace it!"
        elif zodiac == "october":
            return "Your creativity shines bright today."
        elif zodiac == "november":
            return "Your empathy will guide you to help others."
        elif zodiac == "december":
            return "The road that ends is where your journey begins."
        else:
            return "Not a valid zodiac sign or month."

    #create method to get day person was born
    def day_of_week(self):
        day = self.get_day()
        day = day.lower()
        if day == "monday" or day == "mon":
            return "A fresh start awaits — set the tone for the week!"
        elif day == "tuesday" or day == "tue":
            return "Your determination today will pay off tomorrow."
        elif day == "wednesday" or day == "wed":
            return "Midweek clarity helps you solve a lingering problem."
        elif day == "thursday" or day == "thurs":
            return "Stay focused — an opportunity is right around the corner."
        elif day == "friday" or day == "fri":
            return "Celebrate progress, no matter how small."
        elif day == "saturday" or day == "sat":
            return "Relax and recharge — joy is found in simple things."
        elif day == "sunday" or day == "sun":
            return "Reflection today will bring peace for the week ahead."
        else:
            return "Not a valid day."

    #create a method to give a fortune based on age
    def age_fortune(self):
        age = int(self.get_age())
        if 5 < age <= 18:
            return "You're journey has just begun, even when it didn't feel fun"
        elif 18 < age <= 30:
            return "Feathers fall in the most mysterious ways, be weightless and on your path you will stay"
        elif 30 < age <= 55:
            return "The destination is soon to be reached, remember those who sleep beneath"
        elif 55 < age <= 65:
            return "Time has taken its toll, for you I hope it was not droll"
        elif 65 < age <= 90:
            return "Congrats on making it to the end, do you think you will ride again?"
        else:
            return "Not a valid age."

    #get method to print the name
    def print_name(self):
        print(self.get_name())



