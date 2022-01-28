age = int(input("Enter age: "))
washing_machine_price = float(input("Enter the price for the washing mashine: "))
price_per_toy = int(input("Enter the price per each toy: "))

money_saved = 0
toys_count = 0
amount = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        amount += 10
        money_saved += amount - 1
    elif birthday % 2 != 0:
        toys_count += 1

money_form_toys = toys_count * price_per_toy
total_money = money_saved + money_form_toys
diff = abs(washing_machine_price - total_money)

if total_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")