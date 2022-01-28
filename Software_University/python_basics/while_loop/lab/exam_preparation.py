max_poor_grades = int(input("Enter the count of failed tresholds: "))

problems_count = 0
problems_sum = 0
poor_grades = 0
last_problem = ""
has_passed = True

problem_name = input("Enter the task's name: ")

while problem_name != "Enough":
    last_problem = problem_name
    grade = int(input("Enter yout evaluation: "))
    problems_count += 1
    problems_sum += grade

    if grade <= 4:
        poor_grades += 1
        if poor_grades == max_poor_grades:
            print(f"You need a break, {poor_grades} poor grades.")
            has_passed = False
            break
    
    problem_name = input("Enter the task's name: ")


if has_passed:
    print(f"Average score: {problems_sum / problems_count:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {last_problem}")