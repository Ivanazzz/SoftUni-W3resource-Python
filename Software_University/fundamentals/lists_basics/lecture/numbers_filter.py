n = int(input("Enter number: "))
number_list = []
list_output = []

for i in range(n):
    number = int(input("Enter number: "))
    number_list.append(number)

command = input("Enter(even, odd, negative, positive): ")

if command == "even":
    for num in number_list:
        if num % 2 == 0 or num == 0:
            list_output.append(num)
elif command == "odd":
    for num in number_list:
        if num % 2 != 0:
            list_output.append(num)
elif command == "negative":
    for num in number_list:
        if num < 0:
            list_output.append(num)
elif command == "positive":
    for num in number_list:
        if num >= 0:
            list_output.append(num)
            
print(list_output)