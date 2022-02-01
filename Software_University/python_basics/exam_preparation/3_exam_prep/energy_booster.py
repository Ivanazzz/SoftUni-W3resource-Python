fruit = input()
size = input()
sets_count = int(input())

discount = 0

if size == "small":
    if fruit == "Watermelon":
        price = 2 * 56
    elif fruit == "Mango":
        price = 2 * 36.66
    elif fruit == "Pineapple":
        price = 2 * 42.10
    elif fruit == "Raspberry":
        price = 2 * 20
elif size == "big":
    if fruit == "Watermelon":
        price = 5 * 28.70
    elif fruit == "Mango":
        price = 5 * 19.60
    elif fruit == "Pineapple":
        price = 5 * 24.80
    elif fruit == "Raspberry":
        price = 5 * 15.20

total_price = sets_count * price

if total_price >= 400 and total_price <= 1000:
    discount = 0.15
elif total_price > 1000:
    discount = 0.50

total_price -= total_price * discount
print(f"{total_price:.2f} lv.")