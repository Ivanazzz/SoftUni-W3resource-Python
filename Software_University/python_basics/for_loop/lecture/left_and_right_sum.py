count_of_number = int(input("Enter the number quantity: "))
left_sum = 0
right_sum = 0
for i in range(count_of_number * 2):
    user_input = int(input("Enter number: "))
    if i < count_of_number:
        left_sum += user_input
    else:
        right_sum += user_input

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")

