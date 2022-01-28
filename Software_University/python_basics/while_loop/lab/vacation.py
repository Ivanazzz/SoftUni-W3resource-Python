needed_money = float(input("Enter the amount of needed money for the trip: "))
owned_money = float(input("Enter the money you have: "))

days_counter = 0
spending_counter = 0

while True:
    command = input("Enter command(save or spend)")
    money = float(input("Enter the amount of money you want to save or spend: " ))
    days_counter += 1

    if command == "spend":
        spending_counter += 1        
        owned_money -= money
        if owned_money < 0:
            owned_money = 0
        if spending_counter == 5:
            print("You can't save the money.")
            print(f"{days_counter}")    
            break

    else:
        owned_money += money
        spending_counter = 0
    
    if owned_money >= needed_money:
        print(f"You saved the money for {days_counter} days.")
        break
