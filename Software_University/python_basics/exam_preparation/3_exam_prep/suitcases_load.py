trunck_capacity = float(input())
is_valid = True
suitcase_count = 0

while True:
    suitcase_volume = input()
    if suitcase_volume == "End":
        break
    suitcase_volume = float(suitcase_volume)
    if suitcase_count % 3 == 0:
        suitcase_volume += suitcase_volume * 0.1
    if suitcase_volume > trunck_capacity:
        is_valid = False
        break
    else:
        trunck_capacity -= suitcase_volume
    suitcase_count += 1

if is_valid:
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")

print(f"Statistic: {suitcase_count} suitcases loaded.")
