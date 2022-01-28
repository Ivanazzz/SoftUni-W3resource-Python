days = int(input("Enter the amount of days: "))
room_type = input("Enter the room type(room for one person, apartment, president apartment): ")
rate = input("Enter your rate(positive, negative): ")

nights = days - 1
discount = 0

if days < 10:
    if room_type == "room for one person":
        price_per_night = 18.00
    elif room_type == "apartment":
        price_per_night = 25.00
        discount = 0.3
    elif room_type == "president apartment":
        price_per_night = 35.00
        discount = 0.1
elif 10 <= days <= 15:
    if room_type == "room for one person":
        price_per_night = 18.00
    elif room_type == "apartment":
        price_per_night = 25.00
        discount = 0.35
    elif room_type == "president apartment":
        price_per_night = 35.00
        discount = 0.15 
elif days > 15:
    if room_type == "room for one person":
        price_per_night = 18.00
    elif room_type == "apartment":
        price_per_night = 25.00
        discount = 0.5
    elif room_type == "president apartment":
        price_per_night = 35.00
        discount = 0.2

total_sum = (nights * price_per_night) - (nights * price_per_night * discount)

if rate == "positive":
    total_price = total_sum + (total_sum * 0.25)
else:
    total_price = total_sum - (total_sum * 0.1)

print(f"{total_price:.2f}")