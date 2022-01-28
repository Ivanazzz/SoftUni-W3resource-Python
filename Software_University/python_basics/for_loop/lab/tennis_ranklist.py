from math import floor

tournamnet_count = int(input("Enter the tournamnets count: "))
initial_points = int(input("Enter the startup points: "))

tournament_points = 0
won_touranments = 0

for tournamnet in range(tournamnet_count):
    position_finished = input("Enter the position he finished in the tournament(W, F, SF): ")
    if position_finished == "W":
        tournament_points += 2000
        won_touranments += 1
    elif position_finished == "F":
        tournament_points += 1200
    elif position_finished == "SF":
        tournament_points += 720

total_points = initial_points + tournament_points
average_points = tournament_points / tournamnet_count
won_tournaments_percent = won_touranments / tournamnet_count * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{won_tournaments_percent:.2f}%")
