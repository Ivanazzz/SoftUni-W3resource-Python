done_walking = False
total_steps = 0

while True:
    steps = input("Enter your steps you walked: ")
    if steps != "Going home":
        steps = int(steps)
        total_steps += steps
        if total_steps >= 10000:
            done_walking = True
            break
    else:
        last_steps = int(input("Enter your steps you walked: "))
        total_steps += last_steps
        if total_steps >= 10000:
            done_walking = True
        break

if done_walking:
    print("Goal reached! Good job!")
    print(f"{total_steps - 10000} steps over the goal!")
else:
    print(f"{10000 - total_steps} more steps to reach goal.")
