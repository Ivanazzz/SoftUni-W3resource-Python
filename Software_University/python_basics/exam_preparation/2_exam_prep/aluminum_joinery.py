joinery_count = int(input())
joinery_type = input()
shipment_method = input()

price_per_joinery = 0
discount = 0
is_valid = True

if joinery_count < 10:
    is_valid = False

if joinery_type == "90X130":
    price_per_joinery = 110
    if joinery_count > 60:
        discount = 0.08
    elif joinery_count > 30:
        discount = 0.05
elif joinery_type == "100X150":
    price_per_joinery = 140
    if joinery_count > 80:
        discount = 0.1
    elif joinery_count > 40:
        discount = 0.06
elif joinery_type == "130X180":
    price_per_joinery = 190
    if joinery_count > 50:
        discount = 0.12
    elif joinery_count > 20:
        discount = 0.07
elif joinery_type == "200X300":
    price_per_joinery = 250 
    if joinery_count > 50:
        discount = 0.14
    elif joinery_count > 25:
        discount = 0.09

joinery_price = (price_per_joinery * joinery_count) - ((price_per_joinery * joinery_count) * discount)

if shipment_method == "With delivery":
    joinery_price += 60

if joinery_count > 99:
    joinery_price -= joinery_price * 0.04

if is_valid:
    print(f"{joinery_price:.2f} BGN")
else:
    print("Invalid order")