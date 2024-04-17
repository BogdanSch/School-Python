def numbers_sum():
    numbersAmount = int(input("Enter the amount of numbers: "))
    sum = 0

    for _ in range(numbersAmount):
        number = int(input("Enter a random number: "))
        sum += number
    
    return sum

def multiply_numbers(*args):
    total = 1
    for num in args:
        if isinstance(num, float):
            total *= num
        else:
            print("Warning: Non-float value detected and ignored.")
    return total

def main():
    print(multiply_numbers(1.5, 2.0, 98.6))