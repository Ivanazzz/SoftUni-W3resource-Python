name = input("Enter your name: ")
grade = 0
evaluation_sum = 0
passed = True

while grade < 12:
    evaluation = float(input("Enter your evaluation: "))
    grade += 1
    if evaluation == 2:
        passed = False
        print(f"{name} has been excluded at {grade} grade")
        break
    evaluation_sum += evaluation

if passed:
    average_evaluation = evaluation_sum / grade
    print(f"{name} graduated. Average grade: {average_evaluation:.2f}")

