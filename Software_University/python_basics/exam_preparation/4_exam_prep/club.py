desired_income = float(input())
total_price = 0

while True:
    price = 0
    cocktail_name = input()
    if cocktail_name == "Party!":
        print(f"We need {(desired_income - total_price):.2f} leva more.")
        break
    cocktails_count = int(input())
    price = len(cocktail_name) * cocktails_count
    if price % 2 != 0:
        price -= price * 0.25
    total_price += price
    if total_price >= desired_income:
        print("Target acquired.")
        break

print(f"Club income - {total_price:.2f} leva.")