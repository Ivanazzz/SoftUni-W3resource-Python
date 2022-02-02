budget = float(input())
product_count = 0
products_price = 0

while True:
    product = input()
    if product == "Stop":
        print(f"You bought {product_count} products for {products_price:.2f} leva.")
        break
    price = float(input())
    if price > budget:
        print("You don't have enough money!")
        print(f"You need {(price - budget):.2f} leva!")
        break
    product_count += 1
    if product_count % 3 == 0:
        products_price += price / 2
        budget -= price / 2
    else:
        products_price += price
        budget -= price