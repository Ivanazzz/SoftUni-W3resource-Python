product_type = input("Enter the product type(coffee, water, coke, snacks): ")
quantity = int(input("Enter the quantity: "))

def price():
    if product_type == "coffee":
        total_price = quantity * 1.50
        return total_price
    elif product_type == "water":
        total_price = quantity * 1.00
        return total_price
    elif product_type == "coke":
        total_price = quantity * 1.40
        return total_price
    elif product_type == "snacks":
        total_price = quantity * 2.00
        return total_price

print(f"{price():.2f}")