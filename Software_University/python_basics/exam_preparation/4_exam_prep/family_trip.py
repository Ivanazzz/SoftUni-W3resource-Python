budget = float(input())
nights = int(input())
price_per_night = float(input())
percentage_for_additional_costs = int(input())

if nights > 7:
    price_per_night -= price_per_night * 0.05

price = nights * price_per_night
additional_costs = budget * percentage_for_additional_costs / 100
total_price = price + additional_costs

if budget >= total_price:
    print(f"Ivanovi will be left with {(budget - total_price):.2f} leva after vacation.")
else:
    print(f"{(total_price - budget):.2f} leva needed.")