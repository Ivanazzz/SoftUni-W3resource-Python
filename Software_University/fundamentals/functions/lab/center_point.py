import math

def function():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    
    line1 = math.sqrt((x1 ** 2) + (y1 ** 2))
    line2 = math.sqrt((x2 ** 2) + (y2 ** 2))
    
    if line1 > line2:
        print(f"({math.floor(x2)}, {math.floor(y2)})")
    else:
        print(f"({math.floor(x1)}, {math.floor(y1)})")
        
function()