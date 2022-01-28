hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))

new_minutes = minutes + 15

if new_minutes >= 60:
    hours += 1
    new_minutes = new_minutes % 60
    if hours >= 24:
        hours = 0

if new_minutes <= 9:
    print(f"{hours}:0{new_minutes}")
else:
    print(f"{hours}:{new_minutes}")