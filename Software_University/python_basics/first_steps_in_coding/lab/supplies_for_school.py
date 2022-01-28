pens_pack_price = 5.80
markers_pack_price = 7.20
whiteboard_cleaner_per_liter_price = 1.20

amount_pen_packs = int(input("Enter the amount of pen packs: "))
amount_marker_packs = int(input("Enter the amount of marker packs: "))
whiteboard_cleaner_liters = int(input("Enter the ampunt of liters of whiteboard cleaner: "))
discount = int(input("Enter the amount of discount: "))

total_price_pen_packs = amount_pen_packs * pens_pack_price
total_price_marker_packs = amount_marker_packs * markers_pack_price
total_price_whiteboard_cleaner = whiteboard_cleaner_liters * whiteboard_cleaner_per_liter_price
total_price_products = total_price_pen_packs + total_price_marker_packs + total_price_whiteboard_cleaner
total_price_with_discount = total_price_products - (total_price_products * discount / 100)
print(f"{total_price_with_discount:.2f}")