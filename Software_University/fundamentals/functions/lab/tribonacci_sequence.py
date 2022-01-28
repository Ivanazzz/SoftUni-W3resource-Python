def tribonacciSequence():
    number = int(input())
    a, b, c = 0, 0, 1
    
    for i in range(number):
        if i == 1:
            print(c, end = " ")
        d = a + b + c
        if i == (number - 1):
            break
        print(d, end = " ")
        a, b, c = b, c, d

tribonacciSequence()