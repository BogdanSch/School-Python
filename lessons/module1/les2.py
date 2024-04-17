def find_average():
    numbers = str(input("Enter 5 number, separated them with a comma: ")).split(", ")
    numbers = [int(num) for num in numbers]
    average = sum(numbers) / len(numbers) 
    return average

def calculate_age():
    birthyear = int(input("Enter your birthyear: "))
    currentYear = int(input("Enter the current year: "))

    age = currentYear - birthyear
    return f"Your age: {age}"


def main():
    return calculate_age()