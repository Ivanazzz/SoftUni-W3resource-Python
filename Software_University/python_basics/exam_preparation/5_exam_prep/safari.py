budget = float(input())
fuel_liters_needed = float(input())
day = input()

fuel_price = fuel_liters_needed * 2.10
price = fuel_price + 100

if day == "Saturday":
    price -= price * 0.1
elif day == "Sunday":
    price -= price * 0.2

if budget >= price:
    print(f"Safari time! Money left: {(budget - price):.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {(price - budget):.2f} lv.")