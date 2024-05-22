import numbers

def numbers_sum():
    numbersAmount = int(input("Enter the amount of numbers: "))
    sum = 0
    for _ in range(numbersAmount):
        number = int(input("Enter a random number: "))
        sum += number
    return sum
# Feedback 1 (Lucas): Voeg foutafhandeling toe voor ongeldige gebruikersinvoer.
# Feedback 2 (Uliana): Gebruik een duidelijkere variabelenaam dan "sum" om verwarring met de ingebouwde functie te vermijden.

def multiply_numbers(*args):
    total = 1
    for num in args:
        if isinstance(num, numbers.Number):
            total *= float(num)
        else:
            print(f"{num} is no number, so it will be ignored!")
    return total
# Feedback 1: Voeg error handling toe om ongeldige invoer te verwerken bij het omzetten naar float.
# Feedback 2: Gebruik expliciete typecontrole om onverwachte invoertypes te vermijden.

def main():
    print(multiply_numbers(1.5, 2.0, 98.6, "asd"))