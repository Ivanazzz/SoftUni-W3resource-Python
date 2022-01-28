puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

trip_price = float(input("Enter the price of the trip: "))
puzzle_count = int(input("Enter the amount of puzzles: "))
doll_count = int(input("Enter the amount of dolls: "))
teddy_bear_count = int(input("Enter the amount of teddy bears: "))
minion_count = int(input("Enter the amount of minions: "))
truck_count = int(input("Enter the amount of the trucks: "))

toys_count = puzzle_count + doll_count + teddy_bear_count + minion_count + truck_count
total_toys_price = puzzle_count * puzzle_price + doll_count * doll_price + teddy_bear_count * teddy_bear_price + minion_count * minion_price + truck_count * truck_price

if toys_count >= 50:
    total_toys_price = total_toys_price - (total_toys_price * 0.25)

rent = total_toys_price * 0.1
income = total_toys_price - rent

if income >= trip_price:
    money_left = income - trip_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_left = abs(income - trip_price)
    print(f"Not enough money! {money_left:.2f} lv needed.")

