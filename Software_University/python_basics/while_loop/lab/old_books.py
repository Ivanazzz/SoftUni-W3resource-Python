favourite_book = input("Enter the book's name you are searching for: ")
books_count = 0
found_it = False
book = input("Enter the name of the book you found: ")

while book != "No More Books":
    if book == favourite_book:
        found_it = True
        break
    books_count += 1
    book = input("Enter the name of the book you found: ")
    

if found_it:
    print(f"You checked {books_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")
