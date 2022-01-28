price_chicken_menu = 10.35
price_fish_menu = 12.40
price_vegeterian_menu = 8.15

amount_chicken_menus = int(input('Enter the amount of chicken menus: '))
amount_fish_menus = int(input("Enter the amount of fish menus: "))
amount_vegeterian_menus = int(input("Enter the amount of vegeterian menus: "))

total_price_chicken_menus = amount_chicken_menus * price_chicken_menu
total_price_fish_menus = amount_fish_menus * price_fish_menu
total_price_vegeterian_menus = amount_vegeterian_menus * price_vegeterian_menu
total_menus_price = total_price_chicken_menus + total_price_fish_menus + total_price_vegeterian_menus
dessert_price = total_menus_price * 0.2
delivery_price = 2.50
total_delivery_price = total_menus_price + dessert_price + delivery_price

print(f"{total_delivery_price:.2f}")