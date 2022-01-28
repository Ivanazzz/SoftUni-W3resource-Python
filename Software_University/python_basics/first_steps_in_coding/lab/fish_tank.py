lenght = int(input("Enter the lenght of the fish tank: "))
width = int(input("Enter the width of the fish tank: "))
hight = int(input("Enter the hight of the fish tank: "))
percentage_used_space = float(input("Enter the percentage of used spase in the fish tank: "))

capacity_fish_tank = lenght * width * hight
capacity_per_liters = capacity_fish_tank / 1000
needed_liters = capacity_per_liters * (1 - (percentage_used_space / 100))

print(needed_liters)