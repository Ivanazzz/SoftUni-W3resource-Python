nylon_per_sqrt_meter = 1.50
paint_per_liter = 14.50
paint_thinner_per_liter = 5.00

needed_nylon_sqrt_meters = int(input("Enter the amount of needed squared meters nylon: "))
needed_paint_per_liters = int(input("Enter the amount of needed paint per liter: "))
needed_paint_thinner_per_liters = int(input("Enter the amount of needed paint thinner per liter: "))
hours_to_be_ready = int(input("Enter the amount of hours needed for craftsman to be ready: "))

added_paint = needed_paint_per_liters * 0.1
addded_nylon = 2
added_bags = 0.40

total_price_for_nylon = (needed_nylon_sqrt_meters + addded_nylon) * nylon_per_sqrt_meter
total_price_for_paint = (needed_paint_per_liters + added_paint) * paint_per_liter
total_price_fot_paint_thinner = needed_paint_thinner_per_liters * paint_thinner_per_liter
total_price_supplies = total_price_for_nylon + total_price_for_paint + total_price_fot_paint_thinner +added_bags

craftsman_price_per_hour = total_price_supplies * 0.3
total_price_craftsman = hours_to_be_ready * craftsman_price_per_hour

total_price_for_repainting = total_price_supplies + total_price_craftsman
print(f"{total_price_for_repainting:.2f}")