import sys

command = input("Enter number or 'Stop' to quit: ")
max_num = - sys.maxsize

while command != 'Stop':
    current_number = int(command)
    if current_number > max_num:
        max_num = current_number
    command = input("Enter number or 'Stop' to quit: ") 

if max_num != - sys.maxsize:
    print(max_num)