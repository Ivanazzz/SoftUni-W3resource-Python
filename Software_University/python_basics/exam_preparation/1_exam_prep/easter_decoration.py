number_of_clients = int(input("Enter the number of clients: "))
average_price = 0

for client in range(number_of_clients):
    items_count_per_client = 0
    total_price = 0
    while True:
        command = input("Enter item to buy or 'Finish' to quit: ")
        if command == "Finish":
            if items_count_per_client % 2 == 0:
                total_price -= total_price * 0.2
            print(f"You purchased {items_count_per_client} items for {total_price:.2f} leva.")
            break
        
        item = command
        if item == "basket":
            total_price += 1.50
            items_count_per_client += 1
        elif item == "wreath":
            total_price += 3.80
            items_count_per_client += 1
        elif item == "chocolate bunny":
            total_price += 7
            items_count_per_client += 1
    
    average_price += total_price
            
print(f"Average bill per client is: {(average_price / number_of_clients):.2f} leva.")