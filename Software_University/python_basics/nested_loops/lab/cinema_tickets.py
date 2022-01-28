film_name = input("Enter the film's name or 'Finish' to quit: ")
total_tickets_count = 0
student_tickets_count = 0
standart_tickets_count = 0
kid_tickets_count = 0

while film_name != "Finish":
    total_seats = int(input("Enter the amount of free seats: "))
    occupied_seats_counter = 0
    type_of_seat = input("Enter the type of seat: ")
    
    while type_of_seat != "End":
        occupied_seats_counter += 1
        total_tickets_count += 1
        
        if type_of_seat == "student":
            student_tickets_count += 1
        elif type_of_seat == "standart":
            standart_tickets_count += 1
        else:
            kid_tickets_count += 1
            
        if occupied_seats_counter == total_seats:
            break
        
        type_of_seat = input("Enter the type of seat: ")
            
    print(f"{film_name} - {occupied_seats_counter / total_seats * 100:.2f}% full.")
    
    film_name = input("Enter the film's name or 'Finish' to quit: ")
    
print(f"Total tickets: {total_tickets_count}")
print(f"{student_tickets_count / total_tickets_count * 100:.2f}% student tickets.")
print(f"{standart_tickets_count / total_tickets_count * 100:.2f}% standart tickets.")
print(f"{kid_tickets_count / total_tickets_count * 100:.2f}% kids tickets.")
            