user_input = int(input("Enter number: "))
combinations = 0

for first_num in range(user_input + 1):
    for second_num in range(user_input + 1):
        for third_num in range(user_input + 1):
            if first_num + second_num + third_num == user_input:
                combinations += 1

print(combinations)