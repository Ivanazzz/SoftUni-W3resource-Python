number = int(input("Enter number: "))
 
for num in range(1, number + 1):
    num = str(num)
    digits_sum = 0
    for digit in range(len(num)):
        digits_sum += int(num[digit])
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
         print(f"{num} -> True")
    else:
        print(f"{num} -> False")