month = input("Enter month(May, June, July, August, September, October): ")
number_of_nights = int(input("Enter the number of nights: "))

if month == "May" or month == "October":
    studio_price = 50 * number_of_nights
    apartment_price = 65 * number_of_nights

    if 7 < number_of_nights < 14:
        studio_price -= studio_price * 0.05
    elif number_of_nights > 14:
        studio_price -= studio_price * 0.3
        apartment_price -= apartment_price * 0.1

elif month == "June" or month == "September":
    studio_price = 75.20 * number_of_nights
    apartment_price = 68.70 * number_of_nights
    if number_of_nights > 14:
        studio_price -= studio_price * 0.2
        apartment_price -= apartment_price * 0.1

elif month == "July" or month == "August":
    studio_price = 76 * number_of_nights
    apartment_price = 77 * number_of_nights
    if number_of_nights > 14:
        apartment_price -= apartment_price * 0.1

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
