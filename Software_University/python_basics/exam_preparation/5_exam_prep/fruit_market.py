strawberries_price = float(input())
bananas_amount_kg = float(input())
oranges_amount_kg = float(input())
raspberries_amount_kg = float(input())
strawberries_amount_kg = float(input())

raspberries_price_kg = strawberries_price / 2
raspberries_total_price = raspberries_amount_kg * raspberries_price_kg
oranges_total_price = round(oranges_amount_kg  * (raspberries_price_kg - (raspberries_price_kg * 0.4)), 2)
bananas_total_price = round(bananas_amount_kg * (raspberries_price_kg - (raspberries_price_kg * 0.8)), 2)
strawberries_total_price = strawberries_amount_kg * strawberries_price

total_price = raspberries_total_price + oranges_total_price + bananas_total_price + strawberries_total_price

print(f"{total_price:.2f}")