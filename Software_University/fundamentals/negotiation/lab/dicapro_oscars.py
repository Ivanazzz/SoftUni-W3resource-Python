number = int(input("Enter number: "))
if number == 88:
    message = "Leo finally won the Oscar! Leo is happy"
elif number == 86:
    message = "Not even for Wolf of Wall Street?!"
elif (number !=  88) and (number != 86):
    if number < 88:
        message = "When will you give Leo an Oscar?"
    elif number > 88:
        message = "Leo got one already!"

print(message)