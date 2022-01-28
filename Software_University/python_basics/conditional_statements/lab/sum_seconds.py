time_first = int(input("Enter the first time: "))
time_second = int(input("Emter the second tome: "))
time_third = int(input("Enter the third time: "))

total_time = time_first + time_second + time_third

minutes = total_time // 60
seconds = total_time % 60

if seconds <= 9:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")