luggage_price_above_20_kg = float(input())
luggage_kg = float(input())
days_to_flight = int(input())
luggage_count = int(input())

if luggage_kg <= 10:
    luggage_total_price = luggage_price_above_20_kg * 0.2
elif luggage_kg <= 20:
    luggage_total_price = luggage_price_above_20_kg * 0.5 
else:
    luggage_total_price = luggage_price_above_20_kg

if days_to_flight < 7:
    luggage_total_price += luggage_total_price * 0.4
elif days_to_flight <= 30:
    luggage_total_price += luggage_total_price * 0.15
else:
    luggage_total_price += luggage_total_price * 0.1

total_price = luggage_count * luggage_total_price

print(f"The total price of bags is: {total_price:.2f} lv.")