nums_count = int(input())
p1 = 0
p2 = 0
p3 = 0

for num in range(nums_count):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

p1_result = p1 / nums_count * 100
p2_result = p2 / nums_count * 100
p3_result = p3 / nums_count * 100

print(f"{p1_result:.2f}%")
print(f"{p2_result:.2f}%")
print(f"{p3_result:.2f}%")