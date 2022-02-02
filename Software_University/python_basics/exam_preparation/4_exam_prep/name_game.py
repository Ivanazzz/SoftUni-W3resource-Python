first_player_points = 0

points_list = []
players_name_list = []

while True:
    points = 0
    players_name = input()
    if players_name == "Stop":
        break
    players_name_list.append(players_name)
    for i in range(len(players_name)):
        number = int(input())
        if number == ord(players_name[i]):
            points += 10
        else:
            points += 2
    points_list.append(points)

if points_list[0] > points_list[1]:
    print(f"The winner is {players_name_list[0]} with {points_list[0]} points!")
else:
    print(f"The winner is {players_name_list[1]} with {points_list[1]} points!")