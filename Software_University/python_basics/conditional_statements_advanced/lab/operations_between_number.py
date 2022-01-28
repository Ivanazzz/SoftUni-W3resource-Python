first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operation = input("Choose operation(+, -, *, /, %): ")
result = 0

if operation == "+" or operation == "-" or operation == "*":
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    if result % 2 == 0:
        print(f"{first_number} {operation} {second_number} = {result} - even")
    else:
        print(f"{first_number} {operation} {second_number} = {result} - odd")

elif operation == "/" or operation == "%":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    elif operation == "/":
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result:.2f}")
    elif operation == "%":
        result = first_number % second_number
        print(f"{first_number} % {second_number} = {result}")