number_of_orders = int(input("Enter the number of orders: "))
total_money = 0

for order in range(number_of_orders):
    current_total_price = 0 
    price_per_capsule = float(input("Enter the price per capsule: "))
    days = int(input("Enter number of days: "))
    capsules_count = int(input("Enter the capsule's count: "))
    current_total_price = price_per_capsule * days * capsules_count
    total_money += current_total_price
    print(f"The price for the coffee is: {current_total_price:.2f}")