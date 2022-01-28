number_amount = int(input("Enter the amount of numbers: "))
user_input_list = []
number_sum = 0

for i in range(0, number_amount):
    number = int(input("Enter number: "))
    user_input_list.append(number)
    number_sum += number

max_num = max(user_input_list)
number_sum = number_sum - max_num
if number_sum == max_num:
    print(f"Yes \nSum = {number_sum}")
else:
    difference = abs(max_num - number_sum)
    print(f"No \nDiff = {difference}")
