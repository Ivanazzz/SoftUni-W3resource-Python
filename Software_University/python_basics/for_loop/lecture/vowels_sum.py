text = input("Enter text: ")
count = 0
for char in text:
    if char == "a":
        count +=1
    if char == "e":
        count += 2
    if char == "i":
        count += 3
    if char == "o":
        count += 4
    if char == "u":
        count += 5
print(count)