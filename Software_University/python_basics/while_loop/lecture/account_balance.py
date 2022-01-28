command = input("Enter payment: ")
total_money = 0

while command != "NoMoreMoney" :
    current_sum = float(command)
    if current_sum < 0:
        print("Invalid operation!")
        break
    total_money += current_sum
    print(f"Increase: {current_sum:.2f}")
    command = input("Enter payment: ")

print(f"Total: {total_money:.2f}")