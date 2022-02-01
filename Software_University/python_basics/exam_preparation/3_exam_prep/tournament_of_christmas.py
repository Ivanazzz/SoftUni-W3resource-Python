tournament_days = int(input())

total_wins = 0
total_loses = 0
money = 0

for day in range(0, tournament_days):
    total_wins_per_day = 0
    total_loses_per_day = 0
    total_money_per_day = 0
    while True:
        sport = input()
        if sport == "Finish":
            break
        else:
            result = input()
            if result == "win":
                total_money_per_day += 20
                total_wins_per_day += 1
            elif result == "lose":
                total_loses_per_day += 1
    total_wins += total_wins_per_day
    total_loses += total_loses_per_day
    if total_wins_per_day > total_loses_per_day:
        money += total_money_per_day + (total_money_per_day * 0.1)
    else:
        money += total_money_per_day

if total_wins > total_loses:
    money += money * 0.2
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")