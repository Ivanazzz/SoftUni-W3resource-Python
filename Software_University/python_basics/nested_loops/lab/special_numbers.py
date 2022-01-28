number = int(input("Enter number: "))

for num in range(1111, 9999 + 1):
    is_special = True
    for digit in str(num):
        digit = int(digit)
        if (digit == 0) or (number % digit !=0):
            is_special = False
            break
        
    if is_special:
        print(num)