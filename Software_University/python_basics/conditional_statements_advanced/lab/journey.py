budget = float(input("Enter yout budget: "))
season = input("Enter season(summer, winter): ")

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        money_for_the_trip = budget * 0.3
        place = "Camp"
    elif season == "winter":
        money_for_the_trip = budget * 0.7
        place = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        money_for_the_trip = budget * 0.4
        place = "Camp"
    elif season == "winter":
        money_for_the_trip = budget * 0.8
        place = "Hotel"
if budget > 1000:
    destination = "Europe"
    money_for_the_trip = budget * 0.9
    place = "Hotel"

print(f"Somewhere in {destination} \n{place} - {money_for_the_trip:.2f}")
