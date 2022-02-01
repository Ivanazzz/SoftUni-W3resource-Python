max_goals = 0
winners_name = ""
is_valid = False

while True:
    players_name = input()
    if players_name == "END":
        break
    goals_count = int(input())

    if goals_count > max_goals:
        max_goals = goals_count
        winners_name = players_name
    
    if goals_count >= 3:
        is_valid = True

    if goals_count >= 10:
        break


print(f"{winners_name} is the best player!")

if is_valid:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")