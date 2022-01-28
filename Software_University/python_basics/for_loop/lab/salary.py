open_tabs_count = int(input("Enter the amount of open tabs: "))
salary = int(input("Enter the salaty: "))

for tab in range(open_tabs_count):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50
    else:
        pass

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)