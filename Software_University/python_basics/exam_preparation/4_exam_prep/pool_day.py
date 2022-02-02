from math import ceil

people = int(input())
entrance_fee = float(input())
price_per_deck_chair = float(input())
price_per_umbrella = float(input())

total_entrance_fee = people * entrance_fee
deck_chair_total_price = ceil(people * 0.75) * price_per_deck_chair
umbrella_total_price = ceil(people / 2) * price_per_umbrella

total_price = total_entrance_fee + deck_chair_total_price + umbrella_total_price

print(f"{total_price:.2f} lv.")