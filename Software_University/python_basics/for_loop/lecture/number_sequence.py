number_quantity = int(input("Enter the number quantity: "))
list = []
for i in range(number_quantity):
    number = int(input("Enter number: "))
    list.append(number)
list.sort()
max_number = list[-1]
min_number = list[0]
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")