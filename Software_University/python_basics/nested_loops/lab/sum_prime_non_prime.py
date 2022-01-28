command = input("Enter number or 'stop' to quit: ")
prime_numbers_sum = 0
non_prime_numbers_sum = 0

while command != "stop":
    is_prime = True
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
        command = input("Enter number or 'stop' to quit: ")
        continue
    
    for number in range(2, current_number):
        if current_number % number == 0:
            is_prime = False
            
    if is_prime:
        prime_numbers_sum += current_number
    else:
        non_prime_numbers_sum += current_number
        
    command = input("Enter number or 'stop' to quit: ")
    
print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")