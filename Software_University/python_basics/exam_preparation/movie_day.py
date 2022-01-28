photoshoot_time = int(input("Enter the photoshoot time: "))
number_of_scenes = int(input("Enter the number of scenes: "))
time_per_scene = int(input("Enter the time per scene: "))

field_preparation_time = photoshoot_time * 0.15
total_needed_time = field_preparation_time + (number_of_scenes * time_per_scene)

if total_needed_time <= photoshoot_time:
    print(f"You managed to finish the movie on time! You have {round(photoshoot_time - total_needed_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(total_needed_time - photoshoot_time)} minutes.")