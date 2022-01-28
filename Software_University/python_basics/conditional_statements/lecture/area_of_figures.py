from math import pi

figure_type = input("Enter the the type of figure: ")

if figure_type == "square":
    side_lenght = float(input("Enter the lengt of the side: "))
    square_area = side_lenght ** 2
    print(f"{square_area:.3f}")
elif figure_type == "rectangle":
    first_side_lenght = float(input("Enter the lengt of the first side: "))
    second_side_lenght = float(input("Enter the lengt of the second side: "))
    rectangle_area = first_side_lenght * second_side_lenght
    print(f"{rectangle_area:.3f}")
elif figure_type == "circle":
    radius = float(input("Enter the radius of the circle: "))
    circle_area = pi * (radius ** 2)
    print(f"{circle_area:.3f}")
elif figure_type == "triangle":
    side_lenght = float(input("Enter the lengt of the side: "))
    hight_lenght = float(input("Enter the lengt of the hight: "))
    triangle_area = side_lenght * hight_lenght / 2
    print(f"{triangle_area:.3f}")