name_of_the_series = input("Enter name of the series: ")
episode_duration = int(input("Enter the episode duration: "))
break_duration = int(input("Enter the break duration: "))

lunch_time = break_duration / 8
rest_time = break_duration / 4

total_time = episode_duration + lunch_time + rest_time
left_minutes = abs(break_duration - total_time)

if total_time <= break_duration:
    print(f"You have enough time to watch {name_of_the_series} and left with {left_minutes} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_the_series}, you need {left_minutes} more minutes.")