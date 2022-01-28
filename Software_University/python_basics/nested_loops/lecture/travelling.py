command = input("Enter destination or 'End' to quit: ")

while command != "End":
    destination = command
    needed_money = float(input("Enter needed money for the trip: "))
    collected_money = 0
    while collected_money < needed_money:
        current_sum = float(input("Enter money: "))
        collected_money += current_sum
    print(f"Going to {destination}!")
    command = input("Enter destination or 'End' to quit: ")