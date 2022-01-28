flower_type = input("Enter the type of flower(Roses, Dahlias, Tulips, Narcissus, Gladiolus): ")
flower_quantity = int(input("Enter the flower quantity: "))
budget = int(input("Enter the budget: "))

roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

if flower_type == "Roses":
    total_sum = flower_quantity * roses_price
    if flower_quantity > 80:
        total_sum = total_sum - total_sum * 0.1
elif flower_type == "Dahlias":
    total_sum = flower_quantity * dahlias_price
    if flower_quantity > 90:
        total_sum = total_sum - total_sum * 0.15
elif flower_type == "Tulips":
    total_sum = flower_quantity * tulips_price
    if flower_quantity > 80:
        total_sum = total_sum - total_sum * 0.15
elif flower_type == "Narcissus":
    total_sum = flower_quantity * narcissus_price
    if flower_quantity < 120:
        total_sum = total_sum + total_sum * 0.15
elif flower_type == "Gladiolus":
    total_sum = flower_quantity * gladiolus_price
    if flower_quantity < 80:
        total_sum = total_sum + total_sum * 0.2

end_sum = abs(budget - total_sum)

if budget < total_sum:
    print(f"Not enough money, you need {end_sum:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {flower_quantity} {flower_type} and {end_sum:.2f} leva left.")