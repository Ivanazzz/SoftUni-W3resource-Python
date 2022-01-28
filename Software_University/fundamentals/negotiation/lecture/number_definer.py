number = float(input("Enter number: "))
 
if number == 0:
    print("zero")
elif number > 0:
    if 0 < number < 1:
        number_type = "small positive"
    elif 1 <= number <= 1000000:
        number_type = "positive"
    else:
        number_type = "large positive"
else:
    if -1 < number < 0:
        number_type = "small negative"
    elif -1000000 <= number <= -1:
        number_type = "negative"
    else:
        number_type = "large negative"
        
print(number_type)