budget = float(input("Enter the budget: "))
amount_of_video_card = int(input("Enter the number of video cards: "))
amount_of_processor = int(input("Enter the number of processors: "))
amount_of_ram_memory = int(input("Enter the number of ram memory: "))

video_card_price_per_one = 250
video_card_total_price = amount_of_video_card * video_card_price_per_one
processor_price_per_one = video_card_total_price * 0.35
processor_total_price = amount_of_processor * processor_price_per_one
ram_memory_per_one = video_card_total_price * 0.1
ram_memory_total_price = amount_of_ram_memory * ram_memory_per_one

total_sum = video_card_total_price + processor_total_price + ram_memory_total_price

if amount_of_video_card > amount_of_processor:
    total_sum = total_sum - total_sum * 0.15

money_left = abs(budget - total_sum)

if budget >= total_sum:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_left:.2f} leva more!")