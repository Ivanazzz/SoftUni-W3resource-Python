count_of_number = int(input("Enter the count of numbers: "))
even_sum = 0
odd_sum = 0
for i in range(count_of_number):
    user_input = int(input("Enter number: "))
    if i % 2 == 0:
        even_sum += user_input
    else:
        odd_sum += user_input

if even_sum == odd_sum:
    print(f"Yes \nSum = {even_sum}")
else:
    print(f"No \nDiff = {abs(even_sum - odd_sum)}")
