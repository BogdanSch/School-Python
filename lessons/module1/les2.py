def find_average():
    numbers = str(input("Enter 5 number, separated them with a comma: ")).split(", ")
    numbers = [float(num) for num in numbers]
    average = sum(numbers) / len(numbers) 
    return average
    # Uliana: Ik vind deze code wel goed, maar ik zou er ook een fouthandeling toegoeven om te checken wat gebruiker heeft ingetypt.
    # Ada: Het programma berekent correct het gemiddelde van de getallen, maar het zou optimaler zijn met verbeterde gebruikersinstructies: "Enter 5 number and separate them with a comma and whitespace: ".

def calculate_age():
    birthyear = int(input("Enter your birthyear: "))
    currentYear = int(input("Enter the current year: "))

    age = currentYear - birthyear
    return f"Your age: {age}"
    # Uliana: De code lijkt correct voor het berekenen van leeftijden, maar het zou beter zijn met ttoevoeging van foutafhandeling als currentYear < dan birthyear.
    # Ada: Ik vind de werking van deze code wel goede en het maakt goed zijn doel.

def main():
    return calculate_age()