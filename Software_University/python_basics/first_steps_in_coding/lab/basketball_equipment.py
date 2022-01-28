price_basket_per_year = int(input("Enter the price for the basketball course per year: "))
basket_shoes = price_basket_per_year - (price_basket_per_year * 0.4)
basket_clothes = basket_shoes - (basket_shoes * 0.2)
basket_ball = basket_clothes / 4
basket_accessories = basket_ball / 5
total_price_equipment = price_basket_per_year + basket_shoes + basket_clothes + basket_ball + basket_accessories
print(f"{total_price_equipment:.2f}")