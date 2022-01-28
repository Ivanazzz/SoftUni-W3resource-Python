number_amount = int(input("Enter amount of the numbers: "))
first_counter = 0
second_counter = 0
third_counter= 0 
fourth_counter = 0
fifth_counter = 0

for i in range(number_amount):
    user_input_number = int(input("Enter number: "))
    if user_input_number < 200:
        first_counter += 1
    elif 200 <= user_input_number <= 399:
        second_counter += 1
    elif 400 <= user_input_number <= 599:
        third_counter += 1
    elif 600 <= user_input_number <= 799:
        fourth_counter += 1
    elif user_input_number >= 800:
        fifth_counter += 1

percent_one = first_counter / number_amount * 100
percent_two = second_counter / number_amount * 100
percent_three = third_counter / number_amount * 100
percent_four = fourth_counter / number_amount * 100
percent_five = fifth_counter / number_amount * 100
print(f"{percent_one:.2f}%")
print(f"{percent_two:.2f}%")
print(f"{percent_three:.2f}%")
print(f"{percent_four:.2f}%")
print(f"{percent_five:.2f}%")