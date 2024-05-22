def get_discount():
    places = {
        "walibi": (10, "You won't get the discount!"),
        "slagharen": (5, 10, "You won't get the discount!")
    }
    place = input("Would you like to go (Walibi) of (Slagharen): ").strip().lower()
    amountPeople = int(input("How many people would you like to go with: "))

    if place in places:
        discounts = places[place]
        if len(discounts) == 2:
            if amountPeople >= discounts[0]:
                print("You get a discount!")
            else:
                print("You won't get the discount!")
        elif len(discounts) == 3:
            if amountPeople >= discounts[0] and amountPeople <= discounts[1]:
                print("You get a discount!")
            else:
                print("You won't get the discount!")
    else:
        print("Sorry, try again later!")

# Feedback 1 (Alex): Voeg inputvalidatie toe om gebruikersinvoer beter te maken.
# Feedback 2 (Silvio): Gebruik benoemde variabelen om de leesbaarheid van je code te verbeteren.
def main():
    get_discount()