drink = input()
sugar = input()
drinks_count = int(input())

if drink == "Espresso":
    if sugar == "Without":
        price = 0.90
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.20
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.20
    elif sugar == "Extra":
        price = 1.60
elif drink == "Tea":
    if sugar == "Without":
        price = 0.50
    elif sugar == "Normal":
        price = 0.60
    elif sugar == "Extra":
        price = 0.70

total_price = drinks_count * price

if sugar == "Without":
    total_price -= total_price * 0.35
if drink == "Espresso":
    if drinks_count >= 5:
        total_price -= total_price * 0.25
if total_price > 15:
    total_price -= total_price * 0.2

print(f"You bought {drinks_count} cups of {drink} for {total_price:.2f} lv.")