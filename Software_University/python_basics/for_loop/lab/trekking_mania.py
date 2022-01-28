group_climbers_amount = int(input("Enter the number of groups: "))

total_amount_climbers = 0
musala_count = 0
monblan_count = 0
kilimandjaro_count = 0
ktwo_count = 0
everest_count = 0

for group in range(group_climbers_amount):
    climbers_in_group = int(input("Enter the number of climbers in the current group: "))
    total_amount_climbers += climbers_in_group
    if climbers_in_group <= 5:
        musala_count += climbers_in_group
    elif climbers_in_group <= 12:
        monblan_count += climbers_in_group
    elif climbers_in_group <= 25:
        kilimandjaro_count += climbers_in_group
    elif climbers_in_group <= 40:
        ktwo_count += climbers_in_group
    elif climbers_in_group > 40:
        everest_count += climbers_in_group

total_climbers_musala = musala_count / total_amount_climbers * 100
total_climbers_monblan = monblan_count / total_amount_climbers * 100
total_climbers_kilimandjaro = kilimandjaro_count / total_amount_climbers * 100
total_climbers_ktwo = ktwo_count / total_amount_climbers * 100
total_climbers_everest = everest_count / total_amount_climbers * 100

print(f"{total_climbers_musala:.2f}%")
print(f"{total_climbers_monblan:.2f}%")
print(f"{total_climbers_kilimandjaro:.2f}%")
print(f"{total_climbers_ktwo:.2f}%")
print(f"{total_climbers_everest:.2f}%")