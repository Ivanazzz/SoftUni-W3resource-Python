coloured_eggs_count = int(input("Enter the number of coloured eggs: "))
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
number_of_max_eggs_from_same_colour = 0
colour_of_max_eggs = ""

for egg in range(coloured_eggs_count):
    egg_colour = input("Enter the egg's colour: ")
    if egg_colour == "red":
        red_eggs += 1
        if red_eggs > number_of_max_eggs_from_same_colour:
            number_of_max_eggs_from_same_colour = red_eggs
            colour_of_max_eggs = "red"
    elif egg_colour == "orange":
        orange_eggs += 1
        if orange_eggs > number_of_max_eggs_from_same_colour:
            number_of_max_eggs_from_same_colour = orange_eggs
            colour_of_max_eggs = "orange"
    elif egg_colour == "blue":
        blue_eggs += 1
        if blue_eggs > number_of_max_eggs_from_same_colour:
            number_of_max_eggs_from_same_colour = blue_eggs
            colour_of_max_eggs = "blue"
    else:
        green_eggs += 1
        if green_eggs > number_of_max_eggs_from_same_colour:
            number_of_max_eggs_from_same_colour = green_eggs
            colour_of_max_eggs = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {number_of_max_eggs_from_same_colour} -> {colour_of_max_eggs}")