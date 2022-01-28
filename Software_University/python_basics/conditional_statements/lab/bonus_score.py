number = int(input("Enter number: "))

first_bonus = 0

if number <= 100:
    first_bonus += 5
elif number < 1000:
    first_bonus = number * 0.2
elif number > 1000:
    first_bonus = number * 0.1

second_bonus = 0

if number % 2 == 0:
    second_bonus += 1
elif number % 10 == 5:
    second_bonus += 2

total_bonus = first_bonus + second_bonus
bonus_plus_number = number + total_bonus

print(total_bonus)
print(bonus_plus_number)