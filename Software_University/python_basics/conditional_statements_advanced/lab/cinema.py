screening_type = input("Enter the screening type: ")
rows = int(input("Enter the amount of rows: "))
columns = int(input("Emter the amount of columns: "))

premiere_price = 12.00
normal_price = 7.50
discount_price = 5.00

if screening_type == "Premiere":
    total_sum = rows * columns * premiere_price
elif screening_type == "Normal":
    total_sum = rows * columns * normal_price
elif screening_type == "Discount":
    total_sum = rows * columns * discount_price

print(f"{total_sum:.2f} leva")