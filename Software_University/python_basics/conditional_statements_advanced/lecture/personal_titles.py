age = float(input("Enter your age: "))
gender = input("Enter your gender (m or f): ")

if gender == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
else:
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")