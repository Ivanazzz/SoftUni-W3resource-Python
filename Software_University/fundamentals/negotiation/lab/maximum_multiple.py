first_number = int(input("Enter the first number(divisor): "))
second_number = int(input("Enter the second number(boundary): "))

for number in range(second_number, 0, -1):
    if number % first_number == 0:
        print(number)
        break
