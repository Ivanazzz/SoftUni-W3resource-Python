rent_price = int(input("Enter the price of the rent: "))

figurine_price = rent_price - (rent_price * 0.3)
catering_price = figurine_price - (figurine_price * 0.15)
music_price = catering_price / 2

total_price = rent_price + figurine_price + catering_price + music_price

print(f"{total_price:.2f}")