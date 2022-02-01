days = int(input())
total_amount_of_food = float(input())

eaten_food_dog_gr = 0
eaten_food_cat_gr = 0
total_amount_of_eaten_food = 0
biscuits_gr = 0

for day in range(1, days + 1):
    amount_eaten_dog_food = int(input())
    amount_eaten_cat_food = int(input())
    eaten_food_dog_gr += amount_eaten_dog_food
    eaten_food_cat_gr += amount_eaten_cat_food
    total_amount_of_eaten_food += amount_eaten_dog_food + amount_eaten_cat_food

    if day % 3 == 0:
        biscuits_gr += (amount_eaten_dog_food + amount_eaten_cat_food) * 0.1

total_eaten_food_percent = total_amount_of_eaten_food / total_amount_of_food * 100
eaten_food_by_dog_percent = eaten_food_dog_gr / total_amount_of_eaten_food * 100
eaten_food_by_cat_percent = eaten_food_cat_gr / total_amount_of_eaten_food * 100

print(f"Total eaten biscuits: {round(biscuits_gr)}gr.")
print(f"{total_eaten_food_percent:.2f}% of the food has been eaten.")
print(f"{eaten_food_by_dog_percent:.2f}% eaten from the dog.")
print(f"{eaten_food_by_cat_percent:.2f}% eaten from the cat.")