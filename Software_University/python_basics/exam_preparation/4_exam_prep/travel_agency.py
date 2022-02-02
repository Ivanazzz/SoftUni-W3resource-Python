city = input()
package_type = input()
vip = input()
days = int(input())

is_valid = True
total_price = 0

if days >= 1:
    if city == "Bansko" or city == "Borovets":
        if package_type == "withEquipment":
            price = 100
            if vip == "yes":
                price -= price * 0.1
        elif package_type == "noEquipment":
            price = 80
            if vip == "yes":
                price -= price * 0.05
        else:
            is_valid = False
    elif city == "Varna" or city == "Burgas":
        if package_type == "withBreakfast":
            price = 130
            if vip == "yes":
                price -= price * 0.12
        elif package_type == "noBreakfast":
            price = 100
            if vip == "yes":
                price -= price * 0.07
        else:
            is_valid = False
    else:
        is_vallid = False
else:
    print("Days must be positive number!")

if is_valid:
    if days > 7:
        total_price = (days - 1) * price
    else:
        total_price = days * price
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
else:
    print("Invalid input!")
