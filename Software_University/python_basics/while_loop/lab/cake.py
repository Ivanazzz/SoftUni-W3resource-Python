width = int(input("Enter the width of the cake: "))
lenght = int(input("Enter the lenght of the cake: "))
total_pieces = width * lenght
enough_pieces = True

command = input("Enter the pieces of cake or 'Stop' to quit: ")

while command != "STOP":
    command = int(command)
    total_pieces -= command
    if total_pieces < 0:
        enough_pieces = False
        break
    command = input("Enter the pieces of cake or 'Stop' to quit: ")

if enough_pieces:
    print(f"{total_pieces} pieces are left." )  
else:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")