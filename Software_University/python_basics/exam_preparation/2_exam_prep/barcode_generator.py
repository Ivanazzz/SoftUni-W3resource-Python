first_number = int(input())
second_number = int(input())

for i in range(first_number, second_number):
    barcode = i
    num1 = i % 10
    i //= 10
    num2 = i % 10
    i //= 10
    num3 = i % 10
    i //= 10
    num4 = i % 10

    if num1 % 2 != 0:
        if num2 % 2 != 0:
            if num3 % 2 != 0:
                if num4 % 2 != 0:
                    print(barcode, end = " ")