number = int(input("Enter number: "))
 
for i in range(number + 1):
    print("*" * i)
for i in range(number - 1, -1, -1):
    print("*" * i)