meters = float(input("Enter the meters for landscaping: "))
price_for_landscaping = meters * 7.61
discount = price_for_landscaping * 0.18
total_price = price_for_landscaping - discount
print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")