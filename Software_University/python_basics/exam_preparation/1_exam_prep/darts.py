players_name = input("Enter the player's name: ")
players_current_points = 301
successful_shots = 0
unsuccessful_shots = 0

while True:
    command = input("Enter command 'Single, Double, Triple, Retire': ")
    
    if command == "Retire":
        print(f"{players_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break
    
    points = int(input("Enter points: "))
    
    if command == "Single":
        single_points = points
        if single_points > players_current_points:
            unsuccessful_shots += 1
        else:
            successful_shots += 1
            players_current_points -= single_points
            
    elif command == "Double":
        double_points = points * 2
        if double_points > players_current_points:
            unsuccessful_shots += 1
        else:
            successful_shots += 1
            players_current_points -= double_points
            
    elif command == "Triple":
        triple_points = points * 3
        if triple_points > players_current_points:
            unsuccessful_shots += 1
        else:
            successful_shots += 1
            players_current_points -= triple_points
            
    if players_current_points == 0:
        print(f"{players_name} won the leg with {successful_shots} shots.")
        break
