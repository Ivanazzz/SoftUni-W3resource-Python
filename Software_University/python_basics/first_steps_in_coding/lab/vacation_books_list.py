book_pages = int(input("Enter the amount of pages of the current book: "))
pages_per_hour = int(input("Enter the amount of pages readed per hour: "))
days = int(input("Enter the amount of days for which you must read the book: "))
total_reading_time = book_pages // pages_per_hour
hours_needed_per_day = total_reading_time / days
print(f"{hours_needed_per_day:.0f}")