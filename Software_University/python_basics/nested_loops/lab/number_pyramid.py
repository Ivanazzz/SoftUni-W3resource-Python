number = int(input("Enter number: "))
current = 1
current_equal_to_number = False

for row in range(1, number + 1):
    for col in range(1, row + 1):
        current += 1
        print(current, end = " ")
        if current == number:
            current_equal_to_number = True
            break
    if current_equal_to_number:
        break
    print()