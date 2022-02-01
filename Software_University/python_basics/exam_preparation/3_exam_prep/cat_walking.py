minutes_walk_per_day = int(input())
walks_count = int(input())
consumed_calories = int(input())

total_min = minutes_walk_per_day * walks_count
calories_burned = total_min * 5

half_consumed_calories = consumed_calories / 2

if calories_burned >= half_consumed_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")