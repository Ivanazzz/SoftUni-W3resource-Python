first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

for number in range(first_number, second_number + 1):
    odd_digits_sum = 0
    even_digits_sum = 0
    for index, digit in enumerate(str(number)):
        digit = int(digit)
        if (index + 1) % 2 != 0:
            odd_digits_sum += digit
        else:
            even_digits_sum += digit
        
    if odd_digits_sum == even_digits_sum:
        print(number)
            
