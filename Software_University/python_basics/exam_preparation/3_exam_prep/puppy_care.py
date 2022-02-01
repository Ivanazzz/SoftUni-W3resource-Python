bought_dogs_food_kg = int(input())
bought_dogs_food_gr = bought_dogs_food_kg * 1000
total_eaten_food = 0

while True:
    eaten_food_gr = input()
    if eaten_food_gr == "Adopted":
        break
    eaten_food_gr = int(eaten_food_gr)
    total_eaten_food += eaten_food_gr

if bought_dogs_food_gr >= total_eaten_food:
    print(f"Food is enough! Leftovers: {bought_dogs_food_gr - total_eaten_food} grams.")
else:
    print(f"Food is not enough. You need {total_eaten_food - bought_dogs_food_gr} grams more.")