while True:
    number = float(input("Enter number: "))
    if number > 1 and number < 100:
        print(f"The number {number:.1f} is between 1 and 100")
        break