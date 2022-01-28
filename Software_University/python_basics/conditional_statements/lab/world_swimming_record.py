record_in_seconds = float(input("Enter the record in seconds: "))
distance_in_meters = float(input("Enter the distance in meters: "))
seconds_per_meter = float(input("Enter the seconds per minute: "))

distance_to_swim_in_seconds = distance_in_meters * seconds_per_meter
time_delay = (distance_in_meters // 15) * 12.5
time_sum = distance_to_swim_in_seconds + time_delay

total_time = abs(record_in_seconds - time_sum)

if record_in_seconds > time_sum:
    print(f"Yes, he succeded! The new world record is {time_sum:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time:.2f} seconds slower.")
