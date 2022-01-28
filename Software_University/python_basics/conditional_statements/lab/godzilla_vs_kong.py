budget_for_the_film = float(input("Enter the budget for the film: "))
number_of_extras = int(input("Enter the number of extras: "))
clothes_price_per_extra = float(input("Enter the price of the clothes per extra: "))

decor_price = budget_for_the_film * 0.1
clothes_price = number_of_extras * clothes_price_per_extra

if number_of_extras > 150:
    clothes_price = clothes_price - clothes_price * 0.1

total_amount = decor_price + clothes_price
left_money = abs(budget_for_the_film - total_amount)

if budget_for_the_film > total_amount:
    print(f"Action! \nWingard starts filming with {left_money:.2f} leva left.")
else:
    print(f"Not enough money! \nWingard needs {left_money:.2f} leva more.")