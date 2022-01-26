# Task 1
# Write a Python program to check if a given positive integer is a power of two.
# Input : 4  Output : True

def power_of_two():
    number = int(input("Enter a number to check if it is a power of two: "))
    if number >= 2:
        while number > 1:
            number = number / 2
            if number == 1:
                return True
            elif number != 0:
                continue
        if number < 1:
            return False
    elif number == 1:
        return True
    elif number < 0:
        return "The number you entered must be positive"


print(power_of_two())
