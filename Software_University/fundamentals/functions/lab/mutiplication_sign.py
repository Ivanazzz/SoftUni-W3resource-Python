def multiplicationSign():
    number1 = int(input())
    number2 = int(input())
    number3 = int(input())
    
    if (number1 < 0) or (number2 < 0) or (number3 < 0):
        return "negative"
    elif (number1 == 0) or (number2 == 0) or (number3 == 0):
        return "zero"
    else:
        return "positive"
        
print(multiplicationSign())