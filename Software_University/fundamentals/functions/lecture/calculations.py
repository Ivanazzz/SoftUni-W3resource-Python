operator = input("Enter(multiply, divide, add, subtract): ")
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

def calculator(operator, first_number, second_number):
    if operator == "multiply":
        result = first_number * second_number
        return result
    elif operator == "divide":
        result = first_number / second_number
        return result
    elif operator == "add":
        result = first_number + second_number
        return result
    elif operator == "subtract":
        result = first_number - second_number
        return result
        
print(calculator(operator, first_number, second_number))