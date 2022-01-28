power_number = int(input("Enter an integer number: "))
for number in range(0, power_number + 1, 2):
    even_power_of_two = 2 ** number
    print(even_power_of_two)