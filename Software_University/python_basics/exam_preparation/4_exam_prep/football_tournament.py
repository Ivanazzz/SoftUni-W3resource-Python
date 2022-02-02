football_team_name = input()
played_games = int(input())

is_valid = True

if played_games == 0:
    is_valid = False
    print(f"{football_team_name} hasn't played any games during this season.")

wins = 0
equality = 0
loses = 0

for game in range(played_games):
    result = input()
    if result == "W":
        wins += 1
    elif result == "D":
        equality += 1
    elif result == "L":
        loses += 1

points = (wins * 3) + (equality * 1)

if is_valid:
    print(f"{football_team_name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {equality}")
    print(f"## L: {loses}")
    print(f"Win rate: {(wins / played_games * 100):.2f}%")