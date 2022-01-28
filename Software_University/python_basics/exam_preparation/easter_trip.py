destination = input("Enter destination: ")
reservation_date = input("Enter the date of reservation: ")
overnights = int(input("Enter the number of overnights: "))

if reservation_date == "21-23":
    if destination == "France":
        price = 30
    elif destination == "Italy":
        price = 28
    elif destination == "Germany": 
        price = 32
elif reservation_date == "24-27":
    if destination == "France":
        price = 35
    elif destination == "Italy":
        price = 32
    elif destination == "Germany": 
        price = 37
elif reservation_date == "28-31":
    if destination == "France":
        price = 40
    elif destination == "Italy":
        price = 39
    elif destination == "Germany": 
        price = 43
        
total_price = overnights * price
print(f"Easter trip to {destination} : {total_price:.2f} leva.")
