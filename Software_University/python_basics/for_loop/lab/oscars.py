actor_name = input("Enter the actor's name: ")
initial_points = int(input("Enter the points form academy: "))
judges_count = int(input("Enter the number of jury: "))

points_needed = 1250.5

for jury in range(judges_count):
    judges_name = input("Enter the name of jury: ")
    points_from_judge = float(input("Enter the points from the jury: "))

    initial_points += ((len(judges_name) * points_from_judge) / 2)

    if initial_points > points_needed:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {initial_points:.1f}!")
        break

if initial_points <= points_needed:
    print(f"Sorry, {actor_name} you need {points_needed - initial_points:.1f} more!")
