budget = int(input("Enter your budget: "))
season = input("Enter the season(Spring, Summer, Autumn, Winter): ")
fisherman_count = int(input("Enter the fishermans count: "))

if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == 'Autumn':
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if fisherman_count <= 6:
    discount = 0.1
elif 7 <= fisherman_count <= 11:
    discount = 0.15
elif fisherman_count >= 12:
    discount = 0.25 

if fisherman_count % 2 == 0 and season != "Autumn":
    even_discount = 0.05
else:
    even_discount = 0

first_sum = boat_rent - (boat_rent * discount)
second_sum = first_sum - (first_sum * even_discount)

money_left = abs(budget - second_sum)

if budget < second_sum:
    print(f"Not enough money! You need {money_left:.2f} leva.")
else:
    print(f"Yes! You have {money_left:.2f} leva left.")