sold_games_count = int(input())

hearthstone_count = 0
fornite_count = 0
overwatch_count = 0
others_count = 0
total_games_count = 0

for game in range(sold_games_count):
    games_name = input()
    if games_name == "Hearthstone":
        hearthstone_count += 1
    elif games_name == "Fornite":
        fornite_count += 1
    elif games_name == "Overwatch":
        overwatch_count += 1
    else:
        others_count += 1
    total_games_count += 1

hearthstone_percentage = hearthstone_count / total_games_count * 100
fornite_percentage = fornite_count / total_games_count * 100
overwatch_percentage = overwatch_count / total_games_count * 100
others_percentage = others_count / total_games_count * 100

print(f"Hearthstone - {hearthstone_percentage:.2f}%")
print(f"Fornite - {fornite_percentage:.2f}%")
print(f"Overwatch - {overwatch_percentage:.2f}%")
print(f"Others - {others_percentage:.2f}%")