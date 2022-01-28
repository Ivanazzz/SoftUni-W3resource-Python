import sys

command = input("Enter number or 'Stop' to quit: ")
min_num = sys.maxsize

while command != 'Stop':
    current_number = int(command)
    if current_number < min_num:
        min_num = current_number
    command = input("Enter number or 'Stop' to quit: ") 

if min_num != sys.maxsize:
    print(min_num)