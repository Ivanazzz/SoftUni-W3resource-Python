exam_hour = int(input("Enter the hour when the exam starts: "))
exam_min = int(input("Enter the minutes when the exam starts: "))
arrival_hour = int(input("Enter the hour when you arrived for the exam: "))
arrival_min = int(input("Enter the minutes when you arrived for the exam: "))

exam_time = exam_min + (exam_hour * 60)
arrival_time = arrival_min + (arrival_hour * 60)
diff = exam_time - arrival_time

if diff < 0:
    print("Late")
    diff = abs(diff)
    if arrival_time != exam_time:
        hours = diff // 60
        minutes = diff % 60
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours after the start")
        else:
            print(f"{minutes} minutes after the the start")
elif 0 <= diff <= 30:
    print("On time")
    if diff > 0:
        print(f"{diff} minutes before the the start")
else:
    print("Early")
    if arrival_time != exam_time:
        hours = diff // 60
        minutes = diff % 60
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours after the start")
        else:
            print(f"{minutes} minutes after the the start")


