from math import ceil

walls_hight = int(input())
walls_witdh = int(input())
percentage_walls_tottal_area_not_painted = int(input())

total_walls_area = walls_hight * walls_witdh * 4
quadratic_meters_left = total_walls_area - ceil(total_walls_area * percentage_walls_tottal_area_not_painted / 100)

while True:
    paint_liters = input()
    if paint_liters == "Tired!":
        print(f"{quadratic_meters_left} quadratic m left.")
        break
    paint_liters = int(paint_liters)
    quadratic_meters_left -= paint_liters

    if quadratic_meters_left < 0:
        print(f"All walls are painted and you have {abs(quadratic_meters_left)} l paint left!")
        break
    elif quadratic_meters_left == 0:
        print("All walls are painted! Great job, Pesho!")
        break
