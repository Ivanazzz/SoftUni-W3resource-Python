width = int(input("Enter width: "))
lenght = int(input("Enter lenght: "))
high = int(input("Enter high: "))

total_space = width * lenght * high
enough_space = True

boxes = input("Enter the amount of boxes or 'Done' to quit: ")

while boxes != "Done":
    boxes = int(boxes)
    total_space -= boxes
    if total_space < 0:
        enough_space = False
        break
    boxes = input("Enter the amount of boxes or 'Done' to quit: ")

if enough_space:
    print(f"{total_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_space)} Cubic meters more.")
