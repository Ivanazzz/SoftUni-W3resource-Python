jury_count = int(input("Enter the count of the jury: "))
presentation_name = input("Enter the name of the presentation or 'Finish' to quit: ")
average_grade_sum = 0
grade_counter = 0

while presentation_name != "Finish":
    average_grade = 0
    for jury in range(jury_count):
        grade = float(input("Enter the grade: "))
        grade_counter += 1
        average_grade += grade
        average_grade_sum += grade
    print(f"{presentation_name} - {average_grade / jury_count:.2f}")
    
    presentation_name = input("Enter the name of the presentation or 'Finish' to quit: ")

print(f"Student's final assessment is {average_grade_sum / grade_counter:.2f}")